#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle
t = turtle.Turtle()

for i in range(2):
    t.forward(250)
    t.left(90)
    t.forward(150)
    t.left(90)
t.fillcolor("red")
t.begin_fill()
for i in range(2):
    t.forward(250)
    t.left(90)
    t.forward(75)
    t.left(90)
t.end_fill()
t.penup()
t.left(90)
t.forward(75)
t.right(90)
t.fillcolor("blue")
t.begin_fill()
for i in range(2):
    t.forward(83)
    t.left(90)
    t.forward(75)
    t.left(90)
t.end_fill()
t.penup()
t.forward(25)
t.left(90)
t.forward(16)
t.right(90)
t.pendown()
t.left(36)
t.fillcolor("white")
t.begin_fill()
for i in range(5):
    t.forward(20)
    t.right(72)
    t.forward(20)
    t.left(144)
t.end_fill()

turtle.done()


# In[ ]:


#for i in range(37):
   # t.forward(250)
   # t.left(90)
   # t.forward(1)
   # t.left(90)
   # t.forward(250)
   # t.right(90)
   # t.forward(1)
   # t.right(90)


# In[ ]:




