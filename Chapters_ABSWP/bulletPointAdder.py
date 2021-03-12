#! python3

# adding bullet points to the text, adding * to the new lines

import pyperclip

text = pyperclip.paste()

#seperate lines and add *
lines = text.split('\n')
for i in range(len(lines)):  #looping all the indexes in lines
    lines[i] = '*' + lines [i] # adding * at each 'lines' list

pyperclip.copy(text)
