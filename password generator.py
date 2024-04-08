def generate_passwords(number_passwords=1,length_password=6):
    import string
    import random
    set_characters=string.ascii_letters+string.digits+string.punctuation
    passwords=''
    for iteration in range(number_passwords):
        password=''
        for number in range(length_password):
            password+=random.choice(set_characters)
        if password not in passwords: passwords+=password+'  '
    return passwords


while True:
    try: start=input('\nDo you want to generate passwords: ').lower()
    except ValueError: print('Invalid Input!\n')
    if start=='yes':
        try: 
            number_passwords=int(input('Enter the number of passwords: '))
            length_passwords=int(input('Enter the length of passwords: '))
            print(generate_passwords(number_passwords,length_passwords))
        except ValueError: print('Invalid Input!\n')
    elif start=='no': break
    else: print('Invalid Input!\n')
