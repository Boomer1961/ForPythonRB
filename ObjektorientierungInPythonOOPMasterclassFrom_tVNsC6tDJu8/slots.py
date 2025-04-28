class Archer:
    __slots__ = ("hp","mana")
    
    def __init__(self,hp,mana):
        self.hp = hp
        self.mana = mana
        
        
class Archer2:
    def __init__(self,hp,mana):
        self.hp = hp
        self.mana = mana
        
        
        
# archer = Archer(100,50)
# archer2 = Archer2(100,50)

from pympler import asizeof

#print(asizeof.asizeof(archer))
#print(asizeof.asizeof(archer2))  # 02:12:55

class MagicArcher(Archer):        
    def __init__(self, hp, mana,arrows):
        super().__init__(hp, mana)
        self.arrows = arrows
        
marcher = MagicArcher(hp=100,mana=70,arrows=24)
print(marcher.__dict__)