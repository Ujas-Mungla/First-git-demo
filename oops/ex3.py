class Vehicle:
    def __init__(self,name,max_speed,mileage) :
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class Bus (Vehicle):
    pass
drive=Bus("School",180,12)
print("Vehical Name :",drive.name,"Max_Speed :",drive.max_speed,"Mileage :",drive.mileage)