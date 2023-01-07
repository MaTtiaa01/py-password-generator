#Ask some question to the user to build a strong password

import random

#charcachtrs

letter_numbers = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
all_char = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/.@?|>$%&(!'

random_password = ''

pass_length = input('Long or short password? Type short or long: ')
pass_char = input('Do you also want special charachters? Type yes or no: ')

#print(random.choice(letter_numbers))

if pass_length == 'long':
    if pass_char == 'yes':
        while len(random_password) < 12:
            random_char = random.choice(all_char)
            random_password += random_char
    else:
         while len(random_password) < 12:
            random_char = random.choice(letter_numbers)
            random_password += random_char
else:
    if pass_char == 'yes':
        while len(random_password) < 8:
            random_char = random.choice(all_char)
            random_password += random_char
    else:
         while len(random_password) < 8:
            random_char = random.choice(letter_numbers)
            random_password += random_char



print(random_password)