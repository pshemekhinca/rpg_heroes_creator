import random
import csv


def get_hero_of_race(x):
    with open(f'txt_files/race_names.csv', 'r') as f:
        reader = csv.reader(f)
        name = random.choice([row[x] for row in reader])
        return name


class Hero:
    """ Creates hero of given race with random name and random items set """

    def __init__(self, race: str, name: str, power=10, agile=10, durability=10, intellect=10, intuition=10,
                 charisma=10):
        self.race = race
        self.name = name
        self.power = power
        self.agile = agile
        self.durability = durability
        self.intellect = intellect
        self.intuition = intuition
        self.charisma = charisma
        self.items = self.get_hero_items()

    def get_hero(self):
        hero = {'name': self.name, 'race': self.race, 'power': self.power, 'agile': self.agile,
                'durability': self.durability, 'intellect': self.intellect, 'intuition': self.intuition,
                'charisma': self.charisma, 'items': self.items}
        return hero

    def get_hero_items(self):
        if self.race == 'dwarf' or self.race == 'human':
            kind1, kind2 = 'close', 'distance'
        else:
            kind1, kind2 = 'distance', 'close'

        with open(f'txt_files/{kind1}_weapon.txt') as k1:
            main_weapon = k1.read().splitlines()
            first_weapon = list(random.sample(main_weapon, 2))
        with open(f'txt_files/{kind2}_weapon.txt') as k2:
            side_weapons = k2.read().splitlines()
            secondary_weapon = list(random.sample(side_weapons, 1))
        return first_weapon + secondary_weapon


if __name__ == '__main__':
    create_kind = int(input("\nWhat race you choose for your hero: \n1. Human\n2. Elf\n3. Dwarf\n4. Shifter"
                            "\n\t\t\tpick the number:"))
    race = {1: 'human', 2: 'elf', 3: 'dwarf', 4: 'shifter'}
    sample_hero = Hero(race[create_kind], get_hero_of_race(create_kind - 1))
    print(sample_hero.get_hero())
