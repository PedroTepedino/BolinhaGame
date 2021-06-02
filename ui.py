import random
from graphics import *


def draw_ui(window: GraphWin):
    linha_superior = Line(Point(0, 25), Point(800, 25))
    linha_superior.setWidth(50)
    linha_superior.setFill(color_rgb(50, 50, 180))
    linha_superior.draw(window)

    linha_inferior = Line(Point(0, 575), Point(800, 575))
    linha_inferior.setWidth(50)
    linha_inferior.setFill(color_rgb(250, 80, 80))
    linha_inferior.draw(window)

    linha_direita = Line(Point(800, 50), Point(800, 550))
    linha_direita.setWidth(25)
    linha_direita.setFill(color_rgb(50, 50, 50))
    linha_direita.draw(window)

    linha_esquerda = Line(Point(0, 50), Point(0, 550))
    linha_esquerda.setWidth(25)
    linha_esquerda.setFill(color_rgb(50, 50, 50))
    linha_esquerda.draw(window)

    fogos = []
    for i in range(3):
        fogos.append(Image(Point(150 + (300 * i), 575), '_imagens/fogo.png'))
        fogos[i].draw(window)

    clouds = []
    for i in range(4):
        clouds.append(Image(Point(110 + (200 * i), 25), '_imagens/cloud.jpg'))
        clouds[i].draw(window)

    diabins = [Image(Point(200, 555), '_imagens/diabin.png'), Image(Point(600, 560), '_imagens/diabin.png')]

    for i in range(len(diabins)):
        diabins[i].draw(window)

    window.setBackground('gray')
    # fogo = Image(Point(150, 575), 'fogo.PNG')
    # fogo2 = Image(Point(450, 575), 'fogo.PNG')
    # fogo3 = Image(Point(750, 575), 'fogo.PNG')
    # cloud = Image(Point(110, 25), 'cloud.JPG')
    # cloud2 = Image(Point(310, 25), 'cloud.JPG')
    # cloud3 = Image(Point(510, 25), 'cloud.JPG')
    # cloud4 = Image(Point(700, 25), 'cloud.JPG')
    # diabin = Image(Point(200, 555), 'diabin.PNG')
    # diabin2 = Image(Point(600, 560), 'diabin.PNG')
    # cloud.draw(window)
    # cloud2.draw(window)
    # cloud3.draw(window)
    # cloud4.draw(window)
    # fogo.draw(window)
    # fogo2.draw(window)
    # fogo3.draw(window)
    # diabin.draw(window)
    # diabin2.draw(window)

# win = GraphWin("Bolinha Game", 800, 600)
# draw_ui(win)
# playing = True
#
# while playing:
#     key = win.checkKey()
#
#     if key == "Escape":
#         playing = False
#
# win.close()
