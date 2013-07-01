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

player1.put_ship(3, [1, 3], 0)


pygame.init()

dimension = [600, 255]
screen=pygame.display.set_mode(dimension)
pygame.display.set_caption("Battle ship")


done = False


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


turn = True
last_turn = None

while done == False:

    draw_board()

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    while turn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (size + margin) - 13
                row = pos[1] // (size + margin)
                sea2[[row, column]].open()
                last_turn = [row, column]
                print("Click ", pos, "Grid coordinates: ", row, column)

        screen.fill(white)

        draw_board()

        if last_turn and not isinstance(sea2[last_turn], player.game.ShipPart):
            turn = False

    clock.tick(20)

    pygame.display.flip()

pygame.quit()