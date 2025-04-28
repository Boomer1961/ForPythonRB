from abc import ABC, abstractmethod

class AbstractArcher(ABC):  
    
    @property
    @abstractmethod
    def hp():
        pass
    
    @abstractmethod
    def walk(self):
        print("Ich laufe und bin eine ABC.")
    
        
class Archer(AbstractArcher):
    def walk(self):
        print("Ich laufe ....")
        
    def __init__(self,hp):
        self._hp = hp
        
    @property
    def hp(self):
        return self.hp
        
        
        
archer = Archer(100)
archer.walk()