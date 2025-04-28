#class Archer:
#    
#    def __init__(self,hp):
#        self._hp = hp
#        
#    def get_hp(self):
#        return self._hp
#    
#    def set_hp(self, value):
#        self._hp = value
#        
#        
#        
#    property(fget=get_hp,fset=set_hp,)
 
 
class Archer:
    def __init__(self,hp,dmg,crit):
        self._hp = hp
        self.dmg = dmg
        self.crit = 1.3
        
    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, value):
        if value > 100:
            raise ValueError("Wert ist über 100") 
        self._hp = value
 


   
archer = Archer(100)
print(archer.hp)

archer.hp = 99
print(archer.hp)

#print(archer.get_hp())
