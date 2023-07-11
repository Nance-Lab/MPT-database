import pandas as pd
import glob as gb
import numpy as np
from natsort import natsorted
import re
import os
import dask.dataframe as dd
import dask.array as da
import time
import csv
import dask.delayed
import pandas as pd

class concat_csvs:
  '''
  Prompts user for CSV files (.csv) with results from multiple particle
  tracking (MPT) experiments, appends them them all together (by file name,
  alphabetically ascending), and then saves the combined CSV in the current
  directory.
  '''

  PARTICLE_ID_STEP = 651 # timesteps per particle

  def __init__(self):
    prompt = "Enter the name of the folder that contains the data: "
    # TODO: check dir is valid
    self.folder_name = validate_input(prompt)
    path_to_folder = os.path.join(os.getcwd(), self.folder_name)

    while not os.path.exists(path_to_folder):
      print(f"'{self.folder_name}' does not exist in the current directory")
      self.folder_name = validate_input(prompt)
      path_to_folder = os.path.join(os.getcwd(), self.folder_name)

    print("Concatenanting the following CSVs:")
    self.files = gb.glob(self.folder_name + "/*.csv")
    self.files = natsorted(self.files)

    timestep_id_count = 0
    particle_id_count = 0

    df_list = []  # append all DataFrames into one list
    count = 2

    for f in self.files:
      if count == 0:
        break

      filename = f[len(self.folder_name)+1:]
      print(f"\t{filename}")

      cur_df = dd.read_csv(f)
      cur_df = cur_df.drop('Unnamed: 0', axis=1)
      length = len(cur_df)

      ids = pd.DataFrame({'timestep_id': list(range(timestep_id_count, timestep_id_count + length))})
      ids = dd.from_pandas(ids, npartitions=1)
      ids = ids.set_index('timestep_id')
      
      cur_df = cur_df.merge(ids, right_on='timestep_id', left_index=True)
      cur_df = cur_df.assign(file_name=filename, particle_id=particle_id_count)
      df_list.append(cur_df)
      
      print("timestep id: ", timestep_id_count)
      print("particle id count: ", particle_id_count)
      timestep_id_count = timestep_id_count + length
      particle_id_count = particle_id_count + self.PARTICLE_ID_STEP
      count = count - 1

    self.full_csv = dd.concat(df_list)

  def __len__(self):
    '''Returns the length of the fully-concatenated CSV.'''
    return len(self.full_csv)

  def __eq__(self, other):
    '''
    Returns true if two fully-concatenated CSVs (as DataFrames) are equal, false otherwise.

    Parameters:
    ----------
    other: dask DataFrame
        The other DataFrame to compare this DataFrame to
    '''
    self_pd_df = self.full_csv.compute()
    other_pd_df = other.full_csv.compute()
    return self_pd_df.equals(other_pd_df)

  def get_columns(self):
    '''Returns all the columns (as a list) of the fully-concatenated CSV.'''
    return self.full_csv.columns.tolist()

  def get_data_folder(self):
    '''Returns the name of the folder containing the CSV files.'''
    return self.folder_name

  def get_as_csv(self, full_csv_name):
    '''
    Returns the fully-concatenated CSV in .csv form with the given name.

    Parameters:
    ----------
    full_csv_name: str
        The name of the fully-concatenated CSV
    '''
    path = os.path.join("./", full_csv_name)
    return self.full_csv.to_csv(filename=path, single_file=True)

  def get_tail(self, n):
    '''
    Returns the last n entries of the fully-concatenated CSV.
    '''
    return self.full_csv.loc[-5:].compute()

def validate_input(prompt):
  '''
  Continues to prompt the user for a name (of a file/directory) until a valid
  name has been given.

  Returns:
  ----------
  A valid name the user has entered.
  '''
  name = input(prompt)
  regex = r"^([a-zA-Z0-9][^*/><?\|:]*)$"
  valid_name = bool(re.search(regex, name))
  while not valid_name:
    print("Invalid name. Try again.")
    name = input(prompt)
    valid_name = bool(re.search(regex, name))
  return name

def main():
  start_time = time.perf_counter()
  full_csv = concat_csvs()
  end_time = time.perf_counter()
  print(f"Full CSV created (length: {len(full_csv)})")
  print(f"Elapsed time: {end_time-start_time}s\n")

  prompt = "Enter the name for the CSV to be saved as: "
  csv_name = validate_input(prompt)
  full_csv_name = csv_name + ".csv"

  try:
    print(f"Saving {full_csv_name} under the current directory...")
    start_time = time.perf_counter()
    full_csv.get_as_csv(full_csv_name)
    end_time = time.perf_counter()
    print(f"Elapsed time: {end_time-start_time}s")
    print(full_csv.get_tail(5))
  except TypeError:
      pass
  
  print(f"Success! '{full_csv_name}' was created under the current directory.")

if __name__ == "__main__":
  main()
