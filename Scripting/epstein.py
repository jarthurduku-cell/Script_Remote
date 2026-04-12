import re
import os
from pathlib import Path
from zipfile import ZipFile

def count_mentions(celebrity_name):
    print(celebrity_name)
    print(os.getcwd())
    print(Path.cwd())
    os.mkdir("epstein")

    for subfolder in os.listdir():
        print(subfolder)

    with ZipFile("epstein_files.zip", "r") as unzipped:
         unzipped.extractall("epstein")

    workDir = str(os.getcwd()) + "\\epstein"
    
    for folderName, subfolders, filenames in os.walk(Path.cwd()):
        print(f"current folder: {folderName}")
    
        for sub in subfolders:
            print(f"SUBFOLDER in {folderName}: {sub}")
            for file in filenames:
                print(f"FILE INSIDE {folderName}: {file}")
            
count_mentions("Mick Jagger")
    
    
    
    



   

def top_words(celebrity_name, n=10):
    print(celebrity_name)
    print(n)
