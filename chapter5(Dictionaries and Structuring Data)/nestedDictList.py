allGuest = {'Alice':{'apples':5, 'pretzels':12},
            'Bob' : {'ham': 3, 'appFun': 4},
            'Greg' : {'cups': 9, 'suyaMen': 8},
            }   

def totalBrought(guest, item):
    numBrought = 0
    for k, b  in guest.items():
        numBrought += b.get(item, 0)
    return numBrought

print('Number of things being brought are: ')
print(' -Apples ' + str(totalBrought(allGuest, 'apples')))
print(' -cups ' + str(totalBrought(allGuest, 'cups')))
print(' -Cakes ' + str(totalBrought(allGuest, 'cakes')))
print(' -Suyamen ' + str(totalBrought(allGuest, 'suyaMen')))
