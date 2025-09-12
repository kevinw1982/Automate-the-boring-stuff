import time, sys
indent = 0 #how many spaces to indent
indent_increasing = True #Whether the indentation is increasing or not

try:
    while True: #the main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)#pause for 1/10th of a second

        if indent_increasing:
            #increase the number of spaces
            indent = indent + 1
            if indent == 20:
                #change direction
                indent_increasing = False
        else:
            #decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                #change direction:
                indent_increasing == True
except KeyboardInterrupt:
    sys.exit() 