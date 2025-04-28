# Auch metaclass

class MetaClass(type):
    def __call__(self, *args, **kwargs):
        print("__call__")
        return super.__call__(*args, **kwargs)
    
    @classmethod
    def __prepare__(metacls,name,bases):
        print("__prepare__")
        return {"hp":100, "mana":100}
    
    def __new__(metacls, name, bases, namespace):
        print("__name__")
        print(namespace)
        return super().__new__(metacls,name, bases, namespace)
        
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__()
        return cls._instances
    
class mySingleTon(metaclass=Singleton):
    pass

a = mySingleTon()
b = mySingleTon()

print(id(a))
print(id(b))





#class Archer(metaclass=MetaClass):
#    hp=100
    
#archer1 = Archer()
#archer2 = Archer()

#print(id(archer1))
#print(id(archer2))
