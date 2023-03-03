# Writing a program that says hello and asks for my name 

print("Hello, what's your name? ")
myName = str(input())
print('It is good to meet you '+ myName)
print('The length of your name is: ')
print(len(myName))
print("What's your age")
age = int(input())
print('You are going to be ' + str(int(age) + 1 ) + ' in a year')