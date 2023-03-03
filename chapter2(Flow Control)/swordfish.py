while True:
    print('who are you?')
    name = input()
    if name != 'joe':
        continue
    print("Hi Joe, what is you password? (It is a fish)")
    password = input()
    if password == 'swordfish':
        break
print('Access granted!')