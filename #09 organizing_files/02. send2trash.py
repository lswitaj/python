#! /usr/bin/python3
# send2trash.py - files and paths

import send2trash

baconFile = open('bacon.txt', 'a') #to create txt file
baconFile.write('bacon is a vegetable')
baconFile.close()
send2trash.send2trash('bacon.txt')
