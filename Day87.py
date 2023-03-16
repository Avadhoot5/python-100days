# Shutil Module

import shutil

# methods 

shutil.copy("src", "dest") # copies the file from src to dest.
shutil.copy2("src", "dest") # also preserves the metadata about the original file
shutil.copytree("src", "dest") # copies the directory 
shutil.move("src", "dest") # moves the file to a new location
shutil.rmtree("src", "dest") # deletes the directory located at path.


