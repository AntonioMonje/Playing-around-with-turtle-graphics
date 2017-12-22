#!/usr/bin/env python
import turtle

turtle.title("Circles made from squares!")
turtle.screensize(2000,1500)
my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.pencolor("white")

my_turtle2 = turtle.Turtle()
my_turtle2.speed(0)
my_turtle2.pencolor("red")

my_turtle3 = turtle.Turtle()
my_turtle3.speed(0)

def square(length, angle):
    for i in range(3):
        my_turtle.forward(length)
        my_turtle.right(angle)

def square2(length, angle):
    for i in range(3):
        my_turtle2.forward(length)
        my_turtle2.right(angle)

def square3(length, angle):
    for i in range(4):
        my_turtle3.forward(length)
        my_turtle3.right(angle)

def main():

    for i in range(100):
        square3(100,90)
        my_turtle3.right(11)

    my_turtle3.clear()
    turtle.bgcolor("black")

    for i in range(100):
        square(100,30)
        my_turtle.right(11)

    my_turtle.clear()


    for i in range(100):
        square2(100, 90)
        my_turtle2.right(11)

    my_turtle2.clear()

if __name__ == '__main__':
    main()
