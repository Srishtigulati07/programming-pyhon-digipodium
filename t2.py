from turtle import*

pensize ('fastest')
pencolor('yellow')
bgcolor('#303030')
pensize(2)

i=1000
while i>0 :
    fd(i)
    lt(90)
    i-=4
    dot(10,'red')
    write (i,font=('calibri',14,'bold'))

    mainloop()