import turtle

def draw_a_square():

    fascu = turtle.Turtle()
    fascu.shape("circle")
    fascu.color("green")
    fascu.speed(3)

    for i in range(1,5):
        fascu.forward(100)
        fascu.right(90)
    
    
def draw_a_circle():    
    
    bopcu = turtle.Turtle()
    bopcu.color("white")
    bopcu.speed(3)
    bopcu.shape("turtle")

    bopcu.circle(55)
    bopcu.left(3)


def draw_a_triangle():

    porcho = turtle.Turtle()    
    porcho.color("yellow")
    porcho.speed(3)

    for i in range(1,4):
        porcho.forward(250)
        porcho.left(120)


mywindow=turtle.Screen()
mywindow.bgcolor("blue")
draw_a_square() 
draw_a_circle()
draw_a_triangle()
mywindow.exitonclick()
