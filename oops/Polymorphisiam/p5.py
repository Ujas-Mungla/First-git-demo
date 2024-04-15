# Polymorphism with Inheritance: 
class Bird:
    def intro(self):
        print("There are many types of birds...")
    def flight(self):
        print("Mosty of the birds can fly but some cannot")
class sparrow(Bird):
    def flight(self):
        print("Sparrow can fly.")
class ostrich(Bird):
    def flight(self):
        print("ostrich cannot fly...")

b1=Bird()
s1=sparrow()
o1=ostrich()

b1.intro()
b1.flight()
s1.intro()
s1.flight()
o1.intro()
o1.flight()