'''
Requirements:
1. Firstly user hase to create an account with master password
2. Entry will be stored in dictionary as a DB where key = username and value = password (master password)
3. After successful creation of account, user can add the password for different websites with username and password of that website
4. These entries will store in the separate file.
    Here, separate text file will be created with the name as username
Note: For each username separate file will be created with the name of username and all the entries of that user will be stored in that file.
5. System will check if there is a duplicate entry in the dictionary or not.
6. System will provide text like --> add new username and password || view your passwords || Exit the system. According to the choice user will get response.


Things left:
Working On:
for choice 2: Need to check if file is empty then return message if nothing in file
handle the situation where user coming for the first time and instead of adding credentials he/she try to view file
'''

master_record={}
def master_user_registration():
    user_name=input('Enter master username: ')
    if user_name in master_record.keys():
        print('Username already exists. Please try with different username.')
        master_user_registration()
    else:
        user_password = input('Enter master password: ')
        master_record.__setitem__(user_name,user_password)
        print('Username and password successfully registered.')

def validate_user_and_create_file():
    user=input('Enter Master username: ')
    if user not in master_record.keys():
        print('Invalid username')
        validate_user_and_create_file()
    else:
        password = input('Enter Master password: ')
        master_pass=master_record.get(user)
        if master_pass!=password:
            print('Invalid password')
            validate_user_and_create_file()
        else:
            print('Access Granted !!!!')
            print('Now You can start storing your credentials')
    while True:
        choice=input('Do you want to add New Credentials or want to quit? --> 1->  Add Credentials and 2->: View Credentials and 3-> Exit: ')
        if choice=='1':
            user_n = input('Enter new User Name: ')
            user_p = input('Enter new password: ')
            with open(user+'.txt','a') as f:
                f.write(user_n+' | '+user_p+'\n')
        elif choice=='2':
            pass
        elif choice=='3':
            print('--- Thank you for choosing Password Management application -----')
            break










