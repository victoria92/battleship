class FullSquareError(Exception):
    pass


class Field:
    def __init__(self, *content):
        if content == ():
            self.content = None
        else:
            if isinstance(content[0], ShipPart):
                self.content = content[0]
            else:
                raise TypeError
        self.is_open = False

    def open(self):
        self.is_open = True


class ShipPart:
    def __init__(self, ship):
        self.ship = ship

    def is_part_of_sunk_ship(self):
        return self.ship.is_sunk()


class Ship:
    def __init__(self, size, sea, start, direction):
        self.size = size
        self.sea = sea
        if direction:
            self.location = [[start[0] + x, start[1]] for x in range(size)]
        else:
            self.location = [[start[0], start[1] + x] for x in range(size)]
        for coords in self.location:
            if not sea.is_valid_coordinates(*coords):
                raise IndexError
            if isinstance(sea[coords].content, ShipPart):
                raise FullSquareError
        for coords in self.location:
            sea[coords] = Field(ShipPart(self))

    def is_sunk(self):
        return all([self.sea[coords].is_open for coords in self.location])


class Sea:
    def __init__(self, size=10):
        self.size = size
        self.board = [[Field() for i in range(size)] for i in range(size)]

    def __getitem__(self, index):
        if index[0] < 0 or index[0] >= self.size:
            raise IndexError
        if index[1] < 0 or index[1] >= self.size:
            raise IndexError
        return self.board[index[0]][index[1]]

    def __setitem__(self, index, value):
        if index[0] < 0 or index[0] >= self.size:
            raise IndexError
        if index[1] < 0 or index[1] >= self.size:
            raise IndexError
        self.board[index[0]][index[1]] = value

    def is_valid_coordinates(self, row, column):
        return 0 <= row < self.size and 0 <= column < self.size

    def represent(self):
        representation = ""
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j].is_open:
                    if isinstance(self.board[i][j].content, ShipPart):
                        representation += "Y "
                    else:
                        representation += "N "
                else:
                    representation += "X "
            representation += "\n"
        return representation
