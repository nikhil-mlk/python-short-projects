'''
Input: "aaabbca"
Break it into consecutive groups:
"aaa" → a3
"bb" → b2
"c" → c1
"a" → a1 (this is separate from the first a group!)

Output: "a3b2c1a1"

Idea:
iterate string and place characters in dictionary along with their values (number of time occurence)

'''
user_string='aaabbcc'
final_str=''
i=0
j=0
k=1
while j<len(user_string):

    j += 1

    if user_string[j] == user_string[i]:
        k += 1
    elif user_string[j]!=user_string[i]:
        final_str=final_str+user_string[i]+str(k)
        i=j
        k=1
print(final_str)











