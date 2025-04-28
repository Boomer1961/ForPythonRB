# Klassen Anfangsbuchstabe groß
class Archer:
    # Attribute  hp = 100   mana = 0
    # in einer Metode
    def __init__(self,hp,mana):
        self.hp = hp
        self.mana = mana
    
    def walk(self):
        print(f"Ich bin {self} und laufe.")
    
    
    
# Ausdruck durch Dunder Attribute der Klasse als Dictionary bzw. Mapping proxy
# print(type(Archer.__dict__)); 

print(Archer.__dict__)

archer1 = Archer()
print(type(archer1))   #  <class '__main__.Archer'>
print(type(archer1.__dict__))  # <class 'dict'>
print(archer1.__dict__) # Leeres dictionary, weil Attributdaten zur class gehören.

archer1.walk()