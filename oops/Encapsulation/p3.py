# Private
class Employee:
    def __init__(self,name,salary) :
        self.name=name
        self.__salary=salary
e1=Employee('Jessa',10000)
print("Salary :",e1.__salary)