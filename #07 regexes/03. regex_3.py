#! /usr/bin/python3
# regex_3.py - Regular expressions vol. 3

import re

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Africa Last Name: Bambata')
print(mo.group(1))
print(mo.group(2))

#greedy and nongreedy regexes
nongreedyRegex = re.compile(r'<.*?>')
nonGreedyMo = nongreedyRegex.search('<To serve man> for dinner.>')
print(nonGreedyMo.group())
greedyRegex = re.compile(r'<.*>')
greedyMo = greedyRegex.search('<To serve man> for dinner.>')
print(greedyMo.group())
print()

#substituting strings
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave us Agent Carol documents.'))