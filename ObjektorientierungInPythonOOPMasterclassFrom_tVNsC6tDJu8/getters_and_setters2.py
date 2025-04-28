class Archer:
    def __init__(self,hp,dmg):
        self._hp = hp
        self._dmg = dmg
        self.crit = 1.3
        self._overall_demage = None
        
    @property
    def dmg(self):
        return self._dmg
    
    @dmg.setter
    def dmg(self,value):
        self._dmg = value
        
    @property
    def overall_demage(self):
        if self._overall_demage is None:
            print("Berechnung wird durchgeführt")
            self._overall_demageoverall_demage = self.dmg*self.crit
        return self._overall_demageoverall_demage
    
archer = Archer(100,50)
print(archer.overall_demage)
archer.dmg = 500
print(archer.overall_demage)
print(archer.overall_demage)