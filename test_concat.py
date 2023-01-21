import unittest
from concat_csvs import concat_csvs

class test_concat_csv(unittest.TestCase):

  complete_csv = concat_csvs()

  def setUp(self):
    self.maxDiff = None

  def test_csv_appropriate_length(self):
    length = len(self.complete_csv)
    self.assertGreater(length, 1, "Resulting csv length should be > 1")

  def test_correct_files(self):
    correct_files = ["msd_NT_slice_1_cortex_vid_6.csv",
                     "msd_NT_slice_1_cortex_vid_7.csv",
                     "msd_NT_slice_1_cortex_vid_8.csv",
                     "msd_NT_slice_1_cortex_vid_9.csv",
                     "msd_NT_slice_1_cortex_vid_10.csv",
                     "msd_NT_slice_1_ganglia_vid_1.csv",
                     "msd_NT_slice_1_ganglia_vid_2.csv",
                     "msd_NT_slice_1_ganglia_vid_3.csv",
                     "msd_NT_slice_1_hippocampus_vid_1.csv",
                     "msd_NT_slice_1_hippocampus_vid_2.csv",
                     "msd_NT_slice_1_hippocampus_vid_3.csv",
                     "msd_NT_slice_1_striatum_vid_1.csv",
                     "msd_NT_slice_1_striatum_vid_2.csv",
                     "msd_NT_slice_1_striatum_vid_3.csv",
                     "msd_NT_slice_1_striatum_vid_4.csv",
                     "msd_NT_slice_1_striatum_vid_5.csv",
                     "msd_NT_slice_1_thalamus_vid_1.csv",
                     "msd_NT_slice_1_thalamus_vid_2.csv",
                     "msd_NT_slice_1_thalamus_vid_3.csv",
                     "msd_NT_slice_2_cortex_vid_1.csv",
                     "msd_NT_slice_2_cortex_vid_2.csv",
                     "msd_NT_slice_2_cortex_vid_3.csv",
                     "msd_NT_slice_2_cortex_vid_4.csv",
                     "msd_NT_slice_2_cortex_vid_5.csv",
                     "msd_NT_slice_2_ganglia_vid_1.csv",
                     "msd_NT_slice_2_ganglia_vid_2.csv",
                     "msd_NT_slice_2_ganglia_vid_3.csv",
                     "msd_NT_slice_2_hippocampus_vid_1.csv",
                     "msd_NT_slice_2_hippocampus_vid_2.csv",
                     "msd_NT_slice_2_hippocampus_vid_3.csv",
                     "msd_NT_slice_2_striatum_vid_1.csv",
                     "msd_NT_slice_2_striatum_vid_2.csv",
                     "msd_NT_slice_2_striatum_vid_3.csv",
                     "msd_NT_slice_2_striatum_vid_4.csv",
                     "msd_NT_slice_2_striatum_vid_5.csv",
                     "msd_NT_slice_2_thalamus_vid_1.csv",
                     "msd_NT_slice_2_thalamus_vid_2.csv",
                     "msd_NT_slice_2_thalamus_vid_3.csv"]
    filenames_without_path = []
    start_index = len(concat_csvs.FOLDER_NAME) + 1
    for f in self.complete_csv.files:
      filenames_without_path.append(f[start_index:])
    self.assertListEqual(filenames_without_path, correct_files,
                         "Doesn't contain the correct files")

  def test_correct_columns(self):
    correct_columns = ["Frame", "Gauss", "MSDs", "Mean_Intensity",
                      "Quality", "SN_Ratio", "Track_ID", "X", "Y",
                      "file_name", "timestep_id", "particle_id"]
    columns = concat_csvs.get_columns(self.complete_csv)
    self.assertListEqual(correct_columns, columns, "Columns are not equal")

  def test_consistent_dfs(self):
    other_csv = concat_csvs()
    self.assertEqual(self.complete_csv, other_csv, "Data order is inconsistent")

if __name__ == "__main__":
  unittest.main()
