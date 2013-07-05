import pygame
import player
import colors
from random import choice


#size = 20
#margin = 3

player1 = player.Player(10, 5)
sea1 = player1.sea
computer = player.Player(10, 5)
sea2 = computer.sea

grid1 = [[0 for i in range(10)] for i in range(10)]
grid2 = [[0 for i in range(10)] for i in range(10)]

pygame.init()
dimension = [600, 255]
screen = pygame.display.set_mode(dimension)
pygame.display.set_caption("Battle ship")
size = 20
margin = 3

def draw_board():

    screen.fill(colors.white)
    for row in range(10):
        for column in range(10):
            pygame.draw.rect(screen,
                             colors.colors[grid1[row][column]],
                             [(margin+size)*column+margin,
                              (margin+size)*row+margin,
                              size,
                              size])

    for row in range(10):
        for column in range(10):
            pygame.draw.rect(screen,
                             colors.colors[grid2[row][column]],
                             [(margin+size)*(column+13)+margin,
                              (margin+size)*row+margin,
                              size,
                              size])



def put_one_ship(new_player, position, ship, direction, size, margin):
    column = position[0] // (size + margin)
    row = position[1] // (size + margin)
    if(column < 10 and row < 10):
        try:
            new_player.put_ship(ship, [row, column], direction)
            for coords in new_player.ships[-1].location:
                grid1[coords[0]][coords[1]] = 5
            return True
        except IndexError:
            print("You must stay in your sea")
            return False
        except player.game.FullSquareError:
            print("This place is already full")
            return False


def player_make_move(position, size, margin):
    turn = True
    column = position[0] // (size + margin) - 13
    row = position[1] // (size + margin)
    if 0 <= column < 10 and 0 <= row < 10:
        sea2[[row, column]].open()
        if isinstance(sea2[row, column].content, player.game.ShipPart):
            grid2[row][column] = 1
        else:
            grid2[row][column] = 2
        draw_board()
        pygame.display.flip()
        if grid2[row][column] == 2:
            turn = False
        else:
            if sea2[[row, column]].content.is_part_of_sunk_ship():
                print("You destroyed this ship!")
            else:
                print("You hit it!")

    return turn


def computer_put_his_ships():
    computer.put_ship(5, [1, 4], 0)
    computer.put_ship(4, [2, 0], 1)
    computer.put_ship(3, [4, 2], 0)
    computer.put_ship(3, [6, 4], 1)
    computer.put_ship(2, [8, 8], 0)


def computer_open_cell(cell):
    sea1[cell].open()
    if isinstance(sea1[cell].content, player.game.ShipPart):
        grid1[cell[0]][cell[1]] = 3
        draw_board()
        pygame.display.flip()
        return False
    else:
        grid1[cell[0]][cell[1]] = 4
        draw_board()
        pygame.display.flip()
        return True


def find_neighbours(field):
    return [[field[0] - 1, field[1]],
            [field[0] + 1, field[1]],
            [field[0], field[1] - 1],
            [field[0], field[1] + 1]]

#TODO test computer move
def computer_make_move():
    closed_fields = []
    hit_ships = []

    for row in range(10):
        for column in range(10):
            fill = sea1[[row, column]].content
            if grid1[row][column] in [0, 5]:
                closed_fields.append([row, column])
            elif grid1[row][column] == 3 and not fill.is_part_of_sunk_ship():
                hit_ships.append([row, column])

    for field in hit_ships:
        neighbours = find_neighbours(field)
        up = neighbours[0]
        down = neighbours[1]
        left = neighbours[2]
        right = neighbours[3]

        cell = None

        if up in hit_ships and down in closed_fields:
            cell = down
        elif down in hit_ships and up in closed_fields:
            cell = up
        elif left in hit_ships and right in closed_fields:
            cell = right
        elif right in hit_ships and left in closed_fields:
            cell = left

        if cell:
            return computer_open_cell(cell)

    for field in hit_ships:
        for cell in find_neighbours(field):
            if cell in closed_fields:
                return computer_open_cell(cell)

    move = choice(closed_fields)
    return computer_open_cell(move)
