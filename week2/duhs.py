import os
import sys

sum=0
path1=os.getcwd()
print(path1)
for item in os.scandir(path1):
    if item.is_file():
        sum+=os.path.getsize(item)
print(str(round(sum*(10**-9),3))+' GB')