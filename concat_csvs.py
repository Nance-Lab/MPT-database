import pandas as pd
import glob as gb
import numpy as np
from natsort import natsorted

class concat_csvs:

  FOLDER_NAME = "raw_data_region"

  def __init__(self):
    self.files = gb.glob(self.FOLDER_NAME + "/*.csv")
    self.files = natsorted(self.files)
    timestep_id_count = 0
    df_list = [] # append all DataFrames into one list
    for f in self.files:
      csv = pd.read_csv(f, index_col=[0])
      csv["file_name"] = f
      df_list.append(csv)
      timestep_id_count = timestep_id_count + len(csv)
    df = pd.concat(df_list, ignore_index=True)
    df["timestep_id"] = np.arange(timestep_id_count)
    df["particle_id"] = 0
    self.full_csv = df

  def __len__(self):
    return len(self.full_csv)

  def __eq__(self, other):
    return pd.DataFrame.equals(self.full_csv, other.full_csv)

  def get_columns(self):
    return list(self.full_csv.columns.values)
