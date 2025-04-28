#class Bogen:
#    def __init__(self,name,preis,schaden):
#        self.name = name
#        self.preis = preis
#        self.schaden = schaden
        
        
# bogen_a = Bogen("Toller Bogen",500,90)

from dataclasses  import dataclass


'''
# @dataclass(frozen=True) wegen Vererbung zu MagicBogen
@dataclass
class Bogen:
    name: str
    preis: float
    schaden: int

@dataclass
class MagicBogen(Bogen):
    mgc_dmg: int = 200
    

    
bogen_1 = Bogen("Toller Bogen",500,90)
bogen_2 = Bogen("Toller Bogen",500,90)
print(bogen_1==bogen_2)

'''

from pydantic import BaseModel 

class Bogen(BaseModel):
    name: str
    preis: float
    schaden: int = 100
    
Bogen(name="testbogen", preis= 500, schaden= "100")

from enum import Enum, unique


class Waffen(Enum):
    S = "Schwert"
    B = "Bogen"
    A = "Axt"
    # SCHWERT = "Schwert"
    
class Waffenkammer(BaseModel):
    zimmer: int
    waffen: list[Waffen]
    
    
    
print(Waffenkammer.waffen)
kammer = Waffenkammer(zimmer = 3, waffen = ["Schwert","Axt"])
print(kammer)
