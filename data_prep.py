import pandas as pd
import numpy as np

from os import listdir, getcwd, chdir
from os.path import isfile, join

filepath = 'INSERT FILEPATH HERE'   # where data is stored
filelist = [f for f in listdir(filepath) if isfile(join(filepath, f))]      # list of csvs
# code to reorder files into correct order goes here (later) --> sort function, find reproducable order
filelist.sort()

new_col_list = ['Particle_ID', 'File_Name']

def add_columns(filepath, filelist, new_col_list, counter):
    
    """
    Adds new columns to list of tables, and vertically concatenates tables into single dataframe.
    
    Parameters
    ---------
    filepath: String
    
        file location where data is stored
        
    filelist: list (of strings)
    
        list of file names
        
    new_col_list: list (of strings)
    
        list of column names to be added
    
    counter: int
        
        current number of particles in the dataframe
        
    Returns
    ---------  
    full_df: Pandas DataFrame
        
        dataframe containing all vertically stacked input files,
        with new columns added
    """
    
    df_list = []                                              
    new_columns = pd.DataFrame(columns = new_col_list)        # dataframe containing only new columns/variables

    for i in range(len(filelist)):
        file = pd.read_csv(filepath + filelist[i])
        
        file_new = pd.concat([file, new_columns], axis = 1)
        file_new['File_Name'] = filelist[i]

        df_list.append(file_new)
        
    full_df = pd.DataFrame()                                  # full_df is the final stacked dataframe
    for i in range(len(df_list)):
        full_df = pd.concat([full_df, df_list[i]], ignore_index = True, axis = 0)    
        
    full_df['Particle_ID'] = np.arange(counter, counter+len(full_df), 1)
    
    return full_df
  
  
full_df_features = add_columns(filepath, filelist, new_col_list, 0)
