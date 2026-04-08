'''
Write a function that takes a string and an integer n, and returns a shortened version
of the string such that:

Final string ki length n ke andar ho
Kisi word ko beech mein cut na karo (word ka meaning change nahi hona chahiye)
Output string end ho " ..." (ek space + three dots) se"

Ex:
Input:  str = "I love programming very much", n = 10
Output: "I love ..."

Input:  str = "Hello world from AI", n = 15
Output: "Hello world ..."

I love programming      very much
I love pro              gramming very much
'''

def alter_string_according_to_length():
    add_string=' ...'
    user_string=input('Enter the string: ')
    length=int(input('Enter the length: '))

    if len(user_string)<=length:
        return user_string

    main_list=list(user_string)
    secondary_list=list(user_string[0:len])

    last_value_main=main_list[-1]
    last_value_secondary=secondary_list[-1]

    if last_value_main!=last_value_secondary:
        pass
    pass




















