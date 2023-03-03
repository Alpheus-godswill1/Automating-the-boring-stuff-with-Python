# This is a guess game 
import random

secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20!')

#Ask the player to guess 6 times
for guessTaken in range(1,10):
    print('Take a guess')
    guess = int(input())
    
    if guess < secretNumber:
        print('guess to low!')
    elif guess > secretNumber:
        print('guess to high')
    else:
        break # This conditions is for the correct guess!
if guess == secretNumber:
    print('Good job! you guessed my number in ' + str(guessTaken) + ' trials')
else:
    print('Nope, the number I was thinking of was ' + str(secretNumber))