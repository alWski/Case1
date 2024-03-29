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
    turtle.color('cyan')
    turtle.begin_fill()
    turtle.forward(a/2)
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
    turtle.right(30)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.end_fill()

def paral(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('blueViolet')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(a/2)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(a/2)
    turtle.right(135)
    turtle.end_fill()

def triangle90dp(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('deep pink')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a*(2**0.5))
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()

def triangle90o(x, y, a):
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

def rombm(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('orange')
    turtle.begin_fill()
    turtle.left(45)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.end_fill()

def square(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('lime')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()

def pryam(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('magenta')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a/2)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a/2)
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
def kva(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('green')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
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
def main():
    turtle.speed(1000)
    trapezoidc(-300,300,200)
    turtle.right(45)
    triangle90dp(-250, 280, 70)
    turtle.left(45)
    square(-350,210,200)
    turtle.right(90)
    rombm(-250, 160,80)
    paral(-360, 80,60)
    paral(-335, 80, 60)
    paral(-145, 80, 60)
    paral(-120, 80, 60)
    paral(-95, 80, 60)

    turtle.left(90)
    paral(-150+100, 80, 200)
    turtle.left(135)
    triangle90dp(122+100, 9, 100)
    turtle.left(45)
    pryam(100+100, 80, 140)
    square(60+100, 150, 50)
    turtle.right(90)
    pryam(10+100, 200, 100)
    triangle60msg(61+100, 245, 55)
    rombm(30+100, 85, 40)

    turtle.right(180)
    triangle90p1(0, 0, 80)
    turtle.right(180)
    triangle90p2(-80, 80, 80)
    turtle.right(180)
    kva(-80, 80, 40)
    turtle.right(120)
    triangle90p2(-80, 120, 20)
    turtle.left(45)
    trapezoidc(0, 80, 30)
    turtle.right(15)
    kva(-20, -21, 20)
    kva(-80, -21, 20)


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
    turtle.right(45 + 180)
    trapezoidcP(-106, -30, 60)


    trapezoidc(0, 0, 150)
    triangle60msg(-38, -72, 80)
    triangle60t(-40, 70, 80)
    paraln(-118, -40, 60)
    triangle90p(-20, -135, 90)
    triangle90dp(-55, -135, 90)
    rombm(10, 5, 70)

    trapezoidc(0, 0, 150)
    triangle60msg(-38, -72, 80)
    triangle60t(-40, 70, 80)
    paraln(-118, -40, 60)
    triangle90p(-20, -135, 90)
    triangle90dp(-55, -135, 90)
    rombm(10, 5, 70)

    turtle.left(90)
    pryam(100, -100, 200)
    turtle.right(90)
    pryam(200, 46, 150)
    turtle.left(90)
    triangle60msg(350, -30, 76)
    turtle.right(90)
    paral(-310, 60, 240)
    turtle.left(135)
    triangle90dp(15, -25, 120)
    turtle.left(45)
    triangle90o(100, -25, 85)
    turtle.right(225)
    triangle90dp(-310, 60, 120)

    turtle.done()
main()