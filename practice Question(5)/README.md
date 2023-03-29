# Practice Question for the chapter 5 -- Dictionaries and Data Structure

1. What does the code for an empty dictionary look like?
2. What does a dictionary value with a key 'foo' and a value 42 look like?
3. What is the main difference between a dictionary and a list?
4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
5. If a dictionary is stored in spam, what is the difference between the 
expressions 'cat' in spam and 'cat' in spam.keys()?
6. If a dictionary is stored in spam, what is the difference between the 
expressions 'cat' in spam and 'cat' in spam.values()?
7. What is a shortcut for the following code?
if 'color' not in spam:
 spam['color'] = 'black'
8. What module and function can be used to “pretty print” 
dictionary values?

# Answers to the Questions

1. Quest. --  What does the code for an empty dictionary look like?

    Ans.  --  EmptyDict = {} 
              print(EmptyDict)

2. Quest. --   What does a dictionary value with a key 'foo' and a value 42 look like?

    Ans. -- test = {'foo':42}
            print(test)

3. Quest. -- What is the main difference between a dictionary and a list?

    Ans. --  Dictionaries are useful because you can map one item (the key) 
               to another (the value), as opposed to lists, which simply contain a series of 
               values in order. 
4. Quest. -- What happens if you try to access spam['foo'] if spam is {'bar': 100}?

    Ans. --  Traceback (most recent call last):
            File "test.py", line 18, in <module>
                print(spam[foo])
            NameError: name 'foo' is not defined

5. Quest. -- If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

    Ans. --  No difference the expression evaluates to the same thing 

6. Quest. --  If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

    Ans. --  There is a difference because:

            cat in spam, would evaluate to the key, 

                    while 
            cat in spam.values(), would evaluate the value of the key cat.
7. Quest. -- What is a shortcut for the following code?

            if 'color' not in spam:
            spam['color'] = 'black'

    Ans. --  spam.setdefault('color', 'black')
            print(spam)

8. Quest. -- What module and function can be used to “pretty print” dictionary values?
 
    Ans. -- import pprint
            test = {}
            pprint.pprint(test)