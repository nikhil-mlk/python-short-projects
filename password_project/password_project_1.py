'''
Requirement:
User will enter the password
We need check following if password is strong or weak

A strong password should contain:
Minimum 8 characters
At least 1 uppercase letter
At least 1 lowercase letter
At least 1 digit
At least 1 special character

How to do:
Ask uer to enter password.
store the password in string
apply regex on it to validate the password.
'''

import re
import sys


def enter_password():
    password=input('Enter the password: ')
    return password

def check_password():

    value=True
    while value:

        password = enter_password()

        # Find length of password
        length = len(password)

        # Find Upper Case
        list_upper_case = re.findall('[A-Z]', password)

        # Find Lower Case
        list_lower_case = re.findall('[a-z]', password)

        # Find digits
        list_digits = re.findall('[0-9]', password)

        # Find Special Characters # ----- Imp ----
        list_special_characters = re.findall(r'[^a-zA-Z0-9\s]', password)

        # Find spaces
        list_spaces = re.findall(r'\s', password)

        if length < 8:
            print('Password Must be minimum 8 characters')
            check_password()
        if len(list_special_characters)>0:
            str_of_special_char="&()-_+=~"
            final_str=''
            for i in range(len(str_of_special_char)):
                if str_of_special_char[i] in list_special_characters:
                    final_str+=str_of_special_char[i]
            if len(final_str)>0:
                print('Special Characters: ', final_str, 'are not allowed')
                check_password()
        if len(list_spaces) > 0:
            print('Password should not contains spaces')
            check_password()
        if len(list_upper_case)==0:
            print('Password should contains at least one uppercase letter')
            check_password()
        if len(list_lower_case)==0:
            print('Password should contains at least one lowercase letter')
            check_password()
        if len(list_digits)==0:
            print('Password should contains at least one digit from 0-9')
            check_password()
        if len(list_special_characters)==0:
            print('Password should contains at least one special character')
            check_password()
        else:
            print('Password accepted: ', password)
            sys.exit()



        # elif length >= 8 and len(list_upper_case) > 0 and len(list_lower_case) > 0 and len(list_digits) >0 and len(
        #     list_special_characters) > 0 and len(list_spaces) == 0:
        #     print('Password accepted: ', password)
        #     value=False



check_password()









