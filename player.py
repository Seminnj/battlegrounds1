# Module : Player

from event import *

class Player:
    def __init__(self,id):
        self.id = id
        self.health = 100
        self.location = get_random_location()
        self.status = "alive"

    def run(self, target_location):
        pass

    # Override
    def __str__(self):
        print("player id: {0}, health: {1}, location: {2}".format(self.id, self.health, self.location))

    def statur_update(self):
        if self.health <= 0:
            self.status = "dead"