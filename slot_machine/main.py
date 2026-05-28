'''
Requirements:
Ask user to deposit the money in order to play the game (value should be from $10-$100)
Ask user how many pay spins he/she wants (value should be between 1-5)
Ask user before the spin that how much he wants to bet on spin (Minimum betting amount is $2)

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
import keyboard

MAX_LINES=5
CASINO_MONEY=0
PLAYER_DEPOSIT=0
BET_AMOUNT=0
MAX_SPIN=0

def player_deposit():
    global PLAYER_DEPOSIT
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

def casino_money():
    return CASINO_MONEY

# def pay_lines():
#     global MAX_LINES
#     global MAX_SPIN
#     while True:
#         number_of_lines = input(f'How many lines you want to play? (1-{MAX_LINES}):')
#         if number_of_lines.isdigit:
#             lines=int(number_of_lines)
#             if lines>=1 and lines<=MAX_LINES:
#                 MAX_SPIN=lines
#                 break
#             else:
#                 print('Number of lines should be between 1-5.')
#         else:
#             print('Please enter a digit ')
#     return MAX_SPIN

def betting_amount():
    global BET_AMOUNT
    global PLAYER_DEPOSIT
    global CASINO_MONEY
    while True:
        amount = input('Enter the betting amount for your spin: ')
        if amount.isdigit():
            amount = int(amount)
            BET_AMOUNT = amount
            if BET_AMOUNT>PLAYER_DEPOSIT:
                print(f'Your account balance is : ${PLAYER_DEPOSIT}. Your betting amount should not exceed your balance.')
            elif BET_AMOUNT==PLAYER_DEPOSIT:
                print(f'Your account balance is : ${PLAYER_DEPOSIT}. Your betting amount should at least $1 less than your balance.')
            elif BET_AMOUNT==1:
                print('Betting amount should be at least $2.')
            else:
                PLAYER_DEPOSIT-=1
                CASINO_MONEY+=1
                return BET_AMOUNT
        else:
            print('Please enter digit')

def spin():
    global PLAYER_DEPOSIT
    global CASINO_MONEY
    global BET_AMOUNT
    spin_result=[]
    symbols=['🍒','🍋','🔔','⭐','💎','7️⃣']
    dict_of_combinations={
        ('🍒','🍒','🍒'):3,
        ('🍋', '🍋', '🍋'):4,
        ('🔔', '🔔', '🔔'):5,
        ('⭐', '⭐', '⭐'):6,
        ('💎', '💎', '💎'):10,
        ('7️⃣', '7️⃣', '7️⃣'):20
    }
    while True:
        user=input("Want to spin? (Press Enter to continue and 'q' to exit)")
        if user=='':
            if PLAYER_DEPOSIT>=10:
                betting_amount()
                for i in range(3):
                    spin_result.append(random.choice(symbols))
                spin_tuple = tuple(spin_result)

                print(spin_tuple)

                # Calculation Logic
                # If all items are same
                if spin_tuple in dict_of_combinations:
                    value = dict_of_combinations.get(spin_tuple)
                    print(f'🏆 Congratulations! Your betting amount is going to {value}X 🏆')
                    PLAYER_DEPOSIT = PLAYER_DEPOSIT + (BET_AMOUNT * value)
                    print(f'💰 Your Deposit Balance is: ${PLAYER_DEPOSIT}')

                # If 2 items match
                elif (spin_tuple[0] == spin_tuple[1]) or (spin_tuple[1] == spin_tuple[2]) or (
                        spin_tuple[0] == spin_tuple[2]):
                    print('🏆 Congratulations! Your betting amount is going to 2X 🏆')
                    PLAYER_DEPOSIT = PLAYER_DEPOSIT + (BET_AMOUNT * 2)
                    print(f'💰 Your Deposit Balance is: ${PLAYER_DEPOSIT}')

                # No items match
                else:
                    print('Sorry no luck this time. 😢')
                    PLAYER_DEPOSIT = PLAYER_DEPOSIT - BET_AMOUNT
                    print(f'💰 Your Deposit Balance is: ${PLAYER_DEPOSIT}')
                spin_result.clear()
            else:
                print(f'Your deposit balance is {PLAYER_DEPOSIT}, which is low. You can not spin')
                break
        elif user.lower()=='q':
            if PLAYER_DEPOSIT>0:
                print(f'Your total deposit is: {PLAYER_DEPOSIT}. Please proceed to the main counter to encash your money')
                break
            else:
                print('You do not have money to encash. Thank you for playing. Have a good day!')
                break
        else:
            print('Press Valid Key')

def main():
    deposit_money=player_deposit()
    print('Deposit money: $',deposit_money)

    spin()

    print('Casino Amount: ',CASINO_MONEY)


main()















