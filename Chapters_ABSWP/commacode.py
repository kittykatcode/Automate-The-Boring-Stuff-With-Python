spam = [ 'apple' , 'banana', 'toufu', 'cheese']

def commacode(joinedlist):
    for i in joinedlist:
        print(', '.join(joinedlist[:-1]) + ' and '+ joinedlist[-1] + str('.'))

        break

commacode(spam)
