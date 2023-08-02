from turtle import*

def haxagon():
    for i in range(6):
        fd(100)
        lt(360/6)

#call the function
haxagon()
penup()
goto(100,100)
pendown()
haxagon()
penup()
goto(-100,100)
haxagon()
penup()
goto(-100,-100)
pendown()
haxagon()
penup()
goto(100,-100)
pendown()
haxagon()
hideturtle()
mainloop()
