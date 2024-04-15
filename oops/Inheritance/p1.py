# single Inheritance
class Father:
    money=10000
    def show(self):
        print("Parent class insttance method")
    @classmethod
    def ShowMoney(cls):
        print("Parent Class Class method :",cls.money)
    @staticmethod
    def stat():
        a=10
        print("Parent class Statiuc method",a)
class Son(Father):
    def disp(self):
        print("Child class instance method")
s1=Son()
s1.disp()
s1.show()
s1.ShowMoney()
s1.stat()
        