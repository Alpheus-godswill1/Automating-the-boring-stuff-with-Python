Numb1 = int(input('Type first Number: ')) 
Numb2 = int(input('Type second Number: '))
valueNumb = 49
NumbUsed = ''
sumNumb = Numb1 + Numb2

subtractedNumb = Numb1 - Numb2
if subtractedNumb < 49:
                subtValue = valueNumb - subtractedNumb
                print(subtValue)



if sumNumb  < 49:
                print(49 - (sumNumb))
                NumbUsed =  49 - sumNumb 
elif sumNumb  > 49:
        print((sumNumb) - 49)
        NumbUsed = sumNumb - 49

if  NumbUsed >= 0  and NumbUsed <= 4 :
        print(f'AddedValue: {NumbUsed + 5 }')
        
elif   NumbUsed >= 5  and NumbUsed <= 9 :
        print(f'AddedValue: {NumbUsed - 5 }')
        
elif   NumbUsed >= 10  and NumbUsed <= 14 :
        print(f'AddedValue: {NumbUsed + 5 }')
        
elif   NumbUsed >= 15  and NumbUsed <= 19 :
        print(f'AddedValue: {NumbUsed - 5 }')
        
elif   NumbUsed >= 20  and NumbUsed <= 24 :
        print(f'AddedValue: {NumbUsed + 5 }')
        
elif   NumbUsed >= 25  and NumbUsed <= 29 :
        print(f'AddedValue: {NumbUsed - 5 }')
        
elif   NumbUsed >= 30  and NumbUsed <=  34:
        print(f'AddedValue: {NumbUsed + 5 }')
        
elif   NumbUsed >= 35  and NumbUsed <= 39 :
        print(f'AddedValue: {NumbUsed - 5 }')
        
elif   NumbUsed >= 40  and NumbUsed <= 44 :
        print(f'AddedValue: {NumbUsed + 5 }')
        
elif   NumbUsed >= 45  and NumbUsed <= 49 :
        print(f'AddedValue: {NumbUsed - 5 }')











