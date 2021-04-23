import turtle as t
t.Screen()
t.speed(0)
t.pensize(3)

def shape(size, sides):
    for i in range(sides):
        t.forward(size)
        t.left(360/sides)

for j in range(18):
    for i in range(8):
        for colours in ['violet' , 'indigo' , 'blue' , 'green' , 'pink' , 'red' , 'yellow']:
            t.color(colours)
            shape(20,4)
            t.forward(10)
            t.left(5)
    t.penup()
    t.forward(20)
    t.right(180)
    t.pendown()
t.exitonclick()


























