#ROCK, PAPER, SCISSORS GAME IN PYTHON
import random , sys

#The Variable below are to keep track of the number of wins, losses, and ties
wins = 0
losses = 0
ties = 0

while True: # True main game loop.
    print('%s wins, %s losses, %s ties' % (wins, losses, ties))
    while True: # The player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input().lower()
        if playerMove == 'q':
            sys.exit() #Quit the program
            
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop
        print('Type one of r, p, s, or q')

    #Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus ...')
    elif playerMove == 's':
        print('Scissors versus ...')
    elif playerMove == 'p':
        print('Paper versus ...')
        
    #Display what the computer chose 
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('Rock')
    elif randomNumber == 2:
        computerMove = 'p'
        print('Paper')
    elif randomNumber == 3:
        computerMove = 's'
        print('Scissors')
    