# Auch metaclass

#class Archer:
#    hp = 100
    
#archer = Archer()
#print(type(archer))
#print(type(Archer))
#print(type(type))

#Archer2 = type("Archer2",(),{"hp":100})
#archer2 = Archer2()
#print(type(archer2))

class MetaClass(type):
    def __call__(self, *args, **kwargs):
        print("__call__")
        return super.__call__(*args, **kwargs)
    
    @classmethod    
    def __prepare__(metacls, name, bases):
        print("__prepare__")
        return {"hp":100,"mana":100}
    
        

# class Archer(MetaClass=type):
class Archer(MetaClass = MetaClass):
    hp = 100
    
print(type(Archer))


