import multiprocessing as mp
import re

def run_trackmate_parallel(path, script, num_threads=mp.cpu_count()):
    '''
    Enables parallel processing of multiple tif files by Trackmate.

    Inputs:
    path (str): The path to the images to be processed
    script (str): The name of the Trackmate script/function to use
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

    pool.close()

    # handle case where provided num_threads > max threads avail
    # folder with 20 vidoes
    # process four at a time
    # her feeding into thread
    # thread have diff val of parameter (diff parameter set)
    

