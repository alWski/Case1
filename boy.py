import turtle
def triangle60msg(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(60)
    turtle.color('medium spring green')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.end_fill()


def triangle60t(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('tomato')
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
    turtle.right(180)
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

def paraln(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('navy')
    turtle.begin_fill()
    turtle.right(0)
    turtle.forward(a)
    turtle.right(65)
    turtle.forward(a)
    turtle.right(115)
    turtle.forward(a)
    turtle.right(65)
    turtle.forward(a)
    turtle.right(115)
    turtle.end_fill()

def triangle90dp(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('deep pink')
    turtle.begin_fill()
    turtle.right(270)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a*(2**0.5))
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()

def triangle90p(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('orange')
    turtle.begin_fill()
    turtle.right(30)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a*(2**0.5))
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()

def rombm(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('maroon')
    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.end_fill()


def main():
    trapezoidc(0,0,150)
    triangle60msg(-38, -72, 80)
    triangle60t(-40, 70, 80)
    paraln(-118, -40, 60)
    triangle90p(-20, -135, 90)
    triangle90dp(-55, -135, 90)
    rombm(10, 5, 70)

    turtle.done()

main()