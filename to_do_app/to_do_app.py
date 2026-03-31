'''
Purpose: To Do App is a simple application that allows users to manage their tasks. Users can add, update, delete, and view their tasks in a list format.

Requirements:
Req1. System will ask user that how many task you want to enter. According to it loop will run and
user will enter tasks in LIST
Req 2. A message will display that will show all the tasks entered by user after adding all the tasks
Req 3: We continously ask user that what he wants to do: 1- Add Task, 2 - Update Task, 3 - Delete Task, 4 - View Tasks. If
user selects 5 - Exit the user should exit from this continous loop
'''
import sys
task_list=[]
def add_task():
    number_of_tasks=int(input('How many tasks you want to add:'))
    for i in range(number_of_tasks):
        task=input('Enter the task:')
        task_list.append(task)
    show_tasks()

    user_choice=0
    while user_choice != 5:
        user_choice = int(input('What you want to do next: 1- Add Task, 2 - Update Task, 3 - Delete Task, 4 - View Tasks, 5 - Exit: '))
        if user_choice == 1:
            task=input('Enter the task:')
            task_list.append(task)
        elif user_choice == 2:
            task_to_update=input('Enter the task name you want to update: ')
            if task_list.__contains__(task_to_update):
                new_task = input('Enter new task name: ')
                index = task_list.index(task_to_update)
                task_list[index] = new_task
            else:
                print('The task you want to update does not exist in the list.')
        elif user_choice == 3:
            task_to_delete=input('Enter the task name you want to delete: ')
            if task_list.__contains__(task_to_delete):
                task_list.remove(task_to_delete)
            else:
                print('The task you want to delete does not exist in the list.')
        elif user_choice == 4:
                show_tasks()
        elif user_choice == 5:
                print('Thank You for using To Do App. Have a good day !!!')
                sys.exit()
        else:
            print('Invalid choice. Please select a valid option.')


def show_tasks():
    print('Your tasks are: ')
    for task in task_list:
        print(task)


add_task()