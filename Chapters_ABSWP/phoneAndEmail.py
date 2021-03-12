#! python3
#phoneAnd Email.py - finds phonenumbers and email adderss on the clipboard

import re, pyperclip

#Create phone regex.
phoneregex = re.comple(r'''(
(\+\d{2,4})             # national code
(\d\d\d| \(\d\d\d\))?  # area code
(-|\s|\.)?             # seperater or just space
(\d{3})                # 3 digit numbers
(-|\s|\.)?             # seperater or just space
(\d{4})                # 4 digit numbers
(ext|x|\.|-|{2,5})     # extn
)''', re.VERBOSE)

#TODO : Create email regex.
emailregex = re.compile(r'''(
[a-z0-9\._\+]                    # name part
@                                 # @ symbol
[a-z0-9\._\+]                     # domain name part
)''', re.VERBOSE, re.I)

# Find matches in the clipboard text.
text = pyperclip.paste()

# extract email and phone
getphone = phoneregex.findall(text)
getemail = emailregex.finfall(text)

allphone = []
for phone in getphone:
    allphone.append(getphone[0])
    print(allphone)

# copy extracted email/phone to the clipboard

restult = '\n'.join(allphone) + '\n' + '\n'.join(getemail)
pyperclip.copy(result)
