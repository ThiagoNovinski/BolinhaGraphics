from graphics import *

win = GraphWin("bola", 800, 700)

bola = Image(Point(400, 100), 'bola.png')
bola.draw(win)
velocidade = 0.0001

while True:
    bola.move(0, velocidade)
    if win.checkMouse():
        break

    centro = bola.getAnchor().getY()

    while velocidade >= 0:
        velocidade = velocidade + 0.0001
        bola.move(0, velocidade)
        centro = bola.getAnchor().getY()
        if (centro+50) >= 700:
            velocidade = velocidade*-1

    while velocidade < 0:
        velocidade = velocidade + 0.00012
        bola.move(0, velocidade)
        centro = bola.getAnchor().getY()
        if (centro-50) <= 0:
            velocidade = velocidade*-1


#raio = bola.getWidth()
# print(raio)

win.getMouse()
win.close()
