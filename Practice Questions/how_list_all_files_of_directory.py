from os import listdir
from os.path import isfile, join
import os

# Get the user's home directory dynamically
user_directory = os.path.expanduser("~")

# List all files in the user's home directory
files_list = [f for f in listdir(user_directory) if isfile(join(user_directory, f))]
print(files_list)

