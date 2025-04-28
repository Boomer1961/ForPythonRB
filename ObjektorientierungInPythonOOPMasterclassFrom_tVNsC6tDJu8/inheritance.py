# inheritance - Vererbung von Klassen
class BasePlayer:
    def __init__(self,hp):
        self.hp = hp
    def walk(self):
        print("Ich laufe ....")
    
    

class Archer(BasePlayer):
    def __init__(self,hp,arrows):  # 58:40
        # BasePlayer.__init__(self,hp=hp) wird ersetzt durch super
        super().__init__(hp=hp) # dadurch hat class Archer Zugriff auf deren methoden
        super().walk()
        self.arrows = arrows


class Wizard(BasePlayer):
    pass

archer = Archer(100,10)
wizard = Wizard(15)

print(archer.hp)
print(wizard.hp)

x = {"bla":'123'}
x["bla"] = 122

print(x)

class NoUpdateDictionary(dict):  # 01:00:12
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError("Key existiert nicht")
        super().__setitem__(key,value)
    
x = NoUpdateDictionary()
x["key"] = 123 
x["key"] = 125

#print(x)