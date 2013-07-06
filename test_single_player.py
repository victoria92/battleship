import unittest
import single_player
from single_player import put_one_ship, player_make_move, computer_make_move
from game import ShipPart


class SinglePlayerTest(unittest.TestCase):
    def test_put_one_ship(self):
        victoria = single_player.player.Player(10, 1)
        grid = [[0 for i in range(10)] for i in range(10)]
        self.assertTrue(put_one_ship(victoria, [0, 0], 3, 0, grid))
        self.assertEqual(grid[0], [5, 5, 5, 0, 0, 0, 0, 0, 0, 0])

    def test_ignore_ships_on_same_place(self):
        victoria = single_player.player.Player(10, 2)
        grid = [[0 for i in range(10)] for i in range(10)]
        put_one_ship(victoria, [0, 0], 3, 0, grid)
        self.assertFalse(put_one_ship(victoria, [0, 0], 4, 0, grid))
        self.assertEqual(grid[0], [5, 5, 5, 0, 0, 0, 0, 0, 0, 0])

    def test_ignore_ships_outside_the_sea(self):
        victoria = single_player.player.Player(10, 2)
        grid = [[0 for i in range(10)] for i in range(10)]
        self.assertFalse(put_one_ship(victoria, [400, 400], 5, 0, grid))

    def test_player_make_move(self):
        player1 = single_player.player.Player(10, 1)
        grid1 = [[0 for i in range(10)] for i in range(10)]
        sea2 = single_player.player.game.Sea()
        grid2 = [[0 for i in range(10)] for i in range(10)]
        put_one_ship(player1, [0, 0], 3, 0, grid1)
        single_player.player.game.Ship(3, sea2, [8, 0], 0)
        self.assertTrue(player_make_move([300, 189], sea2, grid2, grid1))
        single_player.player_make_move([323, 189], sea2, grid2, grid1)
        single_player.player_make_move([346, 189], sea2, grid2, grid1)
        self.assertEqual(grid2[8][0], 1)
        self.assertFalse(player_make_move([367, 215], sea2, grid2, grid1))
        self.assertEqual(grid2[8][5], 0)

    def test_computer_open_cell(self):
        sea1 = single_player.player.game.Sea()
        grid1 = [[0 for i in range(10)] for i in range(10)]
        grid2 = [[0 for i in range(10)] for i in range(10)]
        single_player.player.game.Ship(3, sea1, [4, 4], 0)
        single_player.computer_open_cell([4, 4], grid1, sea1, grid2)
        single_player.computer_open_cell([3, 3], grid1, sea1, grid2)
        self.assertEqual(grid1[4][4], 3)
        self.assertEqual(grid1[3][3], 4)

    def test_closed_neighbours(self):
        sea1 = single_player.player.game.Sea()
        grid1 = [[0 for i in range(10)] for i in range(10)]
        grid2 = [[0 for i in range(10)] for i in range(10)]
        single_player.computer_open_cell([3, 3], grid1, sea1, grid2)
        count34 = single_player.closed_neighbours([3, 4], grid1, 2)
        count88 = single_player.closed_neighbours([9, 9], grid1, 2)
        self.assertEqual(count34, 5)
        self.assertEqual(count88, 4)

    def test_computer_make_move(self):
        player1 = single_player.player.Player(10, 2)
        sea1 = player1.sea
        grid1 = [[0 for i in range(10)] for i in range(10)]
        grid2 = [[0 for i in range(10)] for i in range(10)]
        put_one_ship(player1, [8, 8], 3, 0, grid1)
        single_player.computer_open_cell([0, 0], grid1, sea1, grid2)
        self.assertTrue(computer_make_move(player1, sea1, grid1, grid2))
        self.assertTrue(grid1[0][1] == 3 or grid1[1][0] == 4)
        computer_make_move(player1, sea1, grid1, grid2)
        self.assertTrue(grid1[0][1] == 3)
        computer_make_move(player1, sea1, grid1, grid2)
        self.assertTrue(grid1[0][2] == 3)

    def test_computer_make_random_move(self):
        victoria = single_player.player.Player(10, 2)
        victoria.put_ship(3, [0, 0], 0)
        grid1 = [[0 for i in range(10)] for i in range(10)]
        grid2 = [[0 for i in range(10)] for i in range(10)]
        computer_make_move(victoria, victoria.sea, grid1, grid2)
        sum_grid = sum([sum(row) for row in grid1])
        self.assertEqual(sum_grid, 4)

    def test_is_possible(self):
        sea = single_player.player.game.Sea()
        self.assertTrue(single_player.is_possible([1, 1], 3, 0, sea))
        single_player.player.game.Ship(3, sea, [0, 0], 0)
        self.assertFalse(single_player.is_possible([0, 0], 2, 1, sea))

    def test_computer_put_his_ships(self):
        computer = single_player.player.Player(10, 5)
        single_player.computer_put_his_ships(computer)
        number_of_parts = 0
        for row in computer.sea.board:
            part = filter(lambda cell: isinstance(cell.content, ShipPart), row)
            number_of_parts += len(list(part))
        self.assertEqual(number_of_parts, 17)


# if __name__ == '__main__':
#     unittest.main()
