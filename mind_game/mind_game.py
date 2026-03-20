'''
Requirement:
1. There is a pre-defined pattern of 5 colors, like: [B,O,G,Y,R]. This pattern is not visible to user
2. Now user will get 10 chances to guess the pattern
3. In every chance, user will get the result like: 2 patterns match | 3 patterns donot match
4. Ex: user Enters: [G,O,B,Y,R] --> in this pattern Y and R at the correct place in the predefined pattern, hence 2 patterns match and 3 don't.
5. Program will show to user that at which try (1,2,3,4,5,6...10), he/she finds the correct pattern.
6. If after 10 tries pattern not match then Bye message should appear.
'''

list_of_colors=('B','O','G','Y','R')

def enter_pattern(*pattern):
        print('Enter the pattern: ')
        client_tuple=tuple(input(pattern))
        return client_tuple


def pattern_comparison():
    i=0
    while i<=9:
        tup=enter_pattern()
        if tup==list_of_colors:
            print(f'You have successfully guess the pattern {tup} at {i} time')
            break;
        else:
            pass




















