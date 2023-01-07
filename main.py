#Ask some question to the user to build a strong password

import random

#charcachtrs

letter_numbers = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
all_char = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/.@?|>$%&(!'

random_password = ''

pass_length = input('Long or short password? Type short or long: ')
pass_char = input('Do you also want special charachters? Type yes or no: ')

#print(random.choice(letter_numbers))


#loop function
def getPassword(number,string,newstring):
    while len(newstring) < number:
            random_char = random.choice(string)
            newstring += random_char
    return newstring

if pass_length == 'long':
    if pass_char == 'yes':
        random_password = getPassword(12,all_char,random_password)
    else:
        random_password = getPassword(12,letter_numbers,random_password)
else:
    if pass_char == 'yes':
       random_password = getPassword(8,all_char,random_password)
    else:
        random_password = getPassword(8,letter_numbers,random_password)



print(random_password)