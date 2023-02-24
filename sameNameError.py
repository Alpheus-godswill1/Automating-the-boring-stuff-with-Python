def spam():
    # print(egg) #Error
    egg = 'spam local'
    
egg = 'global'
spam()
print(egg)