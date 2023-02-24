def spam():
    eggs = 'spam local'
    print(eggs) #print 'spam local'
    
def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs) #prints 'bacon local'
    
eggs = 'globally'
bacon()
print(eggs) #print 'globally'


