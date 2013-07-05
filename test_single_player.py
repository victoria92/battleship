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
        single_player.put_one_ship(single_player.player1, [0,0], 11, 0, 20, 3)
        self.assertEqual(single_player.grid1[0], [5,5,5,0,0,0,0,0,0,0])

    def test_player_make_move(self):
        single_player.put_one_ship(single_player.player1, [0,0], 3, 0, 20, 3)
        single_player.player.game.Ship(3, single_player.sea2, [8,0], 0)
        self.assertTrue(single_player.player_make_move([300,189], 20, 3))
        self.assertFalse(single_player.player_make_move([367,215], 20, 3))


if __name__ == '__main__':
    unittest.main()