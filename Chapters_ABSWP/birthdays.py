birthdays = { 'Alice' : '21 Oct', 'bob': '5 jun', 'suzan': '17 Oct'}

while True:
    print('enter a name:')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name]+' is the birthday of' +name)
    else:
        print('I dont have birthday info of' + name)
        print('what is there birthday?')
        bday = input()
        birthdays[name] = bday
        print('birthday database updated')
        print(birthdays)
    
