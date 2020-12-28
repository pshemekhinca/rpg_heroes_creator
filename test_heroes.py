import unittest
from heroes import Hero, get_hero_of_race
from unittest import expectedFailure


class AccountTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.create_kind = 'elf'
        sample = Hero(get_hero_of_race(self.create_kind), self.create_kind)
        sample2 = Hero(get_hero_of_race(self.create_kind), self.create_kind)
        self.race = self.create_kind
        self.power = 10
        self.agile = 10
        self.durability = 10
        self.iq = 10
        self.intuition = 10
        self.charisma = 10
        self.hero = sample.get_hero()
        self.hero2 = sample2.get_hero()

    def test_hero_instance_created_as_dictionary(self):
        self.assertIsInstance(self.hero, dict)

    def test_heroes_created_with_random_name(self):
        name1 = self.hero['name']
        name2 = self.hero2['name']
        self.assertNotEqual(name1, name2)

    def test_random_list_of_item_for_each_hero(self):
        items_list1 = self.hero['items']
        items_list2 = self.hero2['items']
        self.assertNotEqual(items_list1, items_list2)
