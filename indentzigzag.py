#Creating a zigzag game 
import time, sys

indent = 0 # How many spaces should be left when code starts
indentIncrement = True # To check whether the indentation is increasing or not

try:
    while True: # Main program loop
        print(' +' * indent, end = ' !! ')
        print('*****')
        time.sleep(0.1) #Regulating the time of the zigzag occurance
        
        if indentIncrement: #checking if the indentIncrement is still True so I can increment the indentation
            indent += 1
            if indent == 10:
                
                indentIncrement = False # This is done so the indentation can return back and the zigzag can flow well
        else:
        #Decrease the number of spaces:
            indent -= 1
            if indent == 0:
            #change direction 
                indentIncrement = True
except KeyboardInterrupt:
    sys.exit()