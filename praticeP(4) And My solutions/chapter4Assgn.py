
def lstTake(x):
    spam = []
    for i in range(3):
        listVals = input('listVals: ')
        spam.append(listVals)
    print('The concatenated list values are: '+ str(spam)) 
    
    spam[-2] += f', {x}'
    print(str((', ').join(spam)))
lstTake('and')