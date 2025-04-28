class Archer:
    # Attribute  hp = 100   mana = 0
    # in einer Metode
    def __init__(self,hp,mana,arrows):
        self.hp = hp
        self.mana = mana
        self.arrows = arrows # _ arrows bedeutet, das der Wert nie ausserhalb seiner 
                              # methode (Bsp.: archer1.arrows = 0) geändert werden darf.  
                              
    def __str__(self):
        return f"Archer ist {self.hp}, mit {self.mana}, mit {self.arrows} "
    
    def __repr__(self):  # repr wird hier durch __str__ überschrieben, trotzdem lesbar 
        return f"Archer {self.hp},{self.mana},{self.arrows}"   # ausserhalbe durch
        # print(repr(Archer))
        
    def __eq__(self, other):
        if not isinstance(other,Archer):
            return False
        return self.hp == other.hp and self.mana == other.mana and self.arrows == other.arrows

    def __gt__(self, other):
        if not isinstance(other, Archer):
            return NotImplemented
        return self.hp > other.hp
    
    def __ge__(self,other):
        if not isinstance(other, Archer):
            return NotImplemented
        return self.hp >= other.hp
    
    def __hash__(self):        
        return hash((self.hp,self.mana,self.arrows))
  
archer1 = Archer(10,50,1)
archer2 = Archer(11,50,1)

print(archer1 == archer2)
print(archer1 < archer2)
print(hash(archer1))

archers = {archer1 : "Happy",archer2 : "depressiv" }

class Company:
    def __init__(self,size):
        self.archers = []
        self.size = size
        self.index = 0
        
    def add_archer(self,archer):
        if not isinstance(archer,Archer):
            raise TypeError("Nur Archer in Company erlaubt")
        if len(self.archers) >= self.size:
            raise ValueError("Company bereits voll")
        self.archers.append(archer)
        
    def __add__(self,other):    # 42:08
        if not isinstance(other,Archer):
            raise TypeError("Nur Archer addieren erlaubt")
        new_company = Company(self.size)
        for archer in self.archers:
            new_company.add_archer(archer)
        new_company.add_archer(other)
        return new_company
        
    def __radd__(self,other):
        if not isinstance(other,Archer):
            raise TypeError("Nur Archer addieren erlaubt.")
        return self+other
        
    def __iter__(self):
        return iter(self.archers)
    
    def __next__(self):
        if self.index > len(self.archers):
            raise StopIteration
        new_archer = next(self)
        self.index += 1
        return new_archer

company = Company(3)
company = company + archer1
company = archer1 + company
print(company.archers)
    
for soldier in company.archers:
    print(soldier)
            
            
        