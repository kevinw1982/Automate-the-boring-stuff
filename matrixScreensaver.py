import random, sys, time

WIDTH = 70 # the number of columns

try:
    #for each column when the counter is 0, no stream is shown
    #otherwise, it acts as a counter for how many tmies a 1 or 0 should be displayed in that column
    columns = [0] * WIDTH
    while True:
        #loop over each column
        for i in range(WIDTH):
            if random.random() < 0.02:
                #restart a stream counter on this column
                # the stream column is between 4 and 14 characters long
                columns[i] = random.randint(4, 14)
            #print a character in this column
            if columns[i] == 0:
                #change this ' '' to '.' to see empty spaces
                print(' ', end='')
            else:
                #print a 0 or 1
                print(random.choice([0, 1]), end='')
                columns[i] -= 1 #decrement the counter for thiw column
        print()  #print a new line at the end of the row of columns
        time.sleep(0.1) #each row pauses for one tenth of a second
except KeyboardInterrupt:
    sys.exit() #when Ctrl-C is pressed end the program 
