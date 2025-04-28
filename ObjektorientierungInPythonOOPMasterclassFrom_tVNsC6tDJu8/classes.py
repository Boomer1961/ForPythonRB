# Klassen Anfangsbuchstabe groß
class Archer:
    # Attribute  hp = 100   mana = 0
    # in einer Metode
    def __init__(self,hp,mana,arrows):
        self.hp = hp
        self.mana = mana
        self._arrows = arrows # _ arrows bedeutet, das der Wert nie ausserhalb seiner 
                              # methode (Bsp.: archer1.arrows = 0) geändert werden darf.     
    def walk(self):
        print(f"Ich bin {self} und laufe.")
        
    def shoot(self):
        if self._arrows > 0:
            self._arrows -= 1
            print(f"Bogenschütze hat geschossen, noch {self._arrows}übrig")
        else:
            print("Bogenschütze hat keine Pfeile mehr.")
       
    @classmethod     
    def from_data(cls,hp,mana,arrows):
       # print(f"In cls_method einer Klassenmetohde {cls}")        
       return cls(hp,mana,arrows)     
            
    @staticmethod
    def static():
        print("Here in static")        
    

archer1 = Archer(100,50,0)
archer1.shoot()

Archer(100,5,0)
archer = Archer
archer.static


