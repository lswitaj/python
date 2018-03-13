#! /usr/bin/python3
# regex_2.py - Regular expressions vol. 2

import re

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{3})')
found = phoneNumRegex.search('333-333-333 is not my 777777 number 555-343-421')

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 12   drummers'))

eldo = 'Like a COP ROBO with empty head'
vowelRegex = re.compile(r'[aeiouyAEIOUY]')
print(vowelRegex.findall(eldo))

consontantRegex = re.compile(r'[^aeiouyAEIOUY]')
print(consontantRegex.findall(eldo))

fiveFirstLetRegex = re.compile(r'[a-e]')
print(fiveFirstLetRegex.findall(eldo))