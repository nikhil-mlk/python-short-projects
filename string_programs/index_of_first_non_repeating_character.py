'''
Req: Find the index of First Non-Repeating Character in String

Ex: String: swiss
s occurs more than 1 time
w occurs 1 time
i occurs 1 time
But w occurs first and its index is 1.
so answer is 1
'''

str='swiss'
for i in range(len(str)):
    for j in range(i+1, len(str)):
        if str[j]==str[i]:
            break
    else:
        print('The character: ',str[i],' is first non repeating character in the string with index: ',i)
        break




