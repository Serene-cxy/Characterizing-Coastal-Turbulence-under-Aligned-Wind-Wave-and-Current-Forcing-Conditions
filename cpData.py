#!/usr/bin/env python3

"""
Program: cpData
cp data of dynamic regime to my direcotry.
"""

### Histories:
### 2024/09/29 -- Bicheng Chen (bchen@xmu.edu.cn) -- First created



## Prerequisite Module
import os
import shutil



## User-specified Variable
# File
path_in = "/share/home/jzh184/Case/Current_diurnal_hf_heating2/LSCformation"
dirpre_in = "Lat"
fnpre_in = ("oneOrder", "twoOrder", "threeOrder")
fnpost_in = "jld2"
path_out = "./data"



### Main Body
## Find the data path
subdList = []
for subdir in os.listdir(path_in):
  if subdir.startswith(dirpre_in):
    subdList.append(subdir)

## Copy data to the destination
for subdir in subdList:
  # Find source directory and destination directory
  dir_in = os.path.join(path_in, subdir)
  subdir_out = subdir.replace("theta", "X").replace("NaN","Inf")
  dir_out = os.path.join(path_out, subdir_out)

  # Create destination directory if necessary
  if not os.path.exists(dir_out):
    os.makedirs(dir_out)

  for base_in in os.listdir(dir_in):
    # Seek data file with desired name
    if base_in.startswith(fnpre_in) and base_in.endswith(fnpost_in):
      # Modify file name
      if base_in.startswith("one"):
        base_out = base_in.replace("one", "1st")
      elif base_in.startswith("two"):
        base_out = base_in.replace("two", "2nd")
      elif base_in.startswith("three"):
        base_out = base_in.replace("three", "3rd")
      else:
        base_out = base_in

      # Copy file
      fn_in = os.path.join(dir_in, base_in)
      fn_out = os.path.join(dir_out, base_out)

      print("Copying {:s} to {:s}...".format(fn_in, fn_out))
      shutil.copy(fn_in, fn_out)
