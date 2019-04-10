import pygame
from ui.locals import *
from ui.action import *


class PlayerTank(Display, Move):
    def __init__(self, **kwargs):
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.imges = [
            pygame.image.load("img/p1tankU.gif"),
            pygame.image.load("img/p1tankD.gif"),
            pygame.image.load("img/p1tankL.gif"),
            pygame.image.load("img/p1tankR.gif")
        ]
        self.direction = Direction.UP
        self.surface = kwargs['surface']
        self.speed = 5
        self.bad_direction = Direction.NONE
        self.width = self.imges[0].get_width()
        self.height = self.imges[0].get_height()

    def display(self):
        if self.direction == Direction.UP:
            self.surface.blit(self.imges[0], (self.x, self.y))
        if self.direction == Direction.DOWN:
            self.surface.blit(self.imges[1], (self.x, self.y))
        if self.direction == Direction.LEFT:
            self.surface.blit(self.imges[2], (self.x, self.y))
        if self.direction == Direction.RIGHT:
            self.surface.blit(self.imges[3], (self.x, self.y))

    def move(self, direction):

        if direction == self.bad_direction:
            return

        if self.direction != direction:
            self.direction = direction



        else:
            if direction == Direction.UP:
                self.y -= self.speed
                if self.y < 0:
                    self.y = 0
            if direction == Direction.DOWN:
                self.y += self.speed
                if self.y > GAME_HEIGHT - self.height:
                    self.y = GAME_HEIGHT - self.height
            if direction == Direction.LEFT:
                self.x -= self.speed
                if self.x < 0:
                    self.x = 0

            if direction == Direction.RIGHT:
                self.x += self.speed
                if self.x > GAME_WIDTH - self.width:
                    self.x = GAME_WIDTH - self.width

    def fire(self):
        pass

    def is_blocked(self, block):

        next_x = self.x
        next_y = self.y
        if self.direction == Direction.UP:
            next_y -= self.speed
            if next_y < 0:
                self.bad_direction = self.direction
                return True

        if self.direction == Direction.DOWN:
            next_y += self.speed
            if next_y > GAME_HEIGHT - self.height:
                self.bad_direction = self.direction
                return True
        if self.direction == Direction.LEFT:
            next_x -= self.speed
            if next_x < 0:
                self.bad_direction = self.direction
                return True
        if self.direction == Direction.RIGHT:
            next_x += self.speed
            if next_x > GAME_WIDTH - self.width:
                self.bad_direction = self.direction
                return True

        rect_player = pygame.Rect(next_x, next_y, self.width, self.height)
        rect_wall = pygame.Rect(block.x, block.y, block.width, block.height)

        collide = pygame.Rect.colliderect(rect_player, rect_wall)
        if collide:
            self.bad_direction = self.direction
            return True
        else:
            self.bad_direction = Direction.NONE
            return False


class Wall(Display, Block):
    def __init__(self, **kwargs):
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.surface = kwargs['surface']
        self.imge = pygame.image.load("img/walls.gif")
        self.width = self.imge.get_width()
        self.height = self.imge.get_height()

    def display(self):
        self.surface.blit(self.imge, (self.x, self.y))

    def destroy(self):
        pass


class Steel(Display, Block):
    def __init__(self, **kwargs):
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.surface = kwargs['surface']
        self.imge = pygame.image.load("img/steels.gif")
        self.width = self.imge.get_width()
        self.height = self.imge.get_height()

    def display(self):
        self.surface.blit(self.imge, (self.x, self.y))


class Water(Display, Block):
    def __init__(self, **kwargs):
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.surface = kwargs['surface']
        self.imge = pygame.image.load("img/water.gif")
        self.width = self.imge.get_width()
        self.height = self.imge.get_height()

    def display(self):
        self.surface.blit(self.imge, (self.x, self.y))


class Grass(Display, Order):
    """丛林"""

    def __init__(self, **kwargs):
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        self.image = pygame.image.load("img/grass.png")
        self.surface = kwargs["surface"]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def display(self):
        self.surface.blit(self.image, (self.x, self.y))

    def get_order(self):
        return 100
