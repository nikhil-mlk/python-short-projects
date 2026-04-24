'''
Requirement:
Move all Zero elements to the end while maintaining the relative order of elements.
suppose we have [0,1,0,3,12]
Output: [1,3,12,0,0]
'''



def move_zeros_in_end():
    lst1=[0,1,0,3,12]
    lst2=[]

    for i in lst1:
        if i==0:
            lst2.append(i)
            lst1.remove(i)
    lst1.extend(lst2)
    return lst1

result=move_zeros_in_end()
print(result)