# The Keys(), Values(), and items Methods
# The values returned by this methods are not true lists: they cannot ve modified and do not have an append method.

spam = {'color':'red', 'hair':'brown', 'cloth':'jean', 'Water':'Pure', 'House':'white', 'Matches':'2,4', 'Up':'Down'}


print(' ')
print('Values of a Dictionary')
for v in spam.values():
    print(v)
print(' ')


print('Items of a Dictionary(Key:Value Pair)')
for i in spam.items():
    print(i)
print(' ')


print('Keys of a Dictionary')
for z in spam.keys():
    print(z)
print(' ')
