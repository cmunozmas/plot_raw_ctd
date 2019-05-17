# -*- coding: utf-8 -*-
"""
Created on Wed Sep 05 22:38:29 2018

@author: socib
"""
def set_var_to_plot_long_name(varname_to_plot):
    if varname_to_plot == 'cond1':
        varname_to_plot_long = 'sea water conductivity sensor 1'
    elif varname_to_plot == 'cond2':
        varname_to_plot_long = 'sea water conductivity sensor 2'
    elif varname_to_plot == 'psal1':
        varname_to_plot_long = 'sea water salinity sensor 1'
    elif varname_to_plot == 'psal2':
        varname_to_plot_long = 'sea water salinity sensor 2'
    elif varname_to_plot == 'temp1':
        varname_to_plot_long = 'sea water temperature sensor 1'
    elif varname_to_plot == 'temp2':
        varname_to_plot_long = 'sea water temperature sensor 2'
    elif varname_to_plot == 'dens1':
        varname_to_plot_long = 'sea water density sensor 1'
    elif varname_to_plot == 'dens2':
        varname_to_plot_long = 'sea water density sensor 2'
    elif varname_to_plot == 'turb':
        varname_to_plot_long = 'sea water turbidity'
    elif varname_to_plot == 'fluo':
        varname_to_plot_long = 'sea water fluorescence'
    elif varname_to_plot == 'dox':
        varname_to_plot_long = 'sea water dissolved oxygen'
    elif varname_to_plot == 'ptemp1':
        varname_to_plot_long = 'sea water potential temperature sensor 1'
    elif varname_to_plot == 'ptemp2':
        varname_to_plot_long = 'sea water potential temperature sensor 2'
        
    return varname_to_plot_long
        
        
def set_var_to_plot_units(varname_to_plot):
    if varname_to_plot == 'cond1':
        varname_to_plot_units = 'Conductivity [mS/cm]'
    elif varname_to_plot == 'cond2':
        varname_to_plot_units = 'Conductivity [mS/cm]'
    elif varname_to_plot == 'psal1':
        varname_to_plot_units = 'Salinity, Practical [PSU]'
    elif varname_to_plot == 'psal2':
        varname_to_plot_units = 'Salinity, Practical [PSU]'
    elif varname_to_plot == 'temp1':
        varname_to_plot_units = 'sea water temperature sensor 1 [deg C]'
    elif varname_to_plot == 'temp2':
        varname_to_plot_units = 'sea water temperature sensor 2 [deg C]'
    elif varname_to_plot == 'dens1':
        varname_to_plot_units = 'Density [density, kg/m^3]'
    elif varname_to_plot == 'dens2':
        varname_to_plot_units = 'Density [density, kg/m^3]'
    elif varname_to_plot == 'turb':
        varname_to_plot_units = 'Turbidity, Seapoint [FTU]'
    elif varname_to_plot == 'fluo':
        varname_to_plot_units = 'Fluorescence, Seapoint [Volt]'
    elif varname_to_plot == 'dox':
        varname_to_plot_units = 'Oxygen, SBE 43 [mg/l]'  
    elif varname_to_plot == 'ptemp1':
        varname_to_plot_units = 'sea water potential temperature sensor 1 [deg C]'
    elif varname_to_plot == 'ptemp2':
        varname_to_plot_units = 'sea water potential temperature sensor 2 [deg C]'
        
    return varname_to_plot_units

def set_location_long_name(location_code):
    if location_code == 'MC':
        location_long_name = 'Mallorca Channel'
    elif location_code == 'ICS':
        location_long_name = 'Ibiza Channel South'
    elif location_code == 'ICM':
        location_long_name = 'Ibiza Channel Middle'
    elif location_code == 'ICN':
        location_long_name = 'Ibiza Channel North'
        
    return location_long_name
    
