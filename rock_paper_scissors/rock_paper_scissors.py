'''
Requirements:
- User will have an option R - rock, P- paper, S- scissors
- User will play against computer, so computer will also have the same options R, P, S
- User will decide how many rounds he wants to play
- if client says more than 10 rounds, then prompt will appear that max rounds he/she can play is 10
- System again asks client Still want to play? Yes or No: If yes then again asks for the number of rounds. -----L
- if client answer is correct, then 1 point will be added
- if client answer is incorrect then no points to client
- After last round, score will be displayed along with Thank You message
'''
import random
import sys
user_counter = 0
system_counter = 0

def number_of_rounds():
    rounds = int(input('How many rounds you want to play?'))
    if rounds>10:
        print('The maximum rounds you can play are 10')
        sys.exit()
    return rounds

def user_input():
    user_choice = input('Enter your choice: R for Rock, P for Paper, S for Scissors:')
    return user_choice

def system_input():
    system_choice = random.choice(['R', 'P', 'S'])
    print('System choice is: ', system_choice)
    return system_choice

def decision():
    global user_counter
    global system_counter
    user_choice = user_input()
    system_choice = system_input()
    if (user_choice == 'R' and system_choice == 'S') or (user_choice == 'P' and system_choice == 'R') or (user_choice == 'S' and system_choice == 'P'):
        user_counter += 1
    elif (user_choice == 'R' and system_choice == 'P') or (user_choice == 'P' and system_choice == 'S') or (user_choice == 'S' and system_choice == 'R'):
        system_counter += 1
    return user_counter, system_counter

def main():
    user_count=0
    system_count=0
    rounds=number_of_rounds()
    for i in range(rounds):
        user_count,system_count=decision()
    print('User Score is: ', user_count)
    print('System Score is: ', system_count)
    if user_count>system_count:
        print('User wins with score: ',user_count)
    elif user_count<system_count:
        print('System wins with score: ',system_count)

main()
























