class Field:
    def __init__(self, *content):
    	if content == ():
    		self.content = None
    	else:
    		self.content = content[0] #content[0] is not instance of ShipPart
    	self.is_open = False

    def open(self):
    	self.is_open = True


class ShipPart:
    pass


class Ship:
    pass


class Sea:
    def __init__(self, size=10):
    	self.size = size
    	self.board = [[Field() for i in range(size)] for i in range(size)]

    def __getitem__(self, index):
    	if index < 0 or index >= self.size:
    		raise IndexError
    	return self.board[index]

    def is_valid_coordinates(self, row, column):
    	return 0 <= row < self.size and 0 <= column < self.size

class Game:
    pass
