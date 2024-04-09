class Vehical:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def seating_capacity(self,capacity):
        return f"The Seating Capacity of a {self.name} is {capacity}"
class Bus(Vehical):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
sch_bus=Bus("Schools Bus",200,210)
print(sch_bus.seating_capacity())
