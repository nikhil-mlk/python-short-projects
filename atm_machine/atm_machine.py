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
from unittest import case

import openpyxl
import pandas as pd

def card_number_generator():
    card_numb=random.randint(1000000000, 9999999999)
    return card_numb

def add_customer():
    df=pd.read_excel('customer_data.xlsx')
    cust_name=input('Enter your full name:')
    while True:
        user_name=input('Enter your username:')
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
        'cardnumber':card_number
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
    choice=int(input('Press 1-->Deposit, 2-->Withdraw, 3-->Change Pin, 4-->Mini Statement, 5-->Exit'))
    match choice:
        case 1:
            deposit_money()
        case 2:
            new_pin=change_pin()



        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case _:
            pass

def deposit_money():
    deposit_money=[]
    final_deposit_total=0
    print('Denominations accepted: $5, $10, $20, $50 and $100. Max deposit allowed: $400')
    while True:
        quit=input("Press Q or q to quit. Enter any key to continue depositing money:")
        if quit=='q' or quit=='Q':
            break
        else:
            bill=int(input('Enter the denomination:'))
            if bill not in [5,10,20,50,100]:
                print('Denominations accepted: $5, $10, $20, $50 and $100. Max deposit allowed: $400')
                continue
            else:
                deposit_money.append(bill)
                final_deposit_total=sum(deposit_money)
                if final_deposit_total>400:
                    print(f'The deposit exceeds the limit of $400. Hence last bill of ${deposit_money[len(deposit_money)-1]} will not deposit')
                    deposit_money.pop(len(deposit_money)-1)
                    print('Your total deposit is: ',sum(deposit_money))

                    break
    return sum(deposit_money)

def change_pin():
    while True:
        user_pin = input('Enter new pin:')
        if not user_pin.isdigit():
            print('Pin should be 4 digit number')
        elif len(user_pin) < 4 or len(user_pin) > 4:
            print('User pin should be of 4 digits')
        else:
            break
    return user_pin








#login_into_atm()
result=deposit_money()
print(result)









def withdraw_money():
    pass
def change_pin():
    pass
def mini_statement():
    pass
def exit():
    pass