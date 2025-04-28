class A:
    def sayhi(self):
        print("Hello from A")
        
class B(A):
    def sayhi(self):
        print("Hello from B")
        
class C(A):
    def sayhi(self):
        print("Hello from C")
        
class D(C, B):
    pass

d = D()
print(D.__mro__)
d.sayhi()