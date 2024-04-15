class Student:
    def __init__(self, name, rno, age):
        self.name = name
        self.__rno = rno
        self.__age = age

    def show(self):
        print('Student Details:', self.name,",", self.__rno)

    def get_rno(self):
        return self.__rno

    def set_rno(self, number): 
        if number > 50:
            print("Invalid RNO, Please enter a valid RNO")
        else:
            self.__rno = number

js = Student("Rohan", 10, 15)
js.show()
js.set_rno(120)  
js.set_rno(25)   
js.show()
