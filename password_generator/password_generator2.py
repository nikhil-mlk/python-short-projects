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
# numbers=string.digits
# alphabets=string.ascii_letters
# special_chars=string.punctuation
def get_password(length,alpha=True,special=True):
    final_password=random.choice(string.digits)

    if length<6 or length>12:
        print('The length of the password should be between 6 and 12')
        sys.exit()

    if alpha and special:
        while len(final_password)<=length:
            final_password+=random.choice(string.ascii_letters)
            if len(final_password) >= length:
                break
            final_password+=random.choice(string.punctuation)
    elif alpha:
        while len(final_password)<=length:
            final_password+=random.choice(string.ascii_letters)
            if len(final_password) >= length:
                break
    elif special:
        while len(final_password) <= length:
            final_password += random.choice(string.punctuation)
            if len(final_password) >= length:
                break
    print(final_password)


get_password(10,False,True)

