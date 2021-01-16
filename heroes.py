import random
import json


def file_to_write():
    with open('db_files/names_race.json', 'w') as f:
        writer = json.load(f)
        return writer


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

    def get_hero_items(self):
        reader = file_to_read_weapon()
        if self.race == 'dwarf' or self.race == 'human':
            weapon1, weapon2 = reader['close_weapon'], reader['range_weapon']
            pts_1, pts_2 = reader['close_pts'], reader['range_pts']
        else:
            weapon1, weapon2 = reader['range_weapon'], reader['close_weapon']
            pts_1, pts_2 = reader['range_pts'], reader['close_pts']

        weapon_set = {}
        main_weapon_key = random.sample(weapon1.items(), 2)
        weapon_set[main_weapon_key[0][1]] = pts_1[main_weapon_key[0][0]]
        weapon_set[main_weapon_key[1][1]] = pts_1[main_weapon_key[1][0]]
        side_weapon_key = random.sample(weapon2.items(), 1)
        weapon_set[side_weapon_key[0][1]] = pts_2[side_weapon_key[0][0]]

        return weapon_set

    def get_hero(self):
        return {'name': self.name, 'race': self.race, 'power': self.power, 'agile': self.agile,
                'durability': self.durability, 'intellect': self.intellect, 'intuition': self.intuition,
                'charisma': self.charisma, 'items': self.items}


class CreateRaceTeam(Hero):
    """ Creates heroes team of given race under the chosen name"""

    def __init__(self, race: str, heroes_no: int):
        super().__init__(race)
        self.team_name = ''
        self.heroes_no = heroes_no
        self.race = race
        self.team_list = []

    def get_team_of_race(self):
        team_list = [self.team_list.append(Hero(self.race).get_hero()) for _ in range(self.heroes_no)]
        return self.team_list

    # def __repr__(self):
    #     out_team ={}
    #     for k, v in self.get_team_of_race():
    #         out_team[k]=v
    #     # a = dict(self.get_team_of_race())
    #     return out_team
    # #     output = "\n".join(map(str, self.get_team_of_race()))
    # #     return f"\n{output}"


if __name__ == '__main__':
    create_kind = 1
    race = {1: 'human', 2: 'elf', 3: 'dwarf', 4: 'shifter'}
    race_choice = race[create_kind]
    many_heroes = 3

    sample_team = CreateRaceTeam(race_choice, many_heroes)
    print(sample_team.get_team_of_race())
