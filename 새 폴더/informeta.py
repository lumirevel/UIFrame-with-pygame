import math
from UI import *
from vector import vector
from viewer import Window, Movie

#game window 설정
game=Window()

class Play(Movie):
    def __init__(self):
        pass
    
    def mousePressEvent(self,window):
        pass
        
    def mouseMoveEvent(self,window):
        pass
            
    def mouseReleaseEvent(self,window):
        pass
    
    def main(self,window):
        pass

game.addscene(Play())

game.main()