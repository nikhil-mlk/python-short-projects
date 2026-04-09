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


Thought Process:
we need string according to user specific length
then we need another string which is 4 characters less than the user specific length (because we need to add ' ...' at the end of string)
Convert both the string into Lists so that we can check the last word of the string which is 4 characters less than the user specific length is present in the string which is according to user specific length or not

Now possible combinations after lessen 4 characters from user specific length:
1. I love pro
2. I love p
3. I love space
4. I love
'''
def alter_string_according_to_length():
    add_string=' ...'
    user_string=input('Enter the string: ')
    length=int(input('Enter the length: '))

    # Create Strings for both
    str_as_per_length=user_string[0:length]
    str_after_deduction=user_string[0:length-4]

    #Create Lists for both Strings
    list_as_per_length=str_as_per_length.split()
    list_after_deduction=str_after_deduction.split()

    if len(user_string)<=length:
        return user_string
    # I love space
    if str_after_deduction[-1]==' ':
        return str_after_deduction[0:len(str_after_deduction)-1]+add_string
    # I love pro I love p
    elif list_after_deduction[-1] not in list_as_per_length:
            index1 = list_after_deduction.index(list_after_deduction[-1])  # 1
            extract_word = list_as_per_length[index1]  # world
            index_of_word = str_as_per_length.rindex(extract_word)  # 6
            extracted_sub_string = str_after_deduction[index_of_word - 1:len(str_after_deduction)]
            return str_after_deduction.replace(extracted_sub_string, add_string)
    # I love
    else:
        return str_after_deduction+add_string


res=alter_string_according_to_length()
print(res)

































