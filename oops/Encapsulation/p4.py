# Public method to access private members
class Emoloyee:
    def __init__(self,name,salary) :
        self.name=name
        self.__salary=salary
    def show(self):
        print("Name :",self.name ,"Salary :",self.__salary)
e1=Emoloyee('Ram',10000)
e1.show()