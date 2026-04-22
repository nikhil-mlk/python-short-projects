'''
Requirement:
We have to decide the maximum score first lets say 50
user will get a chance to roll the dice. (possible outcomes will be 1-6)
On every roll the value be added to the score
Note: If there will be 1 then all the score will be erased or gone and user will loose the game.
If user score reaches to maximum the game will quit with winning message

How to do?
use of Random for dice rolling
create a variable to store the score and add the score in this variable only
use of while loop for dice rolling and use another while loop to ask user if he/she wants to roll the dice again or not.
'''

import random
import sys

max_score=20
count=0
choice=''
var=True
while var:
    user_input=input('Press Enter key on your keyboard to roll the dice 🎲')
    if len(user_input)>0:
        print('Wrong key pressed')
        continue
    dice_number=random.randint(1,6) # Selecting random number from 1 to 6
    print('Number on dice is: ',dice_number)
    if dice_number!=1:
        count=count+dice_number
    else:
        count=0
        print('Sorry You loose the game.')
        break
    if count>=max_score: # Checking if user score reaches to maximum or not
        print(f'Your total count {count} reaches to maximum. You win this game!!!')
        break
    while True:
        choice = input('Want to roll the dice again? (Y or N):').lower() # Asking user if he/she wants to roll teh dice again?
        if choice == 'y':
            break
        elif choice == 'n':
            print('Your Final Score is: ', count)
            print('Thanks for playing')
            sys.exit()















