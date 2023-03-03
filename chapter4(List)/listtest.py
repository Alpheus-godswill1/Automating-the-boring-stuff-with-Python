import sys
# try:
#     catname = []
#     while True:
#         print('Enter the name of your cat')
#         name = input()
#         if name == '':
#             break
#         catname = catname + [name]
#     print('The cat name are: ')
#     for i in catname:
#         print(' '+ i)
# except KeyboardInterrupt:
#     sys.exit()

# catName = []
# while True:
#     print('Enter the name of cat' + str(len(catName) + 1 ) + '(or enter nothing to stop):')
#     name = input()
#     if name == '':
#         break
#     catName = catName + [name]
# print('The cat name are:')
# for i in catName:
#     print(' ' + i)

# using range(len(someList))
# supplies = ['curtains','window','love','omo','pen']
# for i in range(len(supplies)):
#     print('The index are ' + str(i) + ',' + ' the supplies are' + supplies[i])
    
# try:
#     mypets = ['dog', 'cats', 'rams']
#     while True:
#         name = input('Please insert name of cats: ')
#         if name == '':
#             break
#         elif name not in mypets:
#             print("Sorry, you pet can't be found here")
#         elif name in mypets:
#             print("You pet has been found here")
#         mypets = mypets + [name]
#     print('Your pet name was just added for your sake!')
#     for i in mypets:
#         print(''+ i)
# except KeyboardInterrupt:
#     sys.exit()
    
# Multiple Assignmet Trick

fruits = ['Mbngo','man' ,'Ability','amass','Blue','bick' ,'orange','pineapple','Guava']

# mangoTree, OrangeTree, Suck, GuavaTree = fruits
# print(mangoTree)

for index, items in enumerate(fruits):
    print('Index of each fruits are ' + str(index) + ' while  the item: ' + items )

del fruits[3]
print(fruits)

#Adding Values to list with the append() and insert() methods

fruits.append('[willy,vully,carim]')
print(fruits)

#Sorting the values in the list

# fruits.sort(reverse=True)


fruits.sort(key=str.lower)

print(fruits)






