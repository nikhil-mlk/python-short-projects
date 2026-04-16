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

var=True
while j<len(user_string) and i<len(user_string):
    if j==len(user_string)-1:
        if user_string[j-1]!=user_string[j]:
            final_str=final_str+user_string[j]+'1'
            break
        else:
            pass





    j+=1
    if user_string[j]==user_string[i]:
        k+=1
    elif user_string[j]!=user_string[i]:
        final_str=final_str+user_string[i]+str(k)
        k=1
        i=j

print(final_str)













