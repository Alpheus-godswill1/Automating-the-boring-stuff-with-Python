
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