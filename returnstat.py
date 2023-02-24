import random, sys

def getAnswer(AnswerNumb):
    if AnswerNumb == 1:
        return 'It is certainly !'
    elif AnswerNumb == 2:
        return 'It is certainly 2'
    elif AnswerNumb == 3:
        return 'It is certainly 3'
    elif AnswerNumb == 4:
        return 'It is certainly 4'
    elif AnswerNumb == 5:
        return 'It is certainly 5'
    elif AnswerNumb == 6: 
        return 
    elif AnswerNumb == 7: 
        return 'It is certain 7'
    elif AnswerNumb == 8: 
        return 'It is certain 8'
    elif AnswerNumb == 9: 
        return 'It is certain 9-10'

r = random.randint(1, 9)
if r == 3:
    sys.exit()
print(getAnswer(r))