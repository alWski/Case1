import turtle
def triangle60msg(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('medium spring green')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.end_fill()
def trapezoidc(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('cyan')
    turtle.begin_fill()
    turtle.forward(a*0.5)
    turtle.right(60)
    turtle.forward(a/2)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a/2)
    turtle.right(60)
    turtle.end_fill()
def trapezoidcP(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('pink')
    turtle.begin_fill()
    turtle.forward(a*0.5)
    turtle.right(60)
    turtle.forward(a/2)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a/2)
    turtle.right(60)
    turtle.end_fill()
def triangle90p(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('orange')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a*(2**0.5))
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
def triangle90p1(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('red')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a*(2**0.5))
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
def triangle90p2(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('blue')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a*(2**0.5))
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
def paraln(x, y, a):
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('navy')
    turtle.begin_fill()
    turtle.right(30)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.end_fill()
def main():
    turtle.right(30)
    triangle60msg(0, 0, 60)
    turtle.right(30)
    paraln(0, 0, 60)
    trapezoidc(-53, 0, 60)
    triangle90p(0, 30, 30)
    turtle.right(270)
    triangle90p2(0, 30, 30)
    turtle.right(45)
    triangle90p1(0, -60, 30)
    turtle.right(45+180)
    trapezoidcP(-106, -30, 60)
    turtle.done()
    
main()