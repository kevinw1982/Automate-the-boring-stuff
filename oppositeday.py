#Set say it is the opposite day is based on today is the opposite day
today_is_the_opposite_day = True
if today_is_the_opposite_day == True:
    say_it_is_opposite_day = True
else:
    say_it_is_opposite_day = False

#If it is the opposite day, toggle say it is the opposite day
if today_is_the_opposite_day == True:
    say_it_is_opposite_day = not say_it_is_opposite_day

#Say what day it is
if say_it_is_opposite_day == True:
    print("Today is the Opposite Day.")
else:
    print("Today is not the Opposite Day.")