import pandas as pd
import glob as gb
import numpy as np
from natsort import natsorted
import re
import os
import csv
import dask.dataframe as dd
import dask.array as da

class concat_csvs:
  '''
  Prompts user for CSV files (.csv) with results from multiple particle
  tracking (MPT) experiments, appends them them all together (by file name,
  alphabetically ascending), and then saves the combined CSV in the current
  directory.
  '''

  PARTICLE_ID_STEP = 651 # timesteps per particle

  def __init__(self):
    folder_name_request = "Enter the name of the " \
                           "folder that contains the data: "
    self.folder_name = input(folder_name_request)
    # check to see if name entered is valid
    self.folder_name = validate_input(self.folder_name, folder_name_request)

    print("Concatenanting the CSVs:")
    self.files = gb.glob(self.folder_name + "/*.csv")
    self.files = natsorted(self.files)

    timestep_id_count = 0
    particle_id_count = 0
    df_list = []  # append all DataFrames into one list

    for f in self.files:
      print(f"\t{f}")
      curr_csv = dd.read_csv(f, blocksize="100MB")
      curr_csv["file_name"] = f
      curr_csv["particle_id"] = particle_id_count
      df_list.append(curr_csv)
      timestep_id_count = timestep_id_count + len(curr_csv)
      particle_id_count = particle_id_count + self.PARTICLE_ID_STEP

    df = dd.concat(df_list, ignore_index=True)
    df["timestep_id"] = da.from_array(np.arange(timestep_id_count))
    self.full_csv = df

  def __len__(self):
    '''Returns the length of the combined CSV.'''
    return len(self.full_csv)

  def __eq__(self, other):
    '''
    Returns true if two CSVs are equal, false otherwise.

    Parameters:
    ----------
    other: pandas DataFrame
        Another DataFrame to compare this CSV as a DataFrame to
    '''
    return pd.DataFrame.equals(self.full_csv, other.full_csv)

  def get_columns(self):
    '''Returns all the columns (as a list) of the combined CSV.'''
    return list(self.full_csv.columns.values)

  def get_folder_name(self):
    '''Returns the name of the folder that contains the individual CSV files.'''
    return self.folder_name

  def get_csv(self, full_csv_name):
    '''
    Returns the combined CSV in .csv form using a given name.

    Parameters:
    ----------
    full_csv_name: str
        The desired name of the complete (fully concatenated) CSV
    '''
    return self.full_csv.to_csv(os.path.join("./", full_csv_name), \
                                na_rep="None")

def validate_input(name, prompt):
  '''
  Continues to prompt the user for a name (of a file/directory) until a valid
  name has been given.

  Returns:
  ----------
  A valid name the user has entered.
  '''
  regex = r"^([a-zA-Z0-9][^*/><?\|:]*)$"
  valid_name = bool(re.search(regex, name))
  while not valid_name:
    print("Invalid name. Try again.")
    name = input(prompt)
    valid_name = bool(re.search(regex, name))
  return name

def main():
  full_csv = concat_csvs()
  print(f"CSV made (length: {len(full_csv)}).")
  csv_name_request = "Enter the name for the CSV to be saved as: "
  csv_name = input(csv_name_request)
  csv_name = validate_input(csv_name, csv_name_request)
  full_csv_name = csv_name + ".csv"

  with open("./" + full_csv_name, mode="w") as f:
    writer = csv.writer(f)
    try:
      writer.writerows(full_csv.get_csv(full_csv_name))
    except TypeError:
      pass

  print(f"Success! '{full_csv_name}' was created under the current directory.")

if __name__ == "__main__":
  main()
