# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 13:33:33 2018

@author: cmunoz
"""

def import_profile_data(profile, var_names, deployment_info):
    if deployment_info['instrument_name'] == 'scb-sbe9002': 
        profile_data = {'latitude': profile[var_names[0]],
                        'longitude': profile[var_names[1]],
                        'depth': profile[var_names[22]],
                        'pres': profile[var_names[3]],
                        'temp1': profile[var_names[4]],
                        'temp2': profile[var_names[5]],
                        'cond1': profile[var_names[7]],
                        'cond2': profile[var_names[8]],
                        'psal1': profile[var_names[23]],
                        'psal2': profile[var_names[24]],
                        'dens1': profile[var_names[26]],
                        'dens2': profile[var_names[28]],
                        'turb': profile[var_names[21]],
                        'fluo': profile[var_names[20]],
                        'dox': profile[var_names[16]]
                        }
                        
#    elif deployment_info['instrument_name'] == 'scb-sbe9001': 
#        profile_data = {'latitude': profile[var_names[0]],
#                        'longitude': profile[var_names[1]],
#                        'depth': profile[var_names[12]],
#                        'pres': profile[var_names[3]],
#                        'temp1': profile[var_names[4]],                        
#                        'cond1': profile[var_names[5]],                        
#                        'psal1': profile[var_names[13]],
#                        'dens1': profile[var_names[14]],
#                        'turb': profile[var_names[11]],
#                        'fluo': profile[var_names[10]],
#                        'dox': profile[var_names[8]]
#                        }
    elif deployment_info['instrument_name'] == 'scb-sbe9001': 
        profile_data = {'latitude': profile[var_names[0]],
                        'longitude': profile[var_names[1]],
                        'depth': profile[var_names[23]],
                        'pres': profile[var_names[3]],
                        'temp1': profile[var_names[4]],
                        'temp2': profile[var_names[5]],
                        'cond1': profile[var_names[7]],
                        'cond2': profile[var_names[8]],
                        'psal1': profile[var_names[24]],
                        'psal2': profile[var_names[25]],
                        'dens1': profile[var_names[27]],
                        'dens2': profile[var_names[29]],
                        'turb': profile[var_names[21]],
                        'fluo': profile[var_names[20]],
                        'dox': profile[var_names[16]]
                        }                     
                        
    return profile_data