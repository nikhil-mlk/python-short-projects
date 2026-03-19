'''
Requirements:
1. Ask user for the length of the password he/she needs
2. Minimum length should be 6 and maximum should be 12
3. Password contains numerics, alphabets(upper & lower case) and special characters
4. User can have option to select alphabets OR special characters BUT numbers should be there
'''
import random
import string
import sys

numbers=string.digits
alphabets=string.ascii_letters
special_chars=string.punctuation

def get_password(length,alpha=True,special=True):
    final_password=''
    if length<6 or length>12:
        print('The length of the password should be between 6 and 12')
        sys.exit()
    if alpha and special:

        while len(final_password)<=length:
            print('inside loop')
            final_password += random.choice(numbers)
            if len(final_password)>=length:
                print(final_password)
                break
            final_password += random.choice(alphabets)
            if len(final_password)>=length:
                print(final_password)
                break
            final_password += random.choice(special_chars)
            if len(final_password)>=length:
                print(final_password)
                break



get_password(10)

