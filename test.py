
grid = [
['3', '4', '5', '.', '.', '.'],
['0', 'O', 'O', '6', '.', '.'],
['1', 'O', 'O', 'O', '7', '.'],
['.', 'O', 'O', 'O', 'O', '8'],
['.', 'O', 'O', 'O', 'O', '.'],
['2', 'O', 'O', 'O', '.', '.'],
['0', 'O', 'O', '.', '.', '.'],
['1', '.', '.', '.', '.', '.']]

for y in range(len(grid[0])):
    for x in range(len(grid)):
        print(grid[x][y], end='')
    print()
    
spam = {'cat': 45}
for cat in spam:
    print(cat)
    
    
    




allGuest = {'Alice':1,'Bob' : 5,'Greg' : 3,}   
def totalBrought(val):
    SumBrought = 0
    for v  in val.values():
        SumBrought += v.get(val, 0)
    return SumBrought

print('Number of things being brought are: ')
print(totalBrought(allGuest))

