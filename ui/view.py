import pygame
from ui.locals import *
from ui.action import *


class PlayerTank:
    def __init__(self,**kwargs):
        self.x=500
        self.y=50
        self.imges=[
            pygame.image.load("img/p1tankU.gif"),
            pygame.image.load("img/p1tankD.gif"),
            pygame.image.load("img/p1tankL.gif"),
            pygame.image.load("img/p1tankR.gif")
        ]
        self.direction=Direction.UP
        self.surface=kwargs['surface']
    def display(self):
        if self.direction==Direction.UP:
            self.surface.blit(self.imges[0],(self.x,self.y))
        if self.direction==Direction.DOWN:
            self.surface.blit(self.imges[1],(self.x,self.y))
        if self.direction==Direction.LEFT:
            self.surface.blit(self.imges[2],(self.x,self.y))
        if self.direction==Direction.RIGHT:
            self.surface.blit(self.imges[3],(self.x,self.y))
    def move(self):
        pass
    def fire(self):
        pass


class Wall(Display):
    def __init__(self,**kwargs):
        self.x=kwargs['x']
        self.y=kwargs['y']
        self.surface=kwargs['surface']
        self.imge=pygame.image.load("img/walls.gif")
    def display(self):
        self.surface.blit(self.imge,(self.x,self.y))


    def destroy(self):
        pass
class Steel(Display):
    def __init__(self, **kwargs):
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.surface = kwargs['surface']
        self.imge = pygame.image.load("img/steels.gif")

    def display(self):
        self.surface.blit(self.imge, (self.x, self.y))
