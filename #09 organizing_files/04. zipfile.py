#! /usr/bin/python3
# zipfile.py - files and paths

import os, zipfile

os.chdir('zips/')
exampleZip = zipfile.ZipFile('zipped_files.zip')

pdfFileName, txtFileName = exampleZip.namelist()

print('name: ' + txtFileName + ' size before compress: ' + str(exampleZip.getinfo(txtFileName).file_size) + ' size after: ' + str(exampleZip.getinfo(txtFileName).compress_size))
print('name: ' + pdfFileName + ' size before compress: ' + str(exampleZip.getinfo(pdfFileName).file_size) + ' size after: ' + str(exampleZip.getinfo(pdfFileName).compress_size))

exampleZip.extractall('unzipped') #u can also extract only some files
print('I unzipped into: ' + os.getcwd() + '/unzipped')
os.chdir(os.getcwd() + '/unzipped')

exampleZip.close()

newZip = zipfile.ZipFile('ill_be_new_zip.zip', 'w') #u can also type 'a'

newZip.write('pdf_to_zip.pdf', compress_type=zipfile.ZIP_DEFLATED)
newZip.write('sth_to_zip.txt', compress_type=zipfile.ZIP_DEFLATED)

newZip.close()