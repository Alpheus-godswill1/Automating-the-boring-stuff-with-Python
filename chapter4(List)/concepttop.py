#This is a simple Zigzag game!
import time, sys

indent = 2 # How many spaces to indent
indentIncreasing = False # Whether the indentation is increasing or not

try:
    while True: # The main program loop
        print('+++' * indent, end =' !! ')
        print('******')
        time.sleep(0.00002) # pause for 1/10 of a second
        
        if indentIncreasing:
            #Increase the number of spaces
            indent += 1
            if indent == 10:
                #change direction:
                indentIncreasing = False
        else:
        #Decrease the number of spaces:
            indent -= 1
            if indent == 0:
            #change direction 
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
