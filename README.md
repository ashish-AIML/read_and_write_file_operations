# Read, Write, Delete and Append Operations in Text Files : Automation of I/O Operations in Text Files

This is summary readme for I/O operations in Text Files and brief description of the python codes

---
## Delete Empty Text Files
Run [find_empty_folders_delete](find_empty_folders_delete.py) to delete all empty bulk text files in a folder at once 

***

---
## Keep Wanted Lines and Delete the Unwanted
Run [keep_specific_classes_and_delete_other](keep_specific_classes_and_delete_other.py) to keep specific classes in text files and delete the rest classes. This code is designed in YOLO use case. It can applied to any I/O operations. 

For example: To keep lines with/without specific text and delete the rest lines:

```
with open("file.txt","r+") as f:
    new_f = f.readlines()
    f.seek(0)
    for line in new_f:
        if "specific_word" not in line:
            f.write(line)
    f.truncate()
```

***

---
## Replace Index Values with Specific Values/Text in Text Files
Run [replace_index_with_zero](replace_index_with_zero.py) to replace specific index values in a folder at once. This can be even tweaked to replace specific word with another word.

For example:
```
with open('file.txt', 'r') as file :
  filedata = file.read()
filedata = filedata.replace('word1', 'word2')
with open('file.txt', 'w') as file:
  file.write(filedata)
``` 

## Limitation:
The only limitation for [replace_index_with_zero](replace_index_with_zero.py) this code is, it doesn't overwrite the edited text. For time being, you can run [keep_specific_classes_and_delete_other](keep_specific_classes_and_delete_other.py) with previous class names, after editing [replace_index_with_zero](replace_index_with_zero.py)

***

---
## Create Text Files with Same Image File name and Append Same Data
1. Run [same_text_in_all_image_files](same_text_in_all_image_files.py) to create all text files with respect to all image files present in the folder. This is automating the annotation process in YOLO format with similar locations in the images. 
2. First, annotate one image and create its text file. Copy the coordinates in it and past in [same_text_in_all_image_files](same_text_in_all_image_files.py) and give the folder where all images are located. 

***

---
## License & Copyright

@ Teric-AI Team

***
