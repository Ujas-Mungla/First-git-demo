# Hieriachical Inheritance

# class Shape:
#     def __init__(self,color) :
#         self.color=color
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, color,radius):
#         super().__init__(color)
#         self.radius=radius
#     def area(self):
#         return 3.14* self.radius**2

# class Square(Shape):
#     def __init__(self, color, side_length):
#         super().__init__(color)
#         self.side_length = side_length
#     def area(self):
#         return self.side_length**2

# circle=Circle("Red",5)
# square=Square("Blue",4)
# print(circle.area())
# print(square.area())

class Employee:
    def __init__(self,name,salary) :
        self.name=name
        self.salary=salary
    def display_details(self):
        return f"Name :{self.name} Salary :{self.salary}"

class Manager(Employee):
    def __init__(self, name, salary,team_size):
        super().__init__(name, salary)
        self.team_size=team_size
    def display_details(self):
        return f"{super().display_details()} ,Team Size :{self.team_size}"

class Developer(Employee):
    def __init__(self, name, salary,pg):
        super().__init__(name, salary)
        self.pg="Programming Language"
    def display_details(self):
        return f"{super().display_details() },Language :{self.pg} "

m1=Manager("John",80000,10)
d1=Developer("ALice",60000,"Python")
print(m1.display_details())
print(d1.display_details())