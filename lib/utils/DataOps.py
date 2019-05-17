# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 09:37:41 2018

@author: socib
"""

#import seabird as sbe
from seabird.cnv import fCNV
import numpy as np
import matplotlib.pyplot as plt
import os
import gsw
import seawater as gsw_sw

import utils.ProfileSettings as ProfileSettings


def read_input_files(path_to_file, file_name):
    profile = fCNV(path_to_file + file_name)
    return profile

def get_station_names(filenames_list):
    station_names_list = []
    for i in range(0,len(filenames_list)):
        station_names_list.append(filenames_list[i][1:-4])
    return station_names_list 

def load_profile_data(profile, var_names, deployment_info):
    profile_data = ProfileSettings.import_profile_data(profile, var_names, deployment_info)
    return profile_data

def organize_profiles(profiles_data_df, profile_data, var_names, station_names_list):
    for i in range(0,len(station_names_list)):
        for j in range(0,len(var_names)):
            profiles_data_df[station_names_list[i]] += [profile_data]
    return profiles_data_df

def load_generic_stations_info():
    canales_stations_info = {'location_code': ['MC', 'ICN', 'ICM', 'ICS'] , 
                             'station_location': {'radmed_01': 'MC', 'radmed_02': 'MC', 'radmed_03': 'MC', 'radmed_04': 'MC', 'radmed_05': 'MC',
                                                  'radmed_06': 'MC', 'radmed_07': 'MC', 'radmed_08': 'MC', 'radmed_09': 'MC', 'radmed_10': 'MC',
                                                  's2_01': 'ICN', 's2_02': 'ICN', 's2_03': 'ICN', 's2_04': 'ICN', 's2_05': 'ICN', 's2_06': 'ICN',
                                                  's2_07': 'ICN', 's2_08': 'ICN', 's2_085': 'ICN', 's2_t1_end': 'ICN', 's2_09': 'ICM', 's2_10': 'ICM',
                                                  's2_11': 'ICM', 's2_12': 'ICM', 's2_13': 'ICM', 's2_14': 'ICM', 's2_15': 'ICM', 's2_16': 'ICS',
                                                  's2_17': 'ICS', 's2_18': 'ICS', 's2_19': 'ICS', 's2_20': 'ICS', 's2_21': 'ICS', 's2_22': 'ICS',
                                                  's2_23': 'ICS'},
                            'station_depth': {'radmed_01': 75, 'radmed_02': 97, 'radmed_03': 115, 'radmed_04': 130, 'radmed_05': 465,
                                                  'radmed_06': 585, 'radmed_07': 660, 'radmed_08': 526, 'radmed_09': 290, 'radmed_10': 77,
                                                  's2_01': 102, 's2_02': 120, 's2_03': 633, 's2_04': 828, 's2_05': 951, 's2_06': 911,
                                                  's2_07': 720, 's2_08': 291, 's2_085': 130, 's2_t1_end': 100, 's2_09': 133, 's2_10': 495,
                                                  's2_11': 767, 's2_12': 846, 's2_13': 718, 's2_14': 360, 's2_15': 119, 's2_16': 105,
                                                  's2_17': 120, 's2_18': 438, 's2_19': 648, 's2_20': 877, 's2_21': 811, 's2_22': 340,
                                                  's2_23': 118}
                             }
    return canales_stations_info
    
def set_station_location_codes(station, total_profiles_attrs, stations_info_location):
    location_code = stations_info_location['station_location'][station]
    total_profiles_attrs[station]['location_code'] = location_code
    return total_profiles_attrs

def set_station_depth(station, total_profiles_attrs, stations_info_location):
    station_depth = stations_info_location['station_depth'][station]
    total_profiles_attrs[station]['station_depth'] = station_depth
    return total_profiles_attrs

def build_2d_grid(stations_to_plot, stations_range, total_profiles_data, total_profiles_attrs, varname_to_plot):
    # Creates a grid that contains depth and latitude values for all the stations. 
    # Latitudes are generic and taken from the attributes files. 
    # Depth dimension belongs to the maximum depth range registered among the profiles
    
    depth_length_list = []
    for i in range(0,stations_range):        
        depth_length_profile = len(total_profiles_data[stations_to_plot[i]]['depth']) #the longest profile i n the section
        depth_length_list.append(depth_length_profile)
        depth_size = np.max(depth_length_list)
        depth_length_list_idx = depth_length_list.index(max(depth_length_list))
        
    depth_max_section = np.empty((1,stations_range))  
    for i in range(0, stations_range):
        depth_max_section[0][i] = total_profiles_attrs[stations_to_plot[i]]['station_depth']
        
    grid_var = np.zeros((stations_range, depth_size))
    grid_depth = np.zeros((stations_range, depth_size))

    for i in range(0,stations_range):
        depth_length_profile = len(total_profiles_data[stations_to_plot[i]]['depth'])
        grid_var[i][0:depth_length_profile] = total_profiles_data[stations_to_plot[i]][varname_to_plot]

       
    grid_depth = total_profiles_data[stations_to_plot[depth_length_list_idx]]['depth']   
    grid_var[grid_var==0] = np.nan
    
    return grid_var, grid_depth, depth_max_section


def calculate_ptemp(salt, temp, pres):
    ptemp = gsw.pt_from_t(salt, temp, pres, 0)
    return ptemp

def calculate_dens_and_ptemp(salt, temp, pres):
    ptemp = gsw.pt_from_t(salt, temp, pres, 0)
        
    # Figure out boudaries (mins and maxs)
    smin = np.nanmin(salt) - (0.01 * np.nanmin(salt))
    smax = np.nanmax(salt) + (0.01 * np.nanmax(salt))
    tmin = np.nanmin(temp) - (0.1 * np.nanmin(temp))
    tmax = np.nanmax(temp)
    # Figure out boudaries (mins and maxs)       
#    smin = 37.2
#    smax = 38.8
#    tmin = 12
#    tmax = 20 

    # Calculate how many gridcells we need in the x and y dimensions
    xdim = int(round((smax-smin)/0.1+1,0))
    ydim = int(round((tmax-tmin)+1,0))
    
     
    # Create empty grid of zeros
    dens = np.zeros((ydim,xdim))
     
    # Create temp and salt vectors of appropiate dimensions
    ti = np.linspace(1,ydim-1,ydim)+tmin
    si = np.linspace(1,xdim-1,xdim)*0.1+smin
    
    # Loop to fill in grid with densities
    for j in range(0,int(ydim)):
        for i in range(0, int(xdim)):
            dens[j,i]=gsw_sw.dens(si[i],ti[j],0)
     
    #Substract 1000 to convert to sigma-t
    dens = dens - 1000
    
    return dens, ptemp, si, ti, smin, smax, tmin, tmax
    
    
def save_figure(fig, out_path, deployment_name, figure_name):
    if os.path.isdir(out_path) == False:
        os.mkdir(out_path)
    
    plt.savefig(out_path + figure_name, 
                bbox_inches='tight', format='png',  dpi=800)

        