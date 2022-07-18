#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle

t = turtle.Turtle()

t.speed(1)
t.penup()
t.right(90)
t.forward(100)
t.left(90)
t.pendown()

t.circle(100)
t.circle(100,180)
t.right(180)
t.circle(70)
#t.circle(-100,90)
t.penup()
t.setpos(100,0)
t.pendown()
t.left(45)
t.fd(150)
t.bk(20)
t.left(45)
t.fd(20)
t.bk(20)
t.right(90)
t.fd(20)
t.bk(20)

t.left(180)
t.penup()
t.setpos(-100,0)
t.pendown()
t.right(45)
t.fd(150)
t.bk(20)
t.left(45)
t.fd(20)
t.bk(20)
t.right(90)
t.fd(20)
t.bk(20)

t.right(90)
t.penup()
t.setpos(20,195)
t.pendown()
t.left(45)
t.fd(20)
t.right(90)
t.fd(20)

t.right(135)
t.penup()
t.setpos(-20,195)
t.pendown()
t.right(45)
t.fd(20)
t.left(90)
t.fd(20)

t.left(135)
t.right(45)
t.penup()
t.setpos(-35,140)
t.pendown()
t.circle(50,90)




t.hideturtle()

turtle.done()

