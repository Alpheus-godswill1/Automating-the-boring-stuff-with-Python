import sys

while True:
    print('Type in exit to exit')
    type_exit = input()
    if type_exit == 'exit':
        sys.exit()
    print('You just exited the while loop clause!')