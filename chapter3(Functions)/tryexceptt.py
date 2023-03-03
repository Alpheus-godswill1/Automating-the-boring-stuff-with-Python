def spam(y):
    try:
        return 45 / y
    except ZeroDivisionError:
        print('Sorry you can not divide with a zero!🤴👼👲👦👮‍♂️')
print(spam(int(input('Pick a Number: '))))

print('\n\n')

# Automating way of writing this code
def bacon(divis):
    return 43 / divis
try: 
    print(bacon(7))
    print(bacon(7))
    print(bacon(3))
    print(bacon(0))
    print(bacon(3))
except ZeroDivisionError:
    print('Error: Zero used as the denominator!')
    
