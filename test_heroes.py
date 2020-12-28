import unittest
from heroes import Hero
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

#
# @pytest.fixture
# def hero():
#     return Hero('Merlin')
#
#
# def test_hero_starting_level(hero):
#     """Initial level should be eql 1"""
#     assert 1 == hero.level
#
#
# def test_hero_level_up(hero):
#     """Level should increase every + 1000 """
#     hero.add_exp(2500)
#     assert 3 == hero.level
#
#
# def test_hero_exp_increase(hero):
#     """Experience should accumulate"""
#     hero.add_exp(2500)
#     hero.add_exp(200)
#     assert 2700 == hero.exp
