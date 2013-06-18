class Field:
    def __init__(self, *content):
    	if(content == ()):
    		self.content = None
    	else:
    		self.content = content[0]
    	self.is_open = False

    def open(self):
    	self.is_open = True


class ShipPart:
    pass


class Ship:
    pass


class Sea:
    pass #size, number ships, type


class Game:
    pass
