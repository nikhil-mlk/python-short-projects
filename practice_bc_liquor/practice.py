def reverse_string(s):
   return s[::-1]
result=reverse_string('hello world')
print(result)

def first_non_repeating_character(s):
    for ch in s:
        if s.count(ch)==1:
            return ch
    return None

result=first_non_repeating_character('aabbcdde')
print(result)


def reverse_only_words(s):
    empty_string=''
    lst=s.split(' ')

    for i in lst[::-1]:
        empty_string=empty_string+i+' '
    return empty_string.strip()

result=reverse_only_words('nikhil malik')
print(result)

def find_duplicates_in_list(ls):
    final_list=[]
    dictionary={}
    for numb in ls:
        if numb in dictionary:
            dictionary[numb]+=1
        else:
            dictionary.setdefault(numb,1)
    for i in dictionary.keys():
        if dictionary[i]>1:
            final_list.append(i)
    return final_list

result=find_duplicates_in_list([1, 2, 3, 2, 4, 1])
print(result)


def count_vowels(s):
    vowels_list='aeiou'
    s='automation'
    counter=0
    for i in s:
        if i in vowels_list:
            counter+=1
    return counter

result=count_vowels('automation')
print(result)

def check_palindrome(original_str):
    final_str=''
    for i in original_str[::-1]:
        final_str+=i
    if final_str==original_str:
        return 'It is Palindrome'
    return 'It is Not Palindrome'

result=check_palindrome('madam')
print(result)

def max_number_in_list(list_of_numbers):
    max=list_of_numbers[0]
    for number in list_of_numbers:
        if number>max:
            max=number
    return max

result=max_number_in_list([3, 5, 1, 9, 2])
print(result)


def remove_duplicates_from_list_but_keep_order(list_of_numbers):
    final_list=[]
    for i in list_of_numbers:
        if i not in final_list:
            final_list.append(i)
    return final_list

result=remove_duplicates_from_list_but_keep_order([1, 2, 2, 3, 1, 4])
print(result)


def sum_of_even_numbers(list_of_numbers):
    sum=0
    for i in list_of_numbers:
        if i%2==0:
            sum+=i
    return sum

result=sum_of_even_numbers([1, 2, 3, 4, 5, 6])
print(result)


def second_largest_number(list_of_numbers):
    list_of_numbers.sort()
    return list_of_numbers[len(list_of_numbers) - 2]
result=second_largest_number([10, 20, 4, 45, 99])
print(result)


def anagram_strings_method_1(s1,s2):
    dictionary1 = {}
    dictionary2 = {}
    if len(s1)==len(s2):
        for i in range(0,len(s1)):
            if s1[i] in dictionary1:
                val1=dictionary1.get(s1[i])
                val1+=1
            else:
                dictionary1.setdefault(s1[i],1)
            if s2[i] in dictionary2:
                val2=dictionary2.get(s2[i])
                val2+=1
            else:
                dictionary2.setdefault(s2[i],1)
        print(dictionary1)
        print(dictionary2)
        if dictionary1 == dictionary2:
           return 'Its anagram'
        else:
            return 'Not anagram'

result=anagram_strings_method_1('listen','silent')
print(result)

def anagram_strings_method_2(s1,s2):
    if len(s1)==len(s2):
        for i in range(0,len(s1)):
            ch=s1[i]
            if ch in s2:
                if s1.count(ch)==s2.count(ch):
                    continue
                else:
                    return 'Not Anagram'
        else:
            return 'Anagram'
    else:
        return 'Not Anagram'


result=anagram_strings_method_2('listen','silent')
print(result)


def first_duplicate_element(lst):

    for i in lst:
        if lst.count(i)>1:
            return i
    return None

result=first_duplicate_element([6, 3, 9, 5, 3, 2])
print(result)


def move_zeros_in_end():
    lst1 = [0, 1, 0, 3, 12]
    zero_list=[]
    non_zero_list=[]

    for numb in lst1:
        if numb==0:
            zero_list.append(numb)
        else:
            non_zero_list.append(numb)
    return non_zero_list+zero_list

result=move_zeros_in_end()
print(result)









