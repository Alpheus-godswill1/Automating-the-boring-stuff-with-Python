import random

systemguess = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
print('Take a guess')

while True:
    userGuess = int(input())
    if userGuess < systemguess:
        print('Your guess is too low.')
        print('Take a guess')
    elif userGuess > systemguess:
        print('Your guess is too high.')
        print('Take a guess')
    else:
        break
print('Nice guess, you finally got the answer')