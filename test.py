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
        ship_part = game.ShipPart()
        field = game.Field(ship_part)
        self.assertEqual(field.content, ship_part) #with isinstance
        self.assertFalse(field.is_open)

    def test_open_field(self):
        field = game.Field()
        field.open()
        self.assertTrue(field.is_open)


class ShipPartTest(unittest.TestCase):
    pass


class Ship(unittest.TestCase):
    pass


class Sea(unittest.TestCase):
    pass


class Game(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()