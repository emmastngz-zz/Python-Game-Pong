# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 23:43:36 2020

@author: Emmanuel
"""

import turtle as t

window = t.Screen()

window.title("Pong game")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

# Paddle A
paddle_a = t.Turtle()
paddle_a.speed(0) # animation speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = t.Turtle()
paddle_b.speed(0) # animation speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = t.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)


# Main game loop
while True:
    window.update()
    




