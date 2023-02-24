# Rock, Paper, Scissor game
import random, sys

wins = 0 
losses = 0
ties = 0

while True: # Loop for the main game
    print('%s wins, %s losses, %s ties' % (wins, losses , ties))
    while True: # for the input of the player
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input().lower()
        
        if playerMove == 'q' or playerMove == 'quit':
            sys.exit() # Exit game when 'q' or 'quit' is entered
        
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Leave loop for the player
        print('Type one of r, p, s, or q')
    
    
    # Display  players' choice
    if playerMove == 'r':
        print('ROCK versus ...')
    elif playerMove == 'p':
        print('PAPER versus ...')
    elif playerMove == 's':
        print('SCISSOR  versus ...')
    
    
    # Displaye computer choice
    randomNumber = random.randint(1,3)
    
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
        
    # Compare records and increase values of wins/losses/ties
    
    if playerMove == computerMove:
        print("It's a tie!")
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('You loose!')
        losses += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins += 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins += 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You loose!')
        losses += 1
    elif playerMove == 'p' and computerMove == 's':
        print('You loose!')
        losses += 1
    elif playerMove == 's' and computerMove == 'r':
        print('You loose!')
        losses += 1
        
        