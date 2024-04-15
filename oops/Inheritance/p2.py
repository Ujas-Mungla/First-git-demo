# Multiple Inheritance
class Father:
    def __init__(self):
        print("Parent Class Constructor")
        
    def showF(self):
        print("Parent class Method")

class Son(Father):
    def __init__(self):
        super().__init__() 
        print("Child class constructor")
        
    def showS(self):
        print("Child class method")

class Grandson(Son):
    def __init__(self):
        super().__init__()
        print("GrandChild Method")
        
    def showG(self):
        print("GrandSon class method")


g1 = Grandson()
g1.showG()  
g1.showS()  
g1.showF()  
