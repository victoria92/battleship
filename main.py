import single_player
import pygame
import colors


size = 20
margin = 3
end = False
#clock = pygame.time.Clock

grid1 = single_player.grid1
grid2 = single_player.grid2
screen = single_player.screen


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


def draw_put_ships_board(width, height):
    #screen.fill(colors.white)
    color = colors.blue
    draw_board()

    pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen,
                     colors.gray,
                     [pos[0] - size/2,
                     pos[1] - size/2,
                     width*(size+margin),
                     height*(size+margin)])
    pygame.display.flip()


def put_your_ships(new_player):

    ships = [2, 3, 3, 4, 5]
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
                    if single_player.put_one_ship(new_player, pos, ships[-1], direction, size, margin):
                        ships.pop()

def win_window(winner):
    dimension = [200, 200]
    screen = pygame.display.set_mode(dimension)
    pygame.display.set_caption("Winner")

    if winner == single_player.player1:
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render("You win!", 1, (255, 255, 0))
        screen.blit(label, (80, 80))
    else:
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render("You loose!", 1, (255, 255, 0))
        screen.blit(label, (80, 80))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


turn = True
put_your_ships(single_player.player1)
single_player.computer_put_his_ships()


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
                turn = single_player.player_make_move(pos, size, margin)
                draw_board()
                if single_player.computer.check_ships():
                    win_window(single_player.player1)

    while not turn:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            turn = single_player.computer_make_move()
            draw_board()
            if single_player.player1.check_ships():
                win_window(single_player.computer)

    #clock.tick(20)

pygame.quit()