import player

import unittest
#raise error if there is already ship or it's next to other ship
class PlayerTest(unittest.TestCase):
    def test_initialize_player(self):
        victoria = player.Player(5, 5)
        self.assertIsInstance(victoria.sea, player.game.Sea)
        self.assertEqual(victoria.sea.size, 5)
        self.assertEqual(victoria.ships, [])
        self.assertEqual(victoria.ships_count, 5)
        self.assertFalse(victoria.ready)

    def test_put_ship(self):
        victoria = player.Player(5, 2)
        victoria.put_ship(3, [0,1], 0)
        self.assertFalse(victoria.ready)
        victoria.put_ship(2, [2,1], 0)
        self.assertTrue(victoria.ready)


if __name__ == '__main__':
    unittest.main()