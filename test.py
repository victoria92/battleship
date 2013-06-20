import unittest

import game

class FieldTest(unittest.TestCase):
    def test_check(self):
        self.assertTrue(True)

    def test_create_empty_field(self):
        field = game.Field()
        self.assertEqual(field.content, None)
        self.assertFalse(field.is_open)

    def test_create_field_with_ship_part(self):
        field = game.Field(game.ShipPart(game.Ship(3, game.Sea(), [1, 3], 0)))
        self.assertIsInstance(field.content, game.ShipPart)
        self.assertFalse(field.is_open)

    def test_open_field(self):
        field = game.Field()
        field.open()
        self.assertTrue(field.is_open)

    def test_with_wrong_parameters(self):
        self.assertRaises(TypeError, game.Field, 1)


class ShipPartTest(unittest.TestCase):
    def is_right_initialized(self):
        sea = game.Sea()
        ship = game.Ship(3, sea, [1, 3], 0)
        self.assertEqual(sea[[1, 3]].content.ship, ship)


class ShipTest(unittest.TestCase):
    def test_create_new_ship(self):
        sea = game.Sea()
        ship = game.Ship(3, sea, [1, 3], 0)
        self.assertEqual(ship.size, 3)
        self.assertEqual(ship.sea, sea)
        self.assertEqual(ship.location, [[1, 3], [1, 4], [1, 5]])

    def test_sink(self):
        sea = game.Sea()
        ship = game.Ship(3, sea, [1, 3], 0)
        sea[[1, 3]].open()
        sea[[1, 4]].open()
        sea[[1, 5]].open()
        self.assertTrue(ship.is_sunk())


class SeaTest(unittest.TestCase):
    def test_create_new_sea(self):
        sea = game.Sea()
        self.assertEqual(sea.size, 10)

        sea = game.Sea(20)
        self.assertEqual(sea.size, 20)

    def test_get_field_content(self):
        sea = game.Sea()
        self.assertIsInstance(sea[[3, 3]], game.Field)

    def test_put_field_content(self):
        sea = game.Sea()
        ship_part = game.ShipPart(game.Ship(3, game.Sea(), [1, 3], 0))
        sea[[3, 3]] = ship_part
        self.assertEqual(sea[[3, 3]], ship_part)

    def test_validate_coordinates(self):
        sea = game.Sea()
        self.assertTrue(sea.is_valid_coordinates(5, 6))
        self.assertFalse(sea.is_valid_coordinates(15, 6))

    def test_raise_index_error(self):
        sea = game.Sea()
        self.assertRaises(IndexError, sea.__getitem__, [1, 11])

    def test_representation(self):
        sea = game.Sea(3)
        game.Ship(2, sea, [1, 0], 1)
        sea[[0,0]].open()
        sea[[1,0]].open()
        self.assertEqual(sea.represent(), "N X X \nY X X \nX X X \n")



class GameTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()