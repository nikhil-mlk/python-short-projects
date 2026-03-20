'''
Requirement:
1. There is a pre-defined pattern of 5 colors, like: [B,O,G,Y,R]. This pattern is not visible to user
2. Now user will get 5 chances to guess the pattern
3. In every chance, user will get the result like: 2 patterns match | 3 patterns donot match
4. Ex: user Enters: [G,O,B,Y,R] --> in this pattern Y and R at the correct place in the predefined pattern, hence 2 patterns match and 3 don't.
5. Program will show to user that at which try (1,2,3,4,5,6...10), he/she finds the correct pattern.
6. If after 10 tries pattern not match then Bye message should appear.
'''
default_colors_pattern=['B','O','G','Y','R']

def enter_pattern():
    client_pattern=[]
    matching_position=0
    unmatching_position=0
    k=1
    while k<=5:
        client_pattern = input('Enter the pattern: ').split()
        if default_colors_pattern == client_pattern:
            print(f'Your pattern {client_pattern} matched at {k} point')
            break
        else:
            for a, b in zip(default_colors_pattern, client_pattern):
                if a == b:
                    matching_position += 1
                else:
                    unmatching_position += 1
            print(f'Correct Position(s): {matching_position} | Incorrect Position(s): {unmatching_position}')
            client_pattern.clear()
            matching_position, unmatching_position = 0, 0
        k+=1
        if k>5:
            print('Your attempts are Over')

enter_pattern()






























