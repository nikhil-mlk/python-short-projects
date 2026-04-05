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


str1=('I love programming very much')
str2=' ...'
n=14
k=n-4
j=0

str3=str1[0:k]  # k = 10
print(str3)



if str3[k-2]!=' ' or str3[k-2]!='':
    j=k-1
    f=0

    while str3[j]!=' ':
        if str3[j]==' ':
            f=j
            break
        j=j-1
    print(f)











