class Animal:
    def speak(self):
        print("ANimal Speaks")
class Mannal(Animal):
    def give_birth(self):
        print("Mammal Gives Birth ")
class Bird(Animal):
    def lay_eggs(self):
        print("Bird lays eggs")
class Platypus(Mannal,Bird):
    pass

p1=Platypus()
p1.speak()
p1.give_birth()
p1.lay_eggs()
