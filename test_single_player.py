import unittest

import single_player

class SinglePlayerTest(unittest.TestCase):
    def test_put_one_ship(self):
        victoria = single_player.player.Player(10, 1)
        self.assertTrue(single_player.put_one_ship(victoria, [0,0], 3, 0))
        self.assertEqual(single_player.grid1[0], [5,5,5,0,0,0,0,0,0,0])

    def test_ignore_ships_on_same_place(self):
        victoria = single_player.player.Player(10, 2)
        single_player.put_one_ship(victoria, [0,0], 3, 0)
        single_player.put_one_ship(victoria, [0,0], 4, 0)
        self.assertEqual(single_player.grid1[0], [5,5,5,0,0,0,0,0,0,0])


if __name__ == '__main__':
    unittest.main()