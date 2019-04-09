from ui.view import *



class Gamecontainer:


    def __init__(self,surface):
        self.surface=surface

        self.views=[]
        self.playertank=PlayerTank(surface=self.surface)

        self.views.append(self.playertank)

        self.wall1=Wall(surface=self.surface,x=20,y=60)

        self.views.append(self.wall1)

        self.wall2=Wall(surface=self.surface,x=100,y=200)

        self.views.append(self.wall2)

        self.steel=Steel(surface=self.surface,x=300,y=100)

        self.views.append(self.steel)


    def graphic(self):
        self.surface.fill((0,0,0))
        # self.playertank.display()
        #
        # self.wall1.show()
        # self.wall2.show()
        for view in self.views:
            view.display()

    def keydown(self,key):
        pass

    def keypress(self,keys):
        pass
class Infocontainer:


    def __init__(self,surface):
        self.surface=surface


    def graphic(self):
        self.surface.fill((0,200,0))



