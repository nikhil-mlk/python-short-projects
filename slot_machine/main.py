'''
Requirements:
Ask user to deposit the money in order to play the game (value should be from $10-$100)
Ask user how many pay spins he/she wants (value should be between 1-5)
Ask user before the spin that how much he wants to bet on spin

Imp: On every spin $1 will be credited to Casino (irrespective user win or not)

Note:
Suppose user deposit $10 and he wants 3 spins. Before 1st spin he bets $5 and he looses the spin.
Now $1 is already deducted (for Casino). Now he has a balance of $4.
On second spin he bets $5, which is NOT possible.
Here we need to track this balance and if user tries to bet more than his balance, then prompt will appear that you have only $4 balance, please bet accordingly.

Weighs:
    🍒: 3
    🍋: 4
    🔔: 5
    ⭐: 6
    💎: 10
    7️⃣: 20

Combinations:
if  🍒 🍒 🍒 ---> bet amount * 3
if  🍋 🍋 🔔 ---> bet amount * 4
if  🔔 🔔 🔔 ---> bet amount * 5
if  ⭐ ⭐ ⭐ ---> bet amount * 6
if  💎 💎 💎 ---> bet amount * 10
if  7️⃣ 7️⃣ 7️⃣ ---> bet amount * 20

Special:
if all symbols are different then NO Win Ex: 🍒 🍋 ⭐
if 2 symbols are same then 2x points Ex: 🍒 🍒 ⭐

'''
import random

MAX_LINES=5
CASINO_MONEY=0
PLAYER_DEPOSIT=0
BET_AMOUNT=0
MAX_SPIN=0

def player_deposit():
    while True:
        amount = input('Enter the amount you want to deposit ($): ')
        if amount.isdigit():
            deposit=int(amount)
            if deposit>=10 and deposit <=100:
                PLAYER_DEPOSIT=deposit
                break
            else:
                print('Deposit must be between $10-$100.')
        else:
            print('Please enter a number.')
    return PLAYER_DEPOSIT

def pay_lines():
    while True:
        number_of_lines = input(f'How many lines you want to play? (1-{MAX_LINES}):')
        if number_of_lines.isdigit:
            lines=int(number_of_lines)
            if lines>=1 and lines<=MAX_LINES:
                MAX_SPIN=lines
                break
            else:
                print('Number of lines should be between 1-5.')
        else:
            print('Please enter a digit ')
    return MAX_SPIN

def betting_amount():
    while True:
        amount = input('Enter the betting amount for your spin: ')
        if amount.isdigit():
            amount = int(amount)
            BET_AMOUNT = amount
            if BET_AMOUNT>PLAYER_DEPOSIT:
                print(f'Your account balance is : ${PLAYER_DEPOSIT}. Your betting amount should not exceed your balance.')
            elif BET_AMOUNT==PLAYER_DEPOSIT:
                print(f'Your account balance is : ${PLAYER_DEPOSIT}. Your betting amount should at least $1 less than your balance.')
            elif PLAYER_DEPOSIT==0: # Might be removed
                print('Your account balance is : $0. You are not allowed to spin.')
                break
            else:
                return BET_AMOUNT
        else:
            print('Please enter digit')



# def spin():
#     spin_list=[]
#     symbols=['🍒','🔔','💎','🍋','🍊','⭐','7️⃣']
#     for i in rBET_AMOUNTange(2):
#         random_symbol = random.choice(symbols)
#         spin_list.append(random_symbol)
#     print(spin_list)
#     return spin_list





def main():
    deposit_money=player_deposit()
    print('Deposit money: $',deposit_money)

    number_of_spins=pay_lines()
    print('Number of spins', number_of_spins)


    bet_amount=betting_amount()
    print('Bet Amount: $', bet_amount)


main()















