#import necessary packages
import glob, os

os.chdir("dir") #the directory containing your .jpegs
for file in glob.glob("*.jpg"): #iterates over all files in the directory ending in .jpg        
    f = open(( file.rsplit( ".", 1 )[ 0 ] ) + ".txt", "w") #creates a new file using the .jpg filename, but with the .txt extension
    f.write('whatever you want in the text file') #write to the text file
    f.close()