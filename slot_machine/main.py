'''
Requirements:
Ask user to deposit the money in order to play the game (value should be from $10-$100)
Ask user how many pay lines he/she wants to play (value should be between 1-5)
Note:
All lines are already designed (like cherry, diamond, etc)
Each line costs $1

Money Decision:
Balance = $10
Player chooses:
5 paylines
$1 per line
Total Bet=Lines×Bet Per Line
So:
5×1=5
Meaning:
One spin costs $5
'''
MAX_LINES=5

def deposit():
    while True:
        amount = input('Enter the amount you want to deposit ($): ')
        if amount.isdigit():
            amount=int(amount)
            if amount>=10 and amount <=100:
                break
            else:
                print('Amount must be between $10-$100.')
        else:
            print('Please enter a number.')
    return amount

def pay_lines():
    while True:
        number_of_lines = input(f'How many lines you want to play? (1-{MAX_LINES}):')
        if number_of_lines.isdigit:
            lines=int(number_of_lines)
            if lines>=1 and lines<=MAX_LINES:
                break
            else:
                print('Number of lines should be between 1-5.')
        else:
            print('Please enter a digit ')
    return lines

def sloth_styles():
    styles={
        1:'🍒 🍒 🍒',
        2:'🔔 🔔 🔔',
        3:'💎 💎 💎',
        4:'🍋 🍒 💎',
        5:'🍋 🍋 🍋',
        6:'🍋 🍒 🍋',
        7:'💎 🍒 🔔',

    }







def main():
    # amount=deposit()
    # print(amount)

    lines=pay_lines()
    print(lines)






main()





