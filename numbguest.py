name = ''
while not name:
    print('Enter your name: ')
    name = input()
print('How may guests will you have? ')
numOfGuests = int(input())
if numOfGuests:
    print('Be sure to have enough room for all your guest.')
print('Done')