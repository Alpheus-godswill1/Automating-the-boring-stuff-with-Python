theBoard = {'top-L':'', 'top-M':'', 'top-R':'',
            'mid-L':'', 'mid-M':'', 'mid-R':'',    'bottom-L':'','bottom-M':'', 'bottom-R':''}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] )
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'] )
    print('-+-+-')
    print(board['bottom-L'] + '|' + board['bottom-M'] + '|' + board['bottom-R'] )
turn = 'X'.lower()
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input().lower()
    theBoard[move] = turn
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'
printBoard(theBoard)