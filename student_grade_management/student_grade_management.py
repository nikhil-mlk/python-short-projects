'''
Objective: Create a student grade management system that allows users to Add, View, Delete and Update grades for students.
Requirements:
The name and marks entered by the user will save in a dictionary with the name as key and marks as value.
The system should have the following functionalities:
1. Add Grade: Allow the user to add a student's name and their corresponding grade.
2. View Grades: Display grades of a Specific student in a readable format.
3. View All Grades: Display all students and their grades in a readable format.
4. Delete Grade: Allow the user to delete a student's grade by entering their name.
5. Update Grade: Allow the user to update a student's grade by entering their name and the new grade.
6. Exit: Allow the user to exit the program.
'''

import sys
student_grades={}
def add_grade():
    student_name=input('Enter the name of the student: ')
    grade=int(input('Enter the grade of the student: '))
    student_grades.__setitem__(student_name,grade)
def view_grade():
    student_name=input('Enter the name of the student to view grade: ')
    if record_exists(student_name):
        print(student_grades.get(student_name))
    else:
        print('Student name not found in the records.')
def view_all_grades():
    if len(student_grades)==0:
        print('No Records Found. Please add the records first.')
    all_records=student_grades.keys()
    for i in all_records:
        print(i,':',student_grades[i])
def delete_record():
    student_name=input('Enter the name of the student to delete grade: ')
    if record_exists(student_name):
        student_grades.pop(student_name)
        print(f'The record of {student_name} has been deleted.')
    else:
        print(f'Student Name {student_name} not found in the records. Please enter the valid name.')
def update_grade():
    student_name=input('Enter the name of the student to update grade: ')
    if record_exists(student_name):
        updated_marks = int(input('Enter the marks to update: '))
        student_grades[student_name] = updated_marks
        print(f'The record of {student_name} has been updated successfully.')
    else:
        print(f'Student Name {student_name} not found in the records. Please enter the valid name.')
def record_exists(student_name):
    data=student_grades.keys()
    if student_name in data:
        return True
    else:
        return False
def main():
    print('***** Welcome to Student Grade Management System *****')
    print('Press 1 to Add Grade')
    print('Press 2 to View Grade')
    print('Press 3 to View All Grades')
    print('Press 4 to Delete Grade')
    print('Press 5 to Update Grade')
    print('Press 6 to Exit')
    actions={
        1:add_grade,
        2:view_grade,
        3:view_all_grades,
        4:delete_record,
        5:update_grade,
        6:sys.exit
    }
    while True:
        choice=int(input('Enter your choice: '))
        action = actions.get(choice)
        if action:
            action()
        else:
            print('Invalid Choice. Please enter the valid choice.')


main()