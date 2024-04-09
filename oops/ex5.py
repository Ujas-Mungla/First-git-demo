class Vehicle:
    color="White"
    def __init__(self, name, max_speed, mileage):
        
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

b1=Bus("Schooh Volvo",180,12)
print("Color:",b1.color,"Vehical Name :",b1.name,"Speed :",b1.max_speed,"Mileage :",b1.mileage)
c1=Car("Audi Q5",240,18)
print("Color:",c1.color,"Vehical Name :",c1.name,"Speed :",c1.max_speed,"Mileage :",c1.mileage)
