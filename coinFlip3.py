import random
guess = ''
while guess not in('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) #0 is tails 1 is heads
if guess == 'heads':
    num = 1
else:
    num = 1
if toss == num:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == num:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')