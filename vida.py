from graphics import *
import time

win = GraphWin("Bolinha Game", 800, 600)
t = Text(Point(35,20), "Vidas: ")
t.setOutline("red")
t.setTextColor("black")
t.setSize(14)
t.draw(win)
img = Image(Point(80,20),"vida.png") 
img2 = Image(Point(120,20),"vida.png") 
img3 = Image(Point(160,20),"vida.png") 
img.draw(win)
img2.draw(win)
img3.draw(win)

time.sleep(2)
img3.undraw()

#while img or img2 or img3 !=0:
    #if line > 600:
        #img3.undraw(win)
        #perde a primeira vida e volta pro inicio(return)
        #img2.undraw(win)
        #perde a segunda vida e volta pro inicio(return)
        #img2.undraw(win)
        #perde a vida e acaba o jogo(return)




    
    
        








win.getMouse()
win.close()
