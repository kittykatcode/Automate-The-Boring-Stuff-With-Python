#! python3
#pw.py - An insecure password locker program.

PASSWORD = { 'email': 'kritikakaushik678605@gmail.com',
             'blog': 'whatthefuck',
             'luggage':'123456'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] #frist command line arg is the account name

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print('Password for' + account + 'copied to clipboard.')

else:
    print('there is no account named' + account)
