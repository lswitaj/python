#! /usr/bin/python3
# move, delete.py - files and paths

import shutil, os

shutil.copy('here_is_sth_to_copy/sth_to_copy.txt', 'here_is_sth_to_copy/sth_copied.txt')
try:
    shutil.copytree('here_is_sth_to_copy', 'there_is_copied_folder')
except FileExistsError:
    print('File exist so it cannot be created')

try:
    shutil.move('there_is_copied_folder', 'here_is_sth_to_copy/lala_im_moved_too')
except shutil.Error:
    print('File was moved before')

print('I\'ll delete sth.copied.txt from here_is_sth_to_copy, to do this press antything')
input()
os.unlink(os.getcwd() + '/here_is_sth_to_copy/sth_copied.txt')

print('I\'ll delete there_is_sth_copied_folder, to do this press antything')
input()
shutil.rmtree(os.getcwd() + '/there_is_copied_folder')

print('all stuff is done thanks for work')