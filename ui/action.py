from abc import *



class Display(metaclass=ABCMeta):


    @abstractmethod
    def display(self):
        pass