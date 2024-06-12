
# Set the directory where the .tar.gz files are located
dest_dir_bg = 'D://Gait_Data//data_balance//bg'
path ="D://Gait_Data//GaitDatasetB-silh"

import os
import shutil
filelist = []
c=0
for root, dirs, files in os.walk(path):
  for file in files:
    if (file.find("bg")!=-1):
      #append the file name to the list
      filelist.append(os.path.join(root,file))
#print all the file names
for name in filelist:
    c=c+1
    print(name)
    shutil.copy(name,dest_dir_bg)
print(c)

dest_dir_nm = 'D://Gait_Data//data_balance//nm'
filelist1 = []
c1=0
for root, dirs, files in os.walk(path):
  for file in files:
    if (file.find("nm-05")!=-1) or (file.find("nm-06")!=-1):
      #append the file name to the list
      filelist1.append(os.path.join(root,file))

#print all the file names
for name in filelist1:
    c1=c1+1
    print(name)
    shutil.copy(name,dest_dir_nm)
print(c1)

dest_dir_cl = 'D://Gait_Data//data_balance//cl'
filelist2 = []
c2=0
for root, dirs, files in os.walk(path):
  for file in files:
    if (file.find("cl")!=-1):
      #append the file name to the list
      filelist2.append(os.path.join(root,file))

#print all the file names
for name in filelist2:
    c2=c2+1
    print(name)
    shutil.copy(name,dest_dir_cl)
print(c2)