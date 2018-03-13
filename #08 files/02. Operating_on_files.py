#! /usr/bin/python3
# files_.py - files and paths

def writeLines(fileName):
    helloFile = open(fileName, 'r') #r - read
    #print(helloFile.read());
    print(helloFile.readlines());
    helloFile.close();

import os

os.chdir('/'.join([os.getcwd(), 'snacks']))

writeLines('hello.txt')

helloFile = open('hello.txt', 'w') #w - write, a - append
helloFile.write('The world is beautiful!')
helloFile.close();

writeLines('hello.txt')

helloFile = open('hello.txt', 'a') #w - write, a - append
helloFile.write('\nVery world is beautiful!')
helloFile.close();

writeLines('hello.txt')