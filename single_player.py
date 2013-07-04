import pygame
import player
from random import choice


black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (100, 100, 100)
orange = (255, 165, 0)
dark_blue = (0, 0, 128)

size = 20
margin = 3

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


clock = pygame.time.Clock()

colors = {
    0: blue,
    1: red,
    2: green,
    3: orange,
    4: dark_blue,
    5: gray
}

def draw_board():

    screen.fill(white)
    for row in range(10):
        for column in range(10):
            pygame.draw.rect(screen,
                             colors[grid1[row][column]],
                             [(margin+size)*column+margin,
                              (margin+size)*row+margin,
                              size,
                              size])

    for row in range(10):
        for column in range(10):
            pygame.draw.rect(screen,
                             colors[grid2[row][column]],
                             [(margin+size)*(column+13)+margin,
                              (margin+size)*row+margin,
                              size,
                              size])


#TODO leave player's ships and make them orange if computer hit them and AI
def draw_put_ships_board(width, height):
    screen.fill(white)
    color = blue
    draw_board()

    pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen, gray, [pos[0] - size/2,
                                               pos[1] - size/2,
                                               width*(size+margin),
                                               height*(size+margin)])
    pygame.display.flip()


def put_one_ship(new_player, position, ship, direction):
    column = position[0] // (size + margin)
    row = position[1] // (size + margin)
    if(column < 10 and row < 10):
        try:
            new_player.put_ship(ship, [row, column], direction)
            for coords in new_player.ships[-1].location:
                grid1[coords[0]][coords[1]] = 5
            return True
        except player.game.FullSquareError:
            print("This place is already full")
            return False
        except IndexError:
            print("You must stay in your sea")
            return False

def put_your_ships(new_player):

    ships = [2,3,3,4,5]
    direction = 0

    while ships != []:
        ship_size = [ships[-1], 1]


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                direction = 1 - direction
            draw_put_ships_board(ship_size[direction], ship_size[1-direction])
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if put_one_ship(new_player, pos, ships[-1], direction):
                        ships.pop()


turn = True


def player_make_move(position):
    turn = True
    column = position[0] // (size + margin) - 13
    row = position[1] // (size + margin)
    print(row, column)
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
    else:
        print("It's not your turn!")

    return turn


def computer_put_his_ships():
    player.game.Ship(5, sea2, [1,4], 0)
    player.game.Ship(4, sea2, [2,0], 1)
    player.game.Ship(3, sea2, [4,2], 0)
    player.game.Ship(3, sea2, [6,4], 1)
    player.game.Ship(2, sea2, [8,8], 0)


def computer_make_move():
    closed_fields = []
    hit_ships = []

    for row in range(10):
        for column in range(10):
            if grid1[row][column] in [0, 5]:
                closed_fields.append([row, column])
            elif grid1[row][column] == 3 and not sea1[[row, column]].content.is_part_of_sunk_ship():
                hit_ships.append([row, column])
#TODO if next to it is opened to open opposite
    for field in hit_ships:
        neighbours = [[field[0] - 1, field[1]],
                      [field[0] + 1, field[1]],
                      [field[0], field[1] - 1],
                      [field[0], field[1] + 1]]
        for cell in neighbours:
            if cell in closed_fields:
                sea1[cell].open()
                if isinstance(sea1[cell].content, player.game.ShipPart):
                    grid1[cell[0]][cell[1]] = 3
                    return False
                else:
                    grid1[cell[0]][cell[1]] = 4
                    return True

    move = choice(closed_fields)
    sea1[move].open()
    if isinstance(sea1[move].content, player.game.ShipPart):
        grid1[move[0]][move[1]] = 3
        return False
    else:
        grid1[move[0]][move[1]] = 4
        return True



put_your_ships(player1)
computer_put_his_ships()

while True:

    draw_board()
    pygame.display.flip()

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    while turn:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                turn = player_make_move(pos)

    while not turn:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            turn = computer_make_move()

    clock.tick(20)

pygame.quit()