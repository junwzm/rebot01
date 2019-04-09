from pygame.locals import *
from ui.container import *
from ui.locals import *
import pygame
#0开始，1游戏

__current=1

def getcurrent():
    return __current
def setcurrent(value):
    global __current
    __current=value


class Startpage:

    def __init__(self,surface):
        self.surface=surface


    def graphic(self):
        self.surface.fill((0,255,0))


    def keydown(self,key):
        print(key)
        if key==K_RETURN:
            setcurrent(1)




    def keypress(self,keys):
        pass


class Gamepage:


    def __init__(self,surface):
        self.surface=surface
        self.gameSurface=pygame.Surface((GAME_WIDTH,GAME_HEIGHT))
        self.infoSurface=pygame.Surface((INFO_WIDTH,INFO_HEIGHT))
        self.gamecontainer=Gamecontainer(self.gameSurface)
        self.infocontainer=Infocontainer(self.infoSurface)

    def graphic(self):
        self.surface.fill((200,200,200))
        self.surface.blit(self.gameSurface,(WINDOW_PADDING,WINDOW_PADDING))
        self.gamecontainer.graphic()
        self.surface.blit(self.infoSurface,(GAME_WIDTH+2*WINDOW_PADDING,WINDOW_PADDING))
        self.infocontainer.graphic()




    def keydown(self,key):
        self.gamecontainer.keydown(key)

    def keypress(self,keys):
        self.gamecontainer.keypress(keys)
