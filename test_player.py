import player
import unittest


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
        victoria.put_ship(3, [0, 1], 0)
        self.assertFalse(victoria.ready)
        victoria.put_ship(2, [2, 1], 0)
        self.assertTrue(victoria.ready)

    def test_check_ships(self):
        victoria = player.Player(5, 1)
        victoria.put_ship(1, [1, 1], 0)
        victoria.sea[[1, 1]].open()
        self.assertTrue(victoria.check_ships())

        nevena = player.Player(5, 2)
        nevena.put_ship(1, [1, 1], 0)
        nevena.put_ship(1, [2, 2], 0)
        nevena.sea[[1, 1]].open()
        self.assertFalse(nevena.check_ships())


if __name__ == '__main__':
    unittest.main()
