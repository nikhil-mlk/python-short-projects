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
'''
# Hello world from AI
# Hello world fro    n=15

# Hello World    11
#
def string_creation():
    str1=input('Enter the sentence: ')
    length=int(input('Enter the length: '))
    str2=' ...'
    if len(str1)<=length:
        return str1
    else:
        new_str = str1[0:length - 4]
        last_index = len(new_str) - 1

        if new_str[last_index - 1] == ' ':
            cap_str = new_str[last_index - 1:len(new_str)]
            final_string1 = new_str.replace(cap_str, str2)
            return final_string1

        elif new_str[last_index]==' ':
            cap_str3=new_str[last_index]
            final_string3 = new_str.replace(cap_str3, str2)
            return final_string3





res=string_creation()
print(res)





















