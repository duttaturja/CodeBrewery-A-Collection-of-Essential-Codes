#Single Responsibility Principle

class Car:
    def __init__(self, model, fuel_efficiency):
        self.model = model
        self.fuel_efficiency = fuel_efficiency

    def drive(self):
        print(f"{self.model} is beign driven on the road...")

    def calculate_fuel_efficiency(self, miles, fuel):
        return miles / fuel