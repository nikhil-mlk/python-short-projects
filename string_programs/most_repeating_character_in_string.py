'''
Requirement: To find the most repeating character in a string and number of times it occurs.

What we need:
for loop to iterate string
dictionary to store character and its count

How we do it:
Create empty dictionary
iterate the string
On every character search that character present in dictionary or not
if not present, then add that character in dictionary as a Key and value=1
if character present in dictionary then increase the value of that character by 1

Once you have a complete dictionary with character and its count, then you can find the most repeating character by iterating the dictionary and comparing the values of each character.
'''
str='hello'
dict={}

for char in str:
    if char not in dict:
        dict.__setitem__(char,1)
    else:
        dict[char] +=1

print(dict.items())

final_ch=''
final_val=0

for ch,val in dict.items():
    if val>final_val:
        final_ch=ch
        final_val=val
print('Most Repeating Character is: ',final_ch,' and number of times it occurs: ',final_val)





