#
#Image to base64 converter
#
#version 1.0
#
#@author: Norbert Babineti
#

import base64
import os

#ask for the file path from the user. /home/test/example.jpeg
print("Please enter the full file path including filename and extension or you cand drag and drop the file in this terminal/cmd window and press enter:")
file_path = input().strip('"').rstrip()

#open the file and convert it to base64

with open(file_path, 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read())

#Write a file and save it as .txt
'''Get the original file name:
    Parse the path and get the original filename'''

full_file_name = os.path.basename(file_path)
print('Full file name is: ' + full_file_name)

#Separate the filename from the extension and retrieve the filename

file_name = full_file_name.split('.')[0]
print('File name is: ' + file_name)

pre_file_name = file_name + '.txt'
print('File name with extension: ' + pre_file_name)

new_file_name = os.path.join(os.path.dirname(file_path), pre_file_name)
print('New file name: ' + new_file_name)

if os.path.isfile(new_file_name) == False:  	
    new_file = os.open(new_file_name, os.O_RDWR|os.O_CREAT)
    print('File created')
    os.write(new_file, encoded_string)
    print('File written')
    os.close(new_file)	
else:
    print('File with the name ' + new_file_name + ' aleready exists in this folder: ' + os.path.dirname(file_path))
    exit()
