import unittest
from heroes import Hero, get_name, get_hero_items
from unittest import expectedFailure


class AccountTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.name = 'Gromek'
        self.power = 10
        self.agile = 10
        self.armor = 10
        self.iq = 10
        self.intuition = 10
        self.charisma = 10

    def test_hero_instance_created_as_dictionary(self):
        sample = Hero(self.name)
        hero = sample.get_hero()
        self.assertIsInstance(hero, dict)

    def test_two_heroes_created_with_random_name(self):
        hero1 = Hero(get_name('dwarf'))
        hero2 = Hero(get_name('dwarf'))
        self.assertNotEqual(hero1, hero2)

    def test_random_list_of_item_for_each_hero(self):
        items_list1 = Hero(get_hero_items('close'))
        print(items_list1)
        items_list2 = Hero(get_hero_items('close'))
        print(items_list2)
        self.assertNotEqual(items_list1, items_list2)
