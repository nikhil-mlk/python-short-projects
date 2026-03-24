import random

board_user=['1','2','3','4','5','6','7','8','9']
board_comp=['1','2','3','4','5','6','7','8','9']

def display_board():
    print(f' {board_user[0]} | {board_user[1]} | {board_user[2]}')
    print(' ---------')
    print(f' {board_user[3]} | {board_user[4]} | {board_user[5]}')
    print(' ---------')
    print(f' {board_user[6]} | {board_user[7]} | {board_user[8]}')

def board_full():
    pass
def check_winner():
    if(
    (board_user[0] and board_user[1] and board_user[2])=='X' or
    (board_user[3] and board_user[4] and board_user[5])=='X' or
    (board_user[6] and board_user[7] and board_user[8])=='X' or
    (board_user[0] and board_user[3] and board_user[6])=='X' or
    (board_user[1] and board_user[4] and board_user[7])=='X' or
    (board_user[2] and board_user[5] and board_user[8])=='X' or
    (board_user[0] and board_user[4] and board_user[8])=='X' or
    (board_user[2] and board_user[4] and board_user[6])=='X'):
        print('User wins the game !!!!!!')
        return True
    elif(
    (board_user[0] and board_user[1] and board_user[2])=='O' or
    (board_user[3] and board_user[4] and board_user[5])=='O' or
    (board_user[6] and board_user[7] and board_user[8])=='O' or
    (board_user[0] and board_user[3] and board_user[6])=='O' or
    (board_user[1] and board_user[4] and board_user[7])=='O' or
    (board_user[2] and board_user[5] and board_user[8])=='O' or
    (board_user[0] and board_user[4] and board_user[8])=='O' or
    (board_user[2] and board_user[4] and board_user[6])=='O'):
        print('Computer wins the game !!!!!!')
        return True

def user_input():
    choice=input('Enter your choice:')
    get_index=board_user.index(choice)
    board_user[get_index]='X'
    board_comp.remove(choice)

def system_input():
    comp_choice=random.choice(board_comp)
    get_index=board_comp.index(comp_choice)
    board_user[get_index] = 'O'
    board_comp.remove(comp_choice)

def main():
    i=0
    while(i<9):
        display_board()
        result=check_winner()
        if result:
            break
        user_input()
        system_input()
        i+=1
        display_board()

main()

