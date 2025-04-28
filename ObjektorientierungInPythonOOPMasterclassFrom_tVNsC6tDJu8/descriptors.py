from weakref import WeakKeyDictionary


class Deskriptor:
    def __init__(self,value):
        self._data = WeakKeyDictionary()
        self._value = value
    
    
    def __get__(self,instance,owner):
        print(instance)
        return self._data.get(instance)
    
    
    def __set__(self,instance,value):
        if value < 0 or value > 100:
            raise ValueError("Nur Werte zwischen 0 und 100 erlaubt")
        self._value = value
        
        
class Archer:
    hp = Deskriptor(100)
    mana = Deskriptor(50)
        
archer = Archer()
archer.hp = 70

archer2 = Archer()
archer2.hp = 100

print(archer.hp)
print(archer2.hp)