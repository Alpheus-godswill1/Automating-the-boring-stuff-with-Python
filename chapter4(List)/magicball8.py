import random, sys, time

try:
    while True:
        message = [
    'It is uncertain',
    'I will be back',
    'Finishing well',
    'How to win strong',
    'What a nice way to win',
    'I am young and vibrant',
    'I love what I do',
    'I love Jesus',
    'Life is full of Joy',
    '5 need valid certainties to excel',
    'I am who GOD says I am',
    'I shall make it this year',
    'It just take one right step',
    'I am putting actionable steps in place'
]
        print(message[random.randint(0, len(message)-1)])
        time.sleep(0.6)

except KeyboardInterrupt:
    sys.exit