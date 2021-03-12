
#to find out if given text has phone mumber

def isPhoneNumber(text):
    #check in the number has 12 characteres xxx-xxx-xxxx
    if len(text) != 12:
        return False
    # check if 1st 3 digit is integer (0-3 not including 3 so 0,1,2)
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True


print("123-456-0789 is a phone number")
print(isPhoneNumber('123-456-0789'))
print("is moshi poshi is phone number")
print(isPhoneNumber('moshi-poshi'))
print("123 456 0789 is a phone number")
print(isPhoneNumber('123 456 0789'))

message = 'call me at 415-555-1011 tomorrow, 415-555-1234 is my office number'

for i in range(len(message)):
    chunck = message[i:i+12]
    if isPhoneNumber(chunck):
        print("phone number found :" + chunck)

print('done')
