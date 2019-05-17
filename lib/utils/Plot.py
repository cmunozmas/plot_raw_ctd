# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 20:41:26 2018

@author: socib
"""
import utils.PlotSettings as PlotSettings
import utils.DataOps as DataOps
import utils.globfile as globfile

import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

import numpy as np
import gsw
import seawater as gsw_sw
from matplotlib.ticker import FormatStrFormatter



def plot_var(location_code, varname_to_plot, stations_to_plot, lat, grid_var, 
             grid_depth, depth_max_section, deployment_info, profile_depth_resolution): 
                 
    grid_var = np.ma.masked_where(np.isnan(grid_var),grid_var) # mask NaNs
    
    #fig = plt.figure()
    fig, ax = plt.subplots()
    cmap = plt.cm.get_cmap('jet', 100)
#    VMIN = np.nanmin(grid_var)
#    VMAX = np.nanmax(grid_var)
    font_size = 6
    
    grid_var = np.ma.array(grid_var, mask=grid_var == -9.990e-29)        
    CS = ax.contourf(lat, -grid_depth, grid_var.T, 10, cmap=cmap)
    ax.contour(CS, colors='k', linewidths=0.15)
    cbar = fig.colorbar(CS, format='%4.2f')
    cbar.ax.tick_params(labelsize= font_size) 
    #plt.xticks(lat, stations_to_plot, fontsize = 6, rotation = 90)
    plt.xticks(fontsize = font_size)
    plt.yticks(fontsize = font_size)
    varname_to_plot_long = PlotSettings.set_var_to_plot_long_name(varname_to_plot)
    location_long_name = PlotSettings.set_location_long_name(location_code)
    plt.title(deployment_info['cruise_name'] + ' - ' + varname_to_plot_long + '  -  ' + location_long_name, fontsize = font_size)
    plt.xlabel('Longitude (deg E)', fontsize = font_size)
    plt.ylabel('Depth (m)', fontsize = font_size)
    var_to_plot_units = PlotSettings.set_var_to_plot_units(varname_to_plot)
    cbar.set_label(var_to_plot_units, fontsize = font_size)
    ax2 = plt.plot(lat,-depth_max_section.T, 'r--', label='Nominal Depth')
    plt.legend(loc='lower right', fontsize = font_size)
    
    if profile_depth_resolution == 200:
        plt.ylim(ymin=-200, ymax=0)
 
    
    # save figure
    figure_name = location_code + '_' + varname_to_plot + '.png'
    if profile_depth_resolution == 200:
        figure_name = location_code + '_' + varname_to_plot + '_z200.png'
    DataOps.save_figure(fig, globfile.paths['output_figs_path'], 
                        deployment_info['deployment_name'], figure_name)
    plt.close()
    
    
#%%
def plot_ts(total_profiles_data, stations_to_plot, stations_range, lon, section_code, deployment_info): 
    
    pres = []
    temp = [] 
    psal = [] 
    dens = [] 
    ptemp = []
    station_idx = []
    
    fig1 = plt.figure(figsize=(7.87402, 6.29921))
    ax1 = fig1.add_subplot(111)
    
    font_size = 8
    
    for n in range(0, stations_range):   
        
        station = stations_to_plot[n]
        
        pres_station = total_profiles_data[station]['pres']
        temp_station = total_profiles_data[station]['temp1']
        psal_station = total_profiles_data[station]['psal1']
        
        RANGE = len(psal_station)
        station_idx_station = [lon[n]] * RANGE
        #pres.append(pres_station)
#            temp.append(temp_station)
#            psal.append(psal_station)   
        
        dens_station, ptemp_station, si, ti, smin, smax, tmin, tmax = DataOps.calculate_dens_and_ptemp(psal_station, temp_station, pres_station)             
#            dens.append(dens_station)
#            ptemp.append(ptemp_station)
        psal = np.concatenate((psal, psal_station), axis=0)
        ptemp = np.concatenate((ptemp, ptemp_station), axis=0)
        station_idx = np.concatenate((station_idx, station_idx_station), axis=0)
    
   


        if n == 0:
            levels = np.arange(dens_station.min(),dens_station.max(),0.1)
            CS = plt.contour(si,ti,dens_station, linewidths= 0.05,linestyle='--', colors='k', levels=levels)   
            plt.clabel(CS, fontsize=4, inline=1, inline_spacing=1, fmt='%1.1f') # Label every second level 
            
            ax1.grid(b=True, which='major', color='grey', linewidth=0.01)
            ax1.grid(b=True, which='minor', color='grey', linewidth=0.001)
            ax1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            ax1.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
            
            plt.xticks(np.arange(smin, smax, 0.1)) 
            plt.xticks(rotation=45)
            plt.yticks(np.arange(tmin+1, tmax, 0.25)) 
            plt.tick_params(axis='both', which='major', labelsize=6)
            location_long_name = PlotSettings.set_location_long_name(section_code)
            plt.title(deployment_info['cruise_name'] + ' - Theta-S' + '  -  ' + location_long_name, fontsize = font_size)        
            plt.xlabel('Salinity (PSU)', fontsize=font_size)
            plt.ylabel('Potential Temperature (deg C)', fontsize=font_size)

    plt.scatter(psal, ptemp, c=station_idx, s=20, edgecolor='black', linewidth='0.05')
    
    cbar = plt.colorbar()
    cbar.set_label('Longitude (deg E)', fontsize=font_size)
    cbar.ax.tick_params(labelsize= 6)
    # set axes range
    plt.xlim(37.7, 38.7)
    plt.ylim(12.8, 15.2)
    # save figure
    figure_name = section_code + '_theta-s_diag.png'
    DataOps.save_figure(fig1, globfile.paths['output_figs_path'], 
                        deployment_info['deployment_name'], figure_name)




    
    
