#Parent class
class Vehicle():
    def __init__(self, model, year, wheels ):
        self.model = model
        self.year = year
        self.wheels = wheels

    def show_details(self):
        print(f"The vehicle is a {self.model} of {self.year} and has {self.wheels} wheels")
    
#Child class
class Car(Vehicle):
    def __init__(self, model, year, doors):
        super().__init__(model, year, wheels = 4) 
        self.doors = doors

    def show_doors(self):
        print(f"It has {self.doors} doors")

class Bike(Vehicle):
    def __init__(self, model, year, cornering_angle):
        super().__init__(model, year, wheels = 2)
        self.cornering_angle = cornering_angle
    
    def show_cornering_angle (self):
        print(f"Its cornering angle is: {self.cornering_angle}")


#calling instances
vehicle = Vehicle("Rickshaw", "1998",3)

car = Car("Aston Martin", "1996", 2)
bike = Bike("Ducati", "2003", 30)

#calling methods
vehicle.show_details()

car.show_details()
car.show_doors()

bike.show_details()
bike.show_cornering_angle()



    
        