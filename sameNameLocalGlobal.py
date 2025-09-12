def spam():
    global eggs
    eggs = 'spam'# This is the Global variable

def bacon():
    eggs = 'bacon' # This is a local variable

def ham():
    print(eggs) # this is the global variable

eggs = 'global' # this is the global variable
spam()
print(eggs)