chessBoardValue = {'1h': 'bking', '6c': 'wqueen', 
'2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def isValidChessBoard(KeyValid, ValueValid):
    for KeyValid, ValueValid in chessBoardValue.get(KeyValid, 0):
        print(KeyValid)
    else:
        return ValueValid
        