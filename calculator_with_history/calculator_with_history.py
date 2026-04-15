'''
Requirements: Create a calculator that accepts expressions from user and save them in txt file
1. User will enter FULL expression like 5+8 or 5*7
2. In text file the expression will save  like this: 5+8=13 and so on...
3. User will get following options every time:
- Enter Expression --> This allows user to enter the expression
- History --> This will display the history in text file >> [If there is no history then it will show message like "No history found"]
- Clear --> This will delete/erase the history in text file >> [if there is no history then it will show message like "Nothing to clear"]]
- Exit --> This will exit the program
4. The program will continue asking the user until user will not say Exit

Imp: As of now we are only dealing with 2 numbers in expression

Things to use:
- Create .txt file
- while loop until user selects to Exit the system

Pseudo Code:
while loop until user selects to Exit the system
if user selects Enter Expression:
    ask user to enter the expression
    evaluate the expression
    save the expression with result in text file
if user selects History:
    read the text file and display the history
if user selects Clear:
    clear the content of text file
if user selects Exit:
    exit the system
'''
import sys
def enter_expression():
    result=0
    user_expression=input("Enter expression: ")
    if len(user_expression)>3 or len(user_expression)<3:
        print('Invalid Expression. Please enter expression in format: number operator number (e.g. 5+8)')


    operator = user_expression[1]
    lst1=user_expression.split(operator)
    first_digit=int(lst1[0])
    last_digit=int(lst1[-1])

    match operator:
        case '+':
            result=first_digit+last_digit
        case '-':
            result=first_digit-last_digit
        case '*':
            result=first_digit*last_digit
        case '/':
            if last_digit == 0:
                print('The number cannot be divided by zero')
                return  # stop execution, don't proceed further
            else:
                result = first_digit / last_digit

    final_expression=user_expression+'='+str(result)
    # Add Expression to file
    with open('calculator.txt','a') as f:
        f.write(final_expression+'\n')
    return final_expression

def add_expression_to_file():
    with open('calculator.txt','a') as f:
        f.write(enter_expression()+'\n')
def view_history():
    with open('calculator.txt','r') as f:
        data=f.read()
        if len(data)!=0:
            print('Your History:')
            print(data)
        else:
            print("No history found")

def clear_history():
    with open('calculator.txt','r') as f:
        data=f.read()
        if len(data)!=0:
            with open('calculator.txt','w') as f:
                pass
            print('History cleared')
        else:
            print("No history found")

def exit_system():
    print('*** Thank You for using this Application ***')
    sys.exit()

while True:
    choice=input('Choose your options: 1 -> Enter Expression 2 -> View History 3 -> Clear History 4 -> Exit')
    match choice:
        case '1':
            enter_expression()
            #add_expression_to_file()
        case '2':
            view_history()
        case '3':
            clear_history()
        case '4':
            exit_system()



