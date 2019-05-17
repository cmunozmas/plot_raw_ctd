# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 09:15:13 2018

@author: cristian munoz mas
"""
import utils.SetPaths as SetPaths
import utils.DataOps as DataOps
import utils.Plot as Plot
import utils.globfile as globfile
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

import numpy as np

# settings
deployment_name = 'dep0014_socib-rv_scb-sbe9001_2019-05-07'
cruise_name = 'SOCIB Canales Spring 2019'



#import path to data
deployment_info =   SetPaths.set_deployment_info(deployment_name, cruise_name)
paths =             SetPaths.import_paths(deployment_info, deployment_name)
filenames_list =    SetPaths.list_datasets(paths['input_data_path'])
filenames_list =    SetPaths.filter_filenames_list(filenames_list)

#obtain list of stations names
station_names_list = DataOps.get_station_names(filenames_list)
stations_info_location = DataOps.load_generic_stations_info()


#read datasets and put them in dictionaries
total_profiles_data = dict.fromkeys(station_names_list, [])
total_profiles_attrs = dict.fromkeys(station_names_list, [])


    
    
for i in range(0,len(filenames_list)):
    #load single profile 
    profile = DataOps.read_input_files(paths['input_data_path'], filenames_list[i])
    single_profile_attrs = profile.attributes
    if i == 0:
       var_names = profile.keys()
    single_profile_data = DataOps.load_profile_data(profile, var_names, deployment_info)
#    # identify null values
#    null_value = -9.990e-29
#    for j in range(0,len(single_profile_data)):
#        profile_var = single_profile_data.values()[j]
#        for k in range(0,len(profile_var)):
#            if profile_var[k] == null_value:
#                profile_var[k] = np.NaN
        
    
    #allocate data from single profile   
    total_profiles_data[station_names_list[i]] = single_profile_data    
    total_profiles_attrs[station_names_list[i]] = single_profile_attrs 

# add potential temperature to each of the profiles
for i in range(0,len(total_profiles_data)):
    salt1 = total_profiles_data.values()[i]['psal1']
    temp1 = total_profiles_data.values()[i]['temp1']
    pres = total_profiles_data.values()[i]['pres']
    total_profiles_data.values()[i]['ptemp1'] = DataOps.calculate_ptemp(salt1, temp1, pres)
    
#assign location code and depth to profiles attributes
for i in range(0,len(total_profiles_data)):
    station = total_profiles_data.keys()[i]
    total_profiles_attrs = DataOps.set_station_location_codes(station, total_profiles_attrs, stations_info_location)
    total_profiles_attrs = DataOps.set_station_depth(station, total_profiles_attrs, stations_info_location)    

#plot figures
vars_to_plot = total_profiles_data[total_profiles_data.keys()[0]].keys()
vars_to_plot.remove('longitude')
vars_to_plot.remove('latitude')
vars_to_plot.remove('depth')
vars_to_plot.remove('pres')
vars_to_plot.append('ptemp1')

vars_to_plot_ts = ['temp1', 'psal1', 'temp2', 'psal2', 'pres']
location_code = stations_info_location['location_code']


for i in range(0, len(location_code)):
    stations_to_plot = [] #group profiles according to location
    for j in range(0, len(total_profiles_data)):
        station = total_profiles_attrs.keys()[j]
        section_code = stations_info_location['location_code'][i]
        if total_profiles_attrs[station]['location_code'] == section_code:
            stations_to_plot.append(station)
            
    stations_to_plot = sorted(stations_to_plot, key=str.lower) 
    
    if len(stations_to_plot) != 0:   # it will plot profiles only in case there is any profile per section    
        stations_range = len(stations_to_plot)
        lon = np.arange(stations_range, dtype=float)
        
        for n in range(0, stations_range):
            lon[n] = total_profiles_attrs[stations_to_plot[n]]['LONGITUDE']
            
        # contour plots for each variable to plot
        for k in range(0,len(vars_to_plot)):
            varname_to_plot = vars_to_plot[k]
            #build 2D grid with longitudes and depths
            grid_var, grid_depth, depth_max_section = DataOps.build_2d_grid(stations_to_plot, stations_range, total_profiles_data, total_profiles_attrs, varname_to_plot)                     
            Plot.plot_var(location_code[i], varname_to_plot, stations_to_plot, lon, grid_var, grid_depth, depth_max_section, deployment_info, 0)      
            Plot.plot_var(location_code[i], varname_to_plot, stations_to_plot, lon, grid_var, grid_depth, depth_max_section, deployment_info, 200) 
            
            
#%%    
        # TS diagrams for sensor 1 and sensor 2
        Plot.plot_ts(total_profiles_data, stations_to_plot, stations_range, lon, section_code, deployment_info)

            

            

        
