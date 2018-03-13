#! /usr/bin/python3
# data_renamer.py - files and paths

import shutil, os, re

os.chdir('dates/')

datePattern = re.compile(r"""^(.*?)
((0|1)\d)-
((0|1|2|3)?\d)-
((19|20)\d{2})
(.*?)$
""", re.VERBOSE)

for americanFilename in os.listdir('.'):
    mo = datePattern.search(americanFilename)

    if mo == None:
        continue

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    europeanFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    shutil.move(americanFilename, europeanFilename)