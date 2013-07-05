import single_player
import pygame


single_player.put_your_ships(single_player.player1)
single_player.computer_put_his_ships()
end = False
clock = pygame.time.Clock()

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


while True:

    single_player.draw_board()
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
                turn = single_player.player_make_move(pos)
                if single_player.computer.check_ships():
                    win_window(single_player.player1)

    while not turn:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            turn = single_player.computer_make_move()
            if single_player.player1.check_ships():
                win_window(single_player.computer)

    clock.tick(20)

pygame.quit()