'''
Requirement:
We need to find the longest word in a string
string = python programming is fun

Ans: programming --> length: 11

What we need:
for loop to iterate string
dictionary to store string and its length

How to do:
split the string --> it will turn into List
iterate the list
In dictionary, key=string value and value=size
loop over the dictionary to find the max value
'''

str='python programming is fun'
lst=str.split()

dict={}

for word in lst:
    length=len(word)
    dict.__setitem__(word,length)

print(dict.items())
size=0
str2=''
for key,value in dict.items():
    if value>size:
        size=value
        str2=key
print(str2,':',size)





