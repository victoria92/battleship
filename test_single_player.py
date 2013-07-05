import unittest

import single_player

class SinglePlayerTest(unittest.TestCase):
    def test_put_one_ship(self):
        victoria = single_player.player.Player(10, 1)
        self.assertTrue(single_player.put_one_ship(victoria, [0,0], 3, 0, 20, 3))
        self.assertEqual(single_player.grid1[0], [5,5,5,0,0,0,0,0,0,0])

    def test_ignore_ships_on_same_place(self):
        victoria = single_player.player.Player(10, 2)
        single_player.put_one_ship(victoria, [0,0], 3, 0, 20, 3)
        single_player.put_one_ship(victoria, [0,0], 4, 0, 20, 3)
        self.assertEqual(single_player.grid1[0], [5,5,5,0,0,0,0,0,0,0])

    def test_ignore_ships_outside_the_sea(self):
        self.assertFalse(single_player.put_one_ship(single_player.player1, [11,5], 5, 0, 20, 3))
        self.assertEqual(single_player.grid1[0], [5,5,5,0,0,0,0,0,0,0])

    def test_player_make_move(self):
        single_player.put_one_ship(single_player.player1, [0,0], 3, 0, 20, 3)
        single_player.player.game.Ship(3, single_player.sea2, [8,0], 0)
        self.assertTrue(single_player.player_make_move([300,189], 20, 3))
        single_player.player_make_move([323,189], 20, 3)
        single_player.player_make_move([346,189], 20, 3)
        self.assertEqual(single_player.grid2[8][0], 1)
        self.assertFalse(single_player.player_make_move([367,215], 20, 3))
        self.assertEqual(single_player.grid2[8][5], 0)

    def test_computer_open_cell(self):
        single_player.player.game.Ship(3, single_player.sea1, [4,4], 0)
        single_player.computer_open_cell([4,4])
        single_player.computer_open_cell([3,3])
        self.assertEqual(single_player.grid1[4][4], 3)
        self.assertEqual(single_player.grid1[3][3], 4)

    def test_computer_make_move(self):
        single_player.put_one_ship(single_player.player1, [8,8], 3, 0, 20, 3)
        single_player.computer_open_cell([0,0])
        self.assertTrue(single_player.computer_make_move())
        grid = single_player.grid1
        self.assertTrue(grid[0][1] == 3 or grid[1][0] == 4)
        single_player.computer_make_move()
        self.assertTrue(grid[0][1] == 3)
        single_player.computer_make_move()
        self.assertTrue(grid[0][2] == 3)

    def test_computer_make_random_move(self):
        single_player.computer_make_move()
        sum_grid = sum([sum(row) for row in single_player.grid1])
        self.assertEqual(sum_grid, 17)

if __name__ == '__main__':
    unittest.main()