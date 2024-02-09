from turtle import *


def drawLogo():
    speed(0)
    bgcolor('white')
    color('blue')
    hideturtle()
    n, p = 1, True
    while True:
        circle(n)
        n = (n-1 if p else n+1)
        p = (not p if (n == 0 or n == 60) else p)
        right(1)
        backward(3)


if __name__ == '__main__':
    drawLogo()
