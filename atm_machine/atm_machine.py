'''
Objective
Create ATM system where user can intract with accounts

Main Modules:
1. Add Customer
2. Deposit Money
3. Withdraw Money
4. Change pin
5. Mini Statement
6. Exit

Add Customer:
- ask Name
- ask username (unique)
- ask pin
- Deposit initial money
- Account Number should be created

Deposit Money:
- amount should be > 0
- balance should be update

Withdraw Money:
- Amount > 0
- Sufficient balance should present in account

Change Pin:
Pin should be updated in Excel

Mini Statement:
Record every transaction
Deposited $2000
Withdrawn $1000
Deposited $500

Exit:
Exit the system
'''
import random
import pandas as pd
import sys

user_name=''

def card_number_generator():
    card_numb=random.randint(1000000000, 9999999999)
    return card_numb

def add_customer():
    df=pd.read_excel('customer_data.xlsx')
    cust_name=input('Enter your full name:')
    while True:
        global user_name
        user_name = input('Enter your username:')
        if user_name in df['username'].values:
            print('username already exists')
        else:
            break

    while True:
        user_pin=input('Enter your pin:')
        if not user_pin.isdigit():
            print('Pin should be 4 digit number')
        elif len(user_pin)<4 or len(user_pin)>4:
            print('User pin should be of 4 digits')
        else:
            break

    # Generating card number for customer
    card_number=card_number_generator()

    # Adding record in Excel sheet
    new_customer={
        'Name':cust_name,
        'username':user_name,
        'pin':user_pin,
        'cardnumber':card_number,
        'deposit':0,
        'withdraw':0
    }
    df.loc[len(df)]=new_customer
    df.to_excel('customer_data.xlsx', index=False)

def login_into_atm():
    print('Welcome to ATM')
    df=pd.read_excel('customer_data.xlsx')
    while True:
        user_name = input('Enter the username:')
        if user_name not in df['username'].values:
            print('User Name does not exist. Please enter the correct user name')
            continue

        cust_pin = input('Enter your pin:')

        # Extracting the value of pin from data frame
        actual_pin=str(df.loc[df['username']==user_name,'pin'].iloc[0])

        if actual_pin == cust_pin:
            print('Access Granted. Login Successful')
            break
        else:
            print('Pin does not exist match')
            continue

    # Ask user what they want
    choice=int(input('Press 1-->Deposit, 2-->Withdraw, 3-->Change Pin, 4-->Check Balance, 5-->Exit'))
    match choice:
        case 1:
            deposit_amount = deposit_money(user_name)
            df.loc[df['username'] == user_name, 'deposit'] = deposit_amount
            df.to_excel('customer_data.xlsx', index=False)
        case 2:
            withdraw_money(user_name)
        case 3:
            new_pin = change_pin()
            df.loc[df['username'] == user_name, 'pin'] = new_pin
            df.to_excel('customer_data.xlsx', index=False)
            pass
        case 4:
            print(f'Your total balance is:${df.loc[df['username'] == user_name, 'deposit'].iloc[0]}')
        case 5:
            print('Thank You for using ATM')
            sys.exit()
        case _:
            pass

def deposit_money(user_name):
    df=pd.read_excel('customer_data.xlsx')
    existing_deposit=df.loc[df['username']==user_name,'deposit'].iloc[0]
    deposit_money_list=[]
    final_deposit_total=0
    print('Denominations accepted: $5, $10, $20, $50 and $100. Max deposit allowed: $400')
    while True:
        quit=input("Press Q or q to quit. Enter any key to continue depositing money:")
        if quit=='q' or quit=='Q':
            print('You deposited $',sum(deposit_money_list))
            print('Your total deposit amount is: $',existing_deposit + sum(deposit_money_list))
            break
        else:
            bill=int(input('Enter the denomination:'))
            if bill not in [5,10,20,50,100]:
                print('Denominations accepted: $5, $10, $20, $50 and $100. Max deposit allowed: $400')
                continue
            else:
                deposit_money_list.append(bill)
                final_deposit_total=sum(deposit_money_list)
                if final_deposit_total>400:
                    print(f'The deposit exceeds the limit of $400. Hence last bill of ${deposit_money_list[len(deposit_money_list)-1]} will not deposit')
                    deposit_money_list.pop(len(deposit_money_list)-1)
                    print('You deposited $',sum(deposit_money_list))
                    print('Your total deposit amount is: $',existing_deposit+sum(deposit_money_list))
                    break
    return existing_deposit+sum(deposit_money_list)

def withdraw_money(user_name):
    df = pd.read_excel('customer_data.xlsx')
    existing_deposit = df.loc[df['username'] == user_name, 'deposit'].iloc[0]
    if existing_deposit<50:
        print(f'You have ${existing_deposit} in account. You need to maintain min $50 in your account. Hence no with drawl')
    else:
        while True:
            quit = input("Press Q or q to quit. Enter any key to continue With drawl money:")
            if quit == 'q' or quit == 'Q':
                break
            else:
                withdraw_amount = int(input('Enter the amount you want to with draw:'))
                if not withdraw_amount%5==0:
                    print('Withdraw amount must be an multiple of 5')
                    continue
                elif existing_deposit-withdraw_amount<50:
                    print(f'The withdraw amount of ${withdraw_amount} is making your total deposit less than $50. Hence no with drawl. Choose another amount.')
                    continue
                else:
                    print(f'Please collect you cash of ${withdraw_amount}.')

                    # Currency logic
                    # final_currency=[]
                    # list_of_currency=[5,10,20,50,100]
                    # for i in list_of_currency:
                    #     if i>withdraw_amount:
                    #         list_of_currency.remove(i)
                    # while True:
                    #     final_currency.append(random.choice(list_of_currency))
                    #     if sum(final_currency)==withdraw_amount:
                    #         print(f'List: ${final_currency}')
                    #         break
                    df.loc[df['username'] == user_name, 'deposit']=existing_deposit-withdraw_amount
                    df.to_excel('customer_data.xlsx', index=False)
                    print(f'your total balance is now:${df.loc[df['username'] == user_name, 'deposit'].iloc[0]}')
                    break

def change_pin():
    while True:
        user_pin=input('Enter new pin:')
        if not user_pin.isdigit():
            print('Pin should be 4 digit number')
        elif len(user_pin) < 4 or len(user_pin) > 4:
            print('User pin should be of 4 digits')
        else:
            new_pin=int(user_pin)
            print('Pin Updated Successfully')
            break
    return new_pin



login_into_atm()










