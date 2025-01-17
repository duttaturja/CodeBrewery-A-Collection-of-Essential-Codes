#parent class
class Player:
    def play(self):
        pass

#sub class
class Footballer(Player):
    def play(self):
        print("footballer kicks the ball")
 
#sub class
class Cricketer(Player):
    def play(self):
        print("Cricketer swings the bat")


#creating instances
cricket_player = Cricketer()
football_player = Footballer()

#calling methods
cricket_player.play()
football_player.play()