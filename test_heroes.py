import unittest
from heroes import Hero, get_hero_of_race
from unittest import expectedFailure


class AccountTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.create_kind = 'shifter'
        sample = Hero(get_hero_of_race(self.create_kind), self.create_kind)
        sample2 = Hero(get_hero_of_race(self.create_kind), self.create_kind)
        self.hero = sample.get_hero()
        self.hero2 = sample2.get_hero()

    def test_hero_instance_created_as_dictionary(self):
        self.assertIsInstance(self.hero, dict)

    def test_heroes_created_with_different_random_name(self):
        self.assertNotEqual(self.hero['name'], self.hero2['name'])

    def test_random_list_of_item_for_each_hero(self):
        self.assertNotEqual(self.hero['items'], self.hero2['items'])
