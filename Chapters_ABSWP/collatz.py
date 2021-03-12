import sys

def collatz(number):
    if number % 2 == 1:
        result = 3* number+1
    elif number % 2 == 0:
        result =  number//2

    while result == 1:
        print(result)
        sys.exit()
    while result !=1:
        print(result)
        number = result
        return collatz(number)

print('please enter a number')
try:
    number = int(input( ))
    collatz(number)
except ValueError:
    print("please type a freakin number")
except TypeError:
    print("please type a freaking number")
    collatz()
