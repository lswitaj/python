#! /usr/bin/python3
# walk.py - files and paths

import os

print('current path before walk ' + os.getcwd() + '\n')


for folderName, subFolders, fileNames in os.walk('./'):
    print('the current folder is ' + folderName)

    for subFolder in subFolders:
        print('Subfolder of ' + folderName + ': ' + subFolder)
    for fileName in fileNames:
        print('File inside ' + folderName + ': ' + fileName)

    print('')