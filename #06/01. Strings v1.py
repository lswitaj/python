#! /usr/bin/python3
# password.py - An insecure passord locker program

PASSWORDS = {'email': 'lalapass',
             'blog': 'blogpass',
             'luggage': 'myP ass_123'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python passwird.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   #first parameter is account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Pass for ' + account + 'copied to clipboard')
else:
    print('There is no account named ' + account)
