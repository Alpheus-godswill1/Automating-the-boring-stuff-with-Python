# Practice Projects
# For practice, write programs to do the following tasks.

# Comma Code:
    
# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns 
# a string with all the items separated by a comma and a space, with and
# inserted before the last item. For example, passing the previous spam list to 
# the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test 
# the case where an empty list [] is passed to your function.


def lstTake(x):
    spam = []
    for i in range(3):
        listVals = input('listVals: ')
        spam.append(listVals)
    print('The concatenated list values are: '+ str(spam)) 
    
    spam[-2] += f', {x}'
    print(str((', ').join(spam)))
lstTake('and')