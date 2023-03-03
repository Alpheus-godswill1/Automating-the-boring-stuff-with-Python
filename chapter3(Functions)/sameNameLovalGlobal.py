def spam():
    global egg
    egg = 'spam spam spam' # this is global

def bacon():
    egg = 'John' # this is local
    

def ham():
    print(egg) # This is global

egg = 42 # this is global
ham()
spam()
print(egg)
    
    
    
    
    