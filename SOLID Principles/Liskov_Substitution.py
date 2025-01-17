#Liskov Substitution Principle
class Bird:
    pass #No fly method

class FlyingBird(Bird):
    def fly(self):
        print("Flying...") 


class Sparrow(FlyingBird):
    pass # Sparrow can fly


class Penguin(Bird):
    pass # No fly method
    
