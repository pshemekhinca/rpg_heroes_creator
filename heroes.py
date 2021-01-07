import random
import csv
import json
from itertools import chain


def file_to_write():
    with open('db_files/names_race.json', 'w') as f:
        reader = json.load(f)
        return reader


def file_to_read_name():
    with open('db_files/names_race.json', 'r') as f:
        writer = json.load(f)
        return writer


def file_to_read_weapon():
    with open('db_files/weapons.json', 'r') as weapon:
        reader = json.load(weapon)
        return reader


class Hero:
    """ Creates hero of given race with random name and random items set """

    def __init__(self, race: str, power=100, agile=100, durability=100, intellect=100, intuition=100, charisma=100):
        self.race = race
        self.name = self.get_name_of_race()
        self.power = power
        self.agile = agile
        self.durability = durability
        self.intellect = intellect
        self.intuition = intuition
        self.charisma = charisma
        self.items = self.get_hero_items()

    def get_name_of_race(self):
        reader = file_to_read_name()
        name = random.choice(list(reader[self.race].values()))
        return name

    def get_hero(self):
        one_hero = {'name': self.name, 'race': self.race, 'power': self.power,
                    'agile': self.agile, 'durability': self.durability, 'intellect': self.intellect,
                    'intuition': self.intuition, 'charisma': self.charisma, 'items': self.items}
        return one_hero

    # def get_hero_items(self):
    #     if self.race == 'dwarf' or self.race == 'human':
    #         kind1, kind2 = 0, 1
    #     else:
    #         kind1, kind2 = 1, 0
    #     with open('db_files/weapons.csv', 'r') as weapon:
    #         reader = csv.reader(weapon)
    #         main_weapon = random.sample([row[kind1] for row in reader], 2)
    #     with open('db_files/weapons.csv', 'r') as weapon:
    #         reader = csv.reader(weapon)
    #         side_weapon = random.sample([row[kind2] for row in reader], 1)
    #     return main_weapon + side_weapon

    def get_hero_items(self):
        if self.race == 'dwarf' or self.race == 'human':
            kind1, kind2 = 0, 1
        else:
            kind1, kind2 = 1, 0
        with open('db_files/weapons.csv', 'r') as weapon:
            reader = csv.reader(weapon)
            main_weapon = random.sample([row[kind1] for row in reader], 2)
        with open('db_files/weapons.csv', 'r') as weapon:
            reader = csv.reader(weapon)
            side_weapon = random.sample([row[kind2] for row in reader], 1)
        return main_weapon + side_weapon

class CreateTeam(Hero):
    """ Creates heroes team of given race under the chosen name"""

    def __init__(self, team_name: str, race: str, heroes_no: int):
        self.team_name = team_name
        self.heroes_no = heroes_no
        self.race = race
        self.team_list = []

    def get_team_of_race(self):
        team_list = [self.team_list.append(Hero(self.race).get_hero()) for _ in range(self.heroes_no)]
        return self.team_list

    def __repr__(self):
        output = "\n".join(map(str, self.get_team_of_race()))
        return f"\n{self.team_name}:\n{output}"


if __name__ == '__main__':
    create_kind = 3
    race = {1: 'human', 2: 'elf', 3: 'dwarf', 4: 'shifter'}
    race_choice = race[create_kind]
    many_heroes = 3

    sample_h = Hero(race_choice)
    print(sample_h.get_hero())
    #
    # sample_team = CreateTeam('SampleTeam', race_choice, many_heroes)
    # print(sample_team)
