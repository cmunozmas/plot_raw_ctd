# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 09:15:09 2018

@author: socib
"""
import utils.globfile as globfile

import os

def set_deployment_info(deployment_name, cruise_name):
    tmp = deployment_name.split('_')
    tmp_date = tmp[3].split('-')
    deployment_info = {'deployment_code': tmp[0], 
                       'platform_name': tmp[1], 
                       'instrument_name': tmp[2], 
                       'deployment_date': tmp[3],
                       'deployment_year': tmp_date[0],
                       'deployment_name': deployment_name,
                       'cruise_name': cruise_name}
    return deployment_info
    
def import_paths(deployment_info, deployment_name):
#    main_code_path = 'C:/Users/socib/Documents/python/plot_raw_ctd/'
#    input_data_repository_path = 'C:/Users/socib/Documents/data/vessel_CTD_data/'
    main_code_path = '/home/cmunoz/Documents/programming/PythonScripts/plot_raw_ctd/'
    input_data_repository_path = '/home/vessel/RTDATA/'
    input_data_path = [input_data_repository_path + 
                        deployment_info['platform_name'].replace("-", "_") + '/' +
                        deployment_info['instrument_name'].upper() + '/' +
                        'rawArchive/'+ 
                        deployment_info['deployment_year'] + '/' +
                        deployment_info['deployment_code'] + '_' +
                        deployment_info['platform_name'] + '_' +
                        deployment_info['instrument_name'] + '_' +
                        deployment_info['deployment_date'] + '/' +
                        'PROCESSED_SOCIB_halfm/']
    
    #output_figs_main_path = 'C:/Users/socib/Documents/test_figures_ctd/'
    output_figs_main_path = '/LOCALDATA/canales_plots/dataCTD/FIGURES/' 
    output_figs_path = output_figs_main_path + deployment_name + '/'  
    stations_info_path = main_code_path + 'res/'
    
    
    globfile.paths = {'main_code_path': main_code_path, 
             'input_data_path': input_data_path[0], 
             'output_figs_path': output_figs_path,
             'stations_info_path': stations_info_path}    
    return globfile.paths

def list_datasets(path_to_files):
    filenames_list = os.listdir(path_to_files)
    return filenames_list

def filter_filenames_list(filenames_list):
    filenames_list = filter(lambda x: x[0] == 'd', filenames_list)
    return filenames_list