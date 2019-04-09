
import sys
from ui.page import *
from pygame.locals import *
import pygame
from ui.locals import *

if __name__ == '__main__':
    pygame.init()

    window=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

    pygame.display.set_caption('坦克大战')

    iconimge=pygame.image.load('img/p1tankD.gif')

    pygame.display.set_icon(iconimge)

    start=Startpage(window)

    gamepage=Gamepage(window)

    while True:
        current=getcurrent()
        page=None
        if current==0:
            page=start
        elif current==1:
            page=gamepage

        page.graphic()

        pygame.display.flip()
        events=pygame.event.get()
        for event in events:
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                page.keydown(event.key)
        keys=pygame.key.get_pressed()
        page.keypress(keys)