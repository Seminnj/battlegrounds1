# Module : Game
from player import *
from map import *

class Game:
    def __init__(self, num_player):
        self.num_player = num_player
        temp = Player()
        self.players = [temp]*num_player
        self.map = Map()
        self.global_time = 0

    def time_goes_by(self):
        self.global_time += 1
        for player in self.players:
            if player.status == "alive":
                player.run()
                #.safe_zone_effect()
                player.status_update

        print(self)
        
    def __str__(self):
        pass

    def 