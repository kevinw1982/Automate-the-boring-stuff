birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    name = input('Enter a name: (Blank to quit)')
    if name == '':
        break
    
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print(f'I do not have birthday information of {name}')
        bday = input('What is there birthday?')
        birthdays[name] = bday
        print('Birthday database updated.')