import turtle

def draw_a_ne6to_si(obj):

    for i in range(1,3):
        obj.color("green")
        obj.forward(100)
        obj.right(30)

    for i in range(1,3):
        obj.color("yellow")
        obj.forward(100)
        obj.left(150)

def draw():

    mywindow = turtle.Screen()
    mywindow.bgcolor("blue")
    fascu = turtle.Turtle()
    fascu.speed(30) 
    fascu.shape("circle")
    for i in range(1,39):
        draw_a_ne6to_si(fascu)
        fascu.right(10)

    fascu.left(160)
    fascu.forward(300)    
    mywindow.exitonclick()

print("now this is a flower")
draw()

 
