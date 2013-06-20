import game

class Player:
    def __init__(self, size, ships_count):
        self.sea = game.Sea(size)
        self.ships = []
        self.ready = False
        self.ships_count = ships_count

    def put_ship(self, size, coords, direction): #choose from list of ships
        ship = game.Ship(size, self.sea, coords, direction)
        self.ships.append(ship)
        if len(self.ships) == self.ships_count:
            self.ready = True
