def spam():
    global egg
    egg = 'spam'
    
egg = 'global'
egg = 'boy'
spam()
print(egg)