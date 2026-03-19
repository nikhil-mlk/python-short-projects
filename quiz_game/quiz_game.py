'''
- There will be set of questions (Max 10 questions are in system right now). The system will present questions one by one in from of client.
- User will decide how many questions he wants to play
- if client says more than 10 questions, then prompt will appear that max questions he/she can play is 10
- System again asks client Still want to play? Yes or No: If yes then again asks for the number of questions.
- if client answer that question correctly, then 1 point will be added AND that question will remove from the list, so that it should not appear again
- if client answer is incorrect then no points to client AND the question will remove from list
- After last question, score will be displayed along with Thank You message
'''
'''
Steps to follow:
List to store the questions with answers  --> dictionary
For random selection, choose random library
For existing the system (in case user does not want to proceed) use sys library
'''
import random
import sys
questions={
    'Capital Of India':'Delhi',
    'National bird of India':'Peacock',
    'National animal of India':'Tiger',
    'National game of India':'Hockey',
    'In which continent India is located':'Asia',
    'National language of India':'Hindi',
    'Best computer language':'Python',
    'In which city there is Taj Mahal in India ':'Agra',
    'Prime Minister of India':'Modi',
    'Capital of Punjab':'Chandigarh'
}
list_of_questions = list(questions.keys())
def ask_me_questions():
    decision=''
    number_of_questions=int(input('How many questions you want to play: '))
    while number_of_questions>10:
        print('The maximum number of questions you can play is 10')
        decision = input('Still want to play? Yes or No: ')
        if decision == 'Yes':
            number_of_questions = int(input('How many questions you want to play: '))
        else:
            print('Bye and have a good day !!!')
            sys.exit()
    count=0
    for i in range(number_of_questions):
        question=random.choice(list_of_questions)
        print(question)
        answer=input('Type your answer:')
        if questions.get(question)==answer:
            count=count+1
        list_of_questions.remove(question)
    print('***** Thank you for your participation *****')
    print('Your Total Score is: ',count)


ask_me_questions()












