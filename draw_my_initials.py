import turtle

def draw_my_initials():    
    mywindow = turtle.Screen()
    mywindow.bgcolor("lightblue")
    az = turtle.Turtle()
    az.speed(2) 
    az.shape("turtle")
    az.color("blue")
    az.left(70)
    az.forward(200)
    az.right(140)
    az.forward(200)
    az.backward(100)
    az.right(110)
    az.forward(70)
    az.left(70)
    az.color("lightblue")
    az.forward(100)
    az.left(110)
    az.forward(160)
    az.color("blue")
    az.left(70)
    az.forward(200)
    az.right(140)
    az.forward(200)
    az.backward(100)
    az.right(110)
    az.forward(70)    


mywindow = turtle.Screen()    
draw_my_initials()
mywindow.exitonclick()
