spam = {'color':'red','age':'42'}
print('name' in spam.keys())
print('color' not in spam.keys())
print('color' in spam.keys())
print('42' in spam.values())
print(spam.get('color',0))
print(spam.get('agj', 9))

# First way to use the setdefault(), which is too long compared to using the method setdefault()
if 'friend' not in spam:
    spam['friend'] = 'Utibeabasi, Emma, Steph, Alpheus'
    
# Best and shortest way to assign a key to a value using in one line of code is using setdefault()

print(spam.setdefault('color', 9)) #this can only function if the key you are trying to set does not already have a value assigned to it.
print(spam.setdefault('name','Alpheus the CEO of BentCullinan,Rollins,CrystalSign'))
print(spam)





