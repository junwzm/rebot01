from ui.view import *
from pygame.locals import *
from ui.locals import *



class Gamecontainer:


    def __init__(self,surface):
        self.surface=surface

        self.views=[]

        file=open('map/1.map','r',encoding='UTF-8')

        for cow,line in enumerate(file):
            texts=line.strip()
            for column,text in enumerate(texts):
                x=column*BLOCK
                y=cow*BLOCK
                if text=='草':
                    self.views.append(Grass(surface=self.surface,x=x,y=y))
                if text=='砖':
                    self.views.append(Wall(surface=self.surface,x=x,y=y))
                if text=='铁':
                    self.views.append(Steel(surface=self.surface,x=x,y=y))
                if text=='主':
                    self.playertank=PlayerTank(surface=self.surface,x=x,y=y)
                    self.views.append(self.playertank)
                if text=='水':
                    self.views.append(Water(surface=self.surface,x=x,y=y))





        file.close()
        # self.playertank=PlayerTank(surface=self.surface)
        #
        # self.views.append(self.playertank)
        #
        # self.wall1=Wall(surface=self.surface,x=20,y=60)
        #
        # self.views.append(self.wall1)
        #
        # self.wall2=Wall(surface=self.surface,x=100,y=200)
        #
        # self.views.append(self.wall2)
        #
        # self.steel=Steel(surface=self.surface,x=300,y=100)
        #
        # self.views.append(self.steel)
    def _sort(self,view):

        return view.get_order() if isinstance(view, Order) else 0



    def graphic(self):
        self.surface.fill((0,0,0))
        # self.playertank.display()
        #
        # self.wall1.show()
        # self.wall2.show()

        self.views.sort(key=self._sort)



        for view in self.views:
            view.display()

#判断 可移动的物体 是否和 可阻挡移动的物体 发生了碰撞
        for move in self.views:
            if isinstance(move,Move):
                for block in self.views:
                    if isinstance(block,Block):

                        if move.is_blocked(block):
                            break

    def keydown(self,key):
        pass

    def keypress(self,keys):
        if keys[K_a]:
            self.playertank.move(Direction.LEFT)
        if keys[K_d]:
            self.playertank.move(Direction.RIGHT)
        if keys[K_w]:
            self.playertank.move(Direction.UP)
        if keys[K_s]:
            self.playertank.move(Direction.DOWN)


class Infocontainer:


    def __init__(self,surface):
        self.surface=surface


    def graphic(self):
        self.surface.fill((0,200,0))



