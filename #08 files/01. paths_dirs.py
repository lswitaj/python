#! /usr/bin/python3
# files_.py - files and paths

import os, math

myFiles = ['pyhonProgramm1.py', 'myDataBase1.db']
for filename in myFiles:
    print(os.path.join('home', 'lswitaj', 'Pulpit', 'python', filename))

#cwd - current working directory
print(os.getcwd())

try:
    os.chdir('/home/NotExistingFile')
except FileNotFoundError:
    print('File doesnt exist')

os.chdir('/home/lswitaj/Pulpit/python/#08 files')

try:
    os.makedirs('/'.join([os.getcwd(), 'snacks']))
except FileExistsError:
    print('File exists - you\'ve been redirected their')
    os.chdir('/'.join([os.getcwd(), 'snacks']))
    print('Your current path is ' + os.getcwd())

print('/usr/bin'.split(os.path.sep))

totalSize = 0
for filename in os.listdir('/home/lswitaj/Pulpit'):
    print(filename + ' ' + str(round(os.path.getsize('/home/lswitaj/Pulpit/' + filename)/1024.0, 2)) + ' KiB')
    totalSize += os.path.getsize('/home/lswitaj/Pulpit/' + filename)
print(str(totalSize/math.pow(10,6)) + ' MB')