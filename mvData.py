#!/usr/bin/env python3

"""
"""


## Prerequisite Module
import os
import shutil



## User-specified Variable
# File
path_in = "./"
dirpre_in = "Lat"
path_out = "./"



### Main Body
## Find the data path
subdList = []
for subdir in os.listdir(path_in):
  if subdir.startswith(dirpre_in):
    subdList.append(subdir)

## Copy data to the destination
#for subdir in subdList:
  #dir_in = os.path.join(path_in, subdir)

  #if "kH2'5" in subdir:
  #  subdir_out = subdir.replace("kH2'5", "kH5|2")
  #elif "kH5" in subdir:
  #  subdir_out = subdir.replace("kH5", "kH5|1")
  #elif "kH10" in subdir:
  #  subdir_out = subdir.replace("kH10", "kH10|1")

  #dir_out = os.path.join(path_out, subdir_out)

  #shutil.move(dir_in, dir_out)

bn_in = '1stOrder_tau_A2.jld2'
bn_out = '2ndOrder_tau_A2.jld2'

for subdir in subdList:
  fn_in = os.path.join(path_in, subdir, bn_in)
  if os.path.exists(fn_in):
    fn_out = os.path.join(path_out, subdir, bn_out)
    shutil.move(fn_in, fn_out)
