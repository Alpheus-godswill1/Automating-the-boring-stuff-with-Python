# The in and not in operators are very case sensitive when it comes to  strings


Hi = '' in 'spam'
print(Hi)

Hk = 'Spam' in 'spam'
print(Hk)

Hy = 'Hello' in 'spam'
print(Hy)

Hl = 'Hello' in 'Hello'
print(Hl)

Hp = 'cats' not in 'cats and dog'
print(Hp)

Ho = 'HI' in 'hi'
print(Ho)