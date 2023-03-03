import os
import shutil
from_dir, to_dir = "C:/Users/seane/Downloads", "C:/Users/seane/OneDrive/Desktop/Document_Files"
list_of_files = os.listdir(from_dir)

for i in list_of_files:
    name, ext = os.path.splitext(i)
    print(name, ext)