#! /usr/bin/python3
# regex_1.py - Regular expressions vol. 1

import re

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{3})')
found = phoneNumRegex.search('333-333-333 is not my 777777 number 555-343-421')

for i in range(3):
    print(found.group(i)) #0-get all, 0+i-get i group

firstPart, secondPart = found.groups()
print(found.groups())
print(firstPart == found.group(1) and secondPart == found.group(2))

foundAll = phoneNumRegex.findall('333-333-333 is not my 777777 number 555-343-421')

for telNum in foundAll:
    print(telNum)

#we can also use a pipe | -> it means OR
print()
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')

try:
    print(mo.group())
except AttributeError:
    print('phrase not found')

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())