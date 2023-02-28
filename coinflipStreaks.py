import  random

def coinFlip():
    numberOfHeadStreaks = 0
    numberOfTailStreaks = 0
    flipList = []
    currentHeadStreak = 0
    currentTailStreak = 0
    for i in range(10000):
        flips = random.choice(['H','T'])
        flipList.append(flips)
        
        if flips == 'H':
            currentHeadStreak += 1
            currentTailStreak = 0
            if currentHeadStreak >= 6:
                numberOfHeadStreaks +=1
        else:
            currentTailStreak += 1
            currentHeadStreak = 0
            if currentTailStreak >= 6:
                numberOfTailStreaks += 1
                
    print(f'The number of Head Streak: {numberOfHeadStreaks} ')
    print(f'The number of Tail Streak: {numberOfTailStreaks} ')
    

coinFlip()