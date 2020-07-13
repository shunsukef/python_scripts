#! python3

PASSWORDS = {'email': 'aaaaaa','git': 'bbbb'}

import sys
import pyperclip
if len(sys.argv) < 2:
	print("how to use: python pw.py [account_name]")
	print("copy password to clipboard")
	sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print(account, "password is copied to clipboard")
else:
	print(account, "is not exist")

