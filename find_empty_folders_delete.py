'''
PYTHON CODE TO AUTOMATICALLY DELETE THE EMPTY FILES IN A FOLDER
'''

#import necessary packages
import os

path="path/"
for file in os.listdir(path):
    with open(os.path.join(path,file), "r") as f:
        lines = f.readlines()
        #condition which checks the size of the text file
        if len(lines) == 0:
            print(file) #prints the deleted files
            os.remove(os.path.join(path,file)) #deletes the empty text files
                    

                    