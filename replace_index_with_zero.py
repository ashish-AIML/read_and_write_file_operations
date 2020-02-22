'''
PYTHON CODE TO REPLACE INDEX VALUE IN BULK TEXT FILES AT ONCE
'''

#import necessary packages
import os

path="path/"  #put all text files that are to be replaced in a folder. Example: all files with extension .txt
for files in os.listdir(path):
    with open(os.path.join(path,files), 'r+') as file : #r+ is read+write operation
        filedata = file.readlines() #this function reads each line in the text files
        for index in filedata:
            replaced= index[0].replace(index[0], '0') #replace index value with our own value
            edit= replaced + index[1:] #paste the rest text after index value as it is
            file.write(edit) #write the repaced text in the same file
