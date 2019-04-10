from abc import *



class Display(metaclass=ABCMeta):


    @abstractmethod
    def display(self):
        pass
class Move(metaclass=ABCMeta):

    @abstractmethod
    def move(self,direction):
        pass


    @abstractmethod
    def is_blocked(self,block):
        pass


class Block:

    # @abstractmethod
    # def block(self):
    pass

class Order(metaclass=ABCMeta):
    """排序显示"""

    @abstractmethod
    def get_order(self):
        pass