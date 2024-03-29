"""
?? isalpha() -- Returns True if the string consists only of letters and isn’t blank.

* isalnum() -- Returns True if the string consists only of letters and numbers and is not blank.

!! isdecimal() -- Returns True if the string consists only of numeric characters and is not blank.

* isspace() -- Returns True if the string consists only of spaces, tabs, and newlines and is not blank.

!! istitle() -- Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letter.

"""

print('hello'.isalpha())

print('hello123'.isalpha())

print('hello123'.isalnum())

print('hello'.isalnum())

print('123'.isdecimal())

print(' '.isspace())

print('This Is Title Case'.istitle())

print('This Is Title Case 123'.istitle())

print('This Is not Title Case'.istitle())

print('This Is NOT Title Case Either'.istitle())