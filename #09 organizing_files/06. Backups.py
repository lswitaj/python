#! /usr/bin/python3
# Backups.py - files and paths

import os, zipfile

def backupToZip(folder):
    #folder = os.path.abspath(folder)

    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number += 1

    print('Creating %s...' % (zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    for folderName, subFolders, fileNames in os.walk(folder):
        print('Adding files in %s...' % (folderName))
        backupZip.write(folderName)
        for fileName in fileNames:
            newBase = os.path.basename(folder) + '_'
            if fileName.startswith(newBase) and fileName.endswith('.zip'):
                continue
            backupZip.write(os.path.join(folderName, fileName))
    print('done')

backupToZip('./')