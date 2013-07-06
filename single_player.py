import pygame
import player
import colors
from itertools import dropwhile
from random import choice


pygame.init()
dimension = [600, 255]
screen = pygame.display.set_mode(dimension)
pygame.display.set_caption("Battle ship")
size = 20
margin = 3


def draw_board(grid1, grid2):

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


def put_one_ship(new_player, position, ship, direction, grid1):
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


def player_make_move(position, sea2, grid2, grid1):
    turn = True
    column = position[0] // (size + margin) - 13
    row = position[1] // (size + margin)
    if 0 <= column < 10 and 0 <= row < 10:
        sea2[[row, column]].open()
        if isinstance(sea2[row, column].content, player.game.ShipPart):
            grid2[row][column] = 1
        else:
            grid2[row][column] = 2
        draw_board(grid1, grid2)
        pygame.display.flip()
        if grid2[row][column] == 2:
            turn = False
        else:
            if sea2[[row, column]].content.is_part_of_sunk_ship():
                print("You destroyed this ship!")
            else:
                print("You hit it!")

    return turn


def is_possible(position, size, direction, sea2):

    if direction:
        for i in range(size):
            if position[0] + i > 9:
                return False
            else:
                if sea2[[position[0] + i, position[1]]].content:
                    return False
        return True

    else:
        for i in range(size):
            if position[1] + i > 9:
                return False
            else:
                if sea2[[position[0], position[1] + i]].content:
                    return False
        return True


def computer_put_his_ships(computer):
    ships = [2, 3, 3, 4, 5]

    for size in ships:
        possible_positions = []
        for row in range(10):
            for column in range(10):
                if is_possible([row, column], size, 0, computer.sea):
                    possible_positions.append((size, [row, column], 0))
                if is_possible([row, column], size, 1, computer.sea):
                    possible_positions.append((size, [row, column], 1))
        position = choice(possible_positions)
        computer.put_ship(position[0], position[1], position[2])


def computer_open_cell(cell, grid1, sea1, grid2):
    sea1[cell].open()
    if isinstance(sea1[cell].content, player.game.ShipPart):
        grid1[cell[0]][cell[1]] = 3
        draw_board(grid1, grid2)
        pygame.display.flip()
        return False
    else:
        grid1[cell[0]][cell[1]] = 4
        draw_board(grid1, grid2)
        pygame.display.flip()
        return True


def find_neighbours(field):
    return [[field[0] - 1, field[1]],
            [field[0] + 1, field[1]],
            [field[0], field[1] - 1],
            [field[0], field[1] + 1]]


def closed_neighbours(cell, grid, smallest_ship):
    count = 0

    for dif in range(-smallest_ship + 1, smallest_ship):
        if 0 <= cell[1] + dif < 10 and grid[cell[0]][cell[1] + dif] in [0, 5]:
            count += 1
        if 0 <= cell[0] + dif < 10 and grid[cell[0] + dif][cell[1]] in [0, 5]:
            count += 1

    return count


def sort_closed_fields(closed_fields, grid1, smallest_ship):

    def criterion(cell):  # ne na dve mesta i testove!!!
        return closed_neighbours(cell, grid1, smallest_ship)

    return sorted(closed_fields, key=lambda cell: criterion(cell))


def computer_make_move(player1, sea1, grid1, grid2):
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
            return computer_open_cell(cell, grid1, sea1, grid2)

    for field in hit_ships:
        for cell in find_neighbours(field):
            if cell in closed_fields:
                return computer_open_cell(cell, grid1, sea1, grid2)

    def criterion(cell):
        return closed_neighbours(cell, grid1, smallest_ship)

    left_ships = filter(lambda ship: not ship.is_sunk(), player1.ships)
    if left_ships != []:
        smallest_ship = min([ship.size for ship in left_ships])
        ordered = sort_closed_fields(closed_fields, grid1, smallest_ship)
        maximum = criterion(ordered[-1])
        choices = dropwhile(lambda cell: criterion(cell) != maximum, ordered)
        move = choice(list(choices))
        return computer_open_cell(move, grid1, sea1, grid2)
