'''
PYTHON CODE TO KEEP SPECIFIC CLASS NAMES (INDEX VALUES) IN TEXT FILE AND DELETE THE REST
'''

#import necessary packages
import os

path="path/"  #put all text files that are to be replaced in a folder. Example: all files with extension .txt
for file in os.listdir(path):
    with open(os.path.join(path,file), "r") as f:
        lines = f.readlines()
        with open(os.path.join(path,file), "w") as f:
            for line in lines:
                if line.startswith("0"): #custom condition where we need our desired index and text 
                    f.write(line) #keeps the text we want and deletes the rest
    
