class Field:
    def __init__(self, *content):
    	if(content == ()):
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
    pass


class Game:
    pass
