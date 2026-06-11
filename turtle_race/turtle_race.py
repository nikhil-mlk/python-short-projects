import turtle
import time

WIDTH, HEIGHT = 500,500
def get_number_of_racers():
    while True:
        racers=input('Enter the number of racers (2-10): ')
        if racers.isdigit():
            no_of_racers=int(racers)
            if no_of_racers>=2 and no_of_racers<=10:
                break
            else:
                print('Please enter the number of racers between 2-10: ')
        else:
            print('Please enter the number. Try again...!!!')
    return no_of_racers

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')


racers=get_number_of_racers()
init_turtle()

turtle1=turtle.Turtle()
turtle1.shape('turtle')
turtle1.color('red')
turtle1.penup()

turtle1.speed(1)
turtle1.forward(100)
turtle1.left(90)
turtle1.forward(100)
turtle1.left(90)
turtle1.forward(100)
time.sleep(5)
