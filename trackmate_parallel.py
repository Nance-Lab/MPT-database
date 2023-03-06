import multiprocessing as mp
import time
import scyjava
import imagej
import sys

def process_videos_parallel(fn):
  # a) folder with 20 videos - process four at a time
  # b) thread have diff val of parameter (diff parameter set)
  
  ij = imagej.init()
  language_extension = 'ijm'
  result_script = ij.py.run_script(language_extension, macro, args)
  return


def run_trackmate_parallel(path, fn, argmts, num_threads=mp.cpu_count()):
  '''
  Enables parallel processing of multiple tif files by Trackmate.

  Inputs:
  path (str): The path to the images to be processed
  fn (str): The name of the Trackmate script/function to use
  argmts (tuple): The arguments the Trackmate function takes
  num_threads (int): The number of threads/cores to use (default: max cores available)
                      If the threads entered exceeds the number available, the max number
                      of threads available will be used
  
  Outputs:
  Tracking results from each tif file (i.e. a Tuple of csv files,
    where each element of the Tuple is the tracking data csv from a video.
  '''
  threads_avail = mp.cpu_count()
  if num_threads > threads_avail:
    print(f"Provided number of threads exceeds the number available. \
          Using max number available ({threads_avail}) instead.")
    num_threads = threads_avail

  pool = mp.Pool(num_threads)
  # start_time = time.perf_counter()
  pool.apply(process_videos_parallel, args=argmts)
  # pool.map(fn, range())
  # finish_time = time.perf_counter()
  # print(f"Program finished in {finish_time-start_time} seconds.")
  pool.close()

