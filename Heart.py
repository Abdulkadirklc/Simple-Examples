import turtle

t = turtle.Turtle()
t.speed(1)


# Kalp çizimi
turtle.penup()
turtle.goto(0, -250)
turtle.pendown()
turtle.begin_fill()
turtle.color('red')
turtle.pensize(5)
turtle.left(45)
turtle.forward(360)
turtle.circle(180, 180)
turtle.right(90)
turtle.circle(180, 180)
turtle.forward(360)
turtle.end_fill()

# Yazı yazma
turtle.penup()
turtle.goto(0, 20)
turtle.color('white')
turtle.write("Bunu sevdiğiniz \n kişiye gönderin!", align='center', font=('Arial', 40, 'bold'))

turtle.done()
