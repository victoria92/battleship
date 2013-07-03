import pygame
import player


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

# player1.put_ship(3, [0, 0], 0)


pygame.init()

dimension = [600, 255]
screen=pygame.display.set_mode(dimension)
pygame.display.set_caption("Battle ship")


clock = pygame.time.Clock()


def draw_board():

    screen.fill(white)
    color = blue
    for row in range(10):
        for column in range(10):
            if isinstance(sea1[[row, column]].content, player.game.ShipPart):
                if sea1[[row, column]].is_open:
                    color = orange
                else:
                    color = gray
            else:
                if sea1[[row, column]].is_open:
                    color = dark_blue
                else:
                    color = blue
            pygame.draw.rect(screen,
                             color,
                             [(margin+size)*column+margin,
                              (margin+size)*row+margin,
                              size,
                              size])

    color = blue
    for row in range(10):
        for column in range(10):
            if sea2[[row, column]].is_open:
                if isinstance(sea2[[row, column]].content, player.game.ShipPart):
                    color = red
                else:
                    color = green
            else:
                color = blue
            pygame.draw.rect(screen,
                             color,
                             [(margin+size)*(column+13)+margin,
                              (margin+size)*row+margin,
                              size,
                              size])

    #pygame.display.flip()

#TODO leave player's ships and make them orange if computer hit them and AI
def draw_put_ships_board(width, height):
    screen.fill(white)
    color = blue

    for row in range(10):
        for column in range(10):
            if isinstance(sea1[[row, column]].content, player.game.ShipPart):
                color = gray
            else:
                color = blue
            pygame.draw.rect(screen,
                             color,
                             [(margin+size)*column+margin,
                              (margin+size)*row+margin,
                              size,
                              size])

    pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen, gray, [pos[0] - size/2,
                                               pos[1] - size/2,
                                               width*(size+margin),
                                               height*(size+margin)])
    pygame.display.flip()


def put_your_ships(new_player):
    #draw_board()

    # myfont = pygame.font.SysFont("monospace", 15)
    # label = myfont.render("baba", 1, (255,0,0))
    # screen.blit(label, (500, 240))

    ships = [2,3,3,4,5] #add more ships
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
                    column = pos[0] // (size + margin)
                    row = pos[1] // (size + margin)
                    if(column < 10 and row < 10):
                        try:
                            new_player.put_ship(ships.pop(), [row, column], direction)
                        except player.game.FullSquareError:
                            print("This place is already full")
                        except IndexError:
                            print("You must stay in your sea")


turn = True
last_turn = None

put_your_ships(player1)

while True:

    # draw_board()
    # pygame.display.flip()
    # myfont = pygame.font.SysFont("monospace", 15)
    # label = myfont.render("baba", 1, (255,255,0))
    # screen.blit(label, (400, 400))

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    while turn:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (size + margin) - 13
                row = pos[1] // (size + margin)
                if 0 <= column < 10 and 0 <= row < 10:
                    sea2[[row, column]].open()
                    last_turn = [row, column]
                    #print("Click ", pos, "Grid coordinates: ", row, column)

                    draw_board()
                    pygame.display.flip()

                    # if last_turn and not isinstance(sea2[last_turn].content, player.game.ShipPart):
                    #     turn = False

                    if last_turn:
                        if not isinstance(sea2[last_turn].content, player.game.ShipPart):
                            turn = False
                        else:
                            if sea2[last_turn].content.is_part_of_sunk_ship():
                                print("You destroyed this ship!")
                            else:
                                print("You hit it!")
                else:
                    print("It's not your turn!")

    while not turn:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (size + margin)
                row = pos[1] // (size + margin)
                if column < 10 and row < 10:
                    sea1[[row, column]].open()
                    last_turn = [row, column]
                    print("Click ", pos, "Grid coordinates: ", row, column)


                    draw_board()
                    pygame.display.flip()

                    if last_turn:
                        if not isinstance(sea1[last_turn].content, player.game.ShipPart):
                            turn = True
                        else:
                            if sea1[last_turn].content.is_part_of_sunk_ship():
                                print("You destroyed this ship!")
                            else:
                                print("You hit it!")
                else:
                    print("It's not your turn!")

    clock.tick(20)

pygame.quit()