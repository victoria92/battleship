import pygame
import player


black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

size = 20
margin = 3

player1 = player.Player(10, 5)
sea1 = player1.sea
computer = player.Player(10, 5)
sea2 = computer.sea

player1.put_ship(3, [0, 0], 0)


pygame.init()

dimension = [600, 255]
screen=pygame.display.set_mode(dimension)
pygame.display.set_caption("Battle ship")


clock = pygame.time.Clock()

def draw_board():
    color = blue
    for row in range(10):
        for column in range(10):
            if sea1[[row, column]].is_open:
                if isinstance(sea1[[row, column]].content, player.game.ShipPart):
                    color = red
                else:
                    color = green
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

    pygame.display.flip()


def put_your_ships(player):
    draw_board()
    ships = [2,3,3,4,5]

    while ships != []:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (size + margin)
                    row = pos[1] // (size + margin)
                    if(column < 10 and row < 10):
                        player.put_ship(ships.pop(), [row, column], 0)


turn = True
last_turn = None

put_your_ships(player1)

while True:

    screen.fill(white)
    draw_board()

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
                if(column < 10 and row < 10):
                    sea2[[row, column]].open()
                    last_turn = [row, column]
                    #print("Click ", pos, "Grid coordinates: ", row, column)

                    screen.fill(white)
                    draw_board()

                    if last_turn and not isinstance(sea2[last_turn].content, player.game.ShipPart):
                        turn = False
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

                    screen.fill(white)

                    draw_board()

                    if last_turn and not isinstance(sea1[last_turn].content, player.game.ShipPart):
                        turn = True
                else:
                    print("It's not your turn!")

    clock.tick(20)

pygame.quit()