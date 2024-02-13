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
    turtle.right(0)
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
    turtle.right(60)
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
    turtle.right(90)
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
    turtle.right(105)
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
    trapezoidc(-50,0,150)
    triangle60msg(-13, 72, 80)
    triangle60t(-13, 142, 80)
    paraln(-30, 50, 50)
    triangle90p(-40, -135, 70)
    triangle90dp(20, -135, 70)
    rombm(5, 52, 60)

    turtle.done()

main()