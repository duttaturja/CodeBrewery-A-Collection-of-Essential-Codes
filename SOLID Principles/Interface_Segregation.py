#Interface Segregation Principle
class Vehicle:
    pass

class Drivable(Vehicle):
    def drive(self):
        
        pass

class Flyable(Vehicle):
    def fly(self):
        pass

class Car(Drivable):
    def drive(self):
        print("Driving on the road...")

class Airplane(Flyable):
    def fly(self):
        print("Flying in the sky...")

#usage
bugatti = Car()
bugatti.drive()

boyeing747 = Airplane()
boyeing747.fly()