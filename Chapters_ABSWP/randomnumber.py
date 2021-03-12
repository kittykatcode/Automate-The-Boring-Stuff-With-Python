import random


print('Whats your name ?')
name = input()
secretnumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20')
try:

    for guesses in range (1,7):
        print('take a guess')
        guess = int(input())

        if guess > 20:
            print('we asked to guess a number between 1 and 20 phunk! ')

        elif guess < secretnumber:
            print('your guess is too low')
        elif guess > secretnumber:
            print('your guess is too high')

        else:
            break

    if guess == secretnumber:
        print('good job' + name + ' guessed the number i was thinking in '+ str(guesses)+' guesses.')
    else:
        print(name +' could not guess my number, iwas thinking about '+str(secretnumber)+'.')

except ValueError:
    print('please type a number')
