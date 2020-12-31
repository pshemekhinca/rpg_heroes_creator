import random
import csv


def get_hero_of_race(col_numb):
    with open('txt_files/race_names.csv', 'r') as f:
        reader = csv.reader(f)
        name = random.choice([row[col_numb] for row in reader])
        print(name)
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
            kind1, kind2 = 0, 1
        else:
            kind1, kind2 = 1, 0

        with open('txt_files/weapons.csv', 'r') as weapon:
            reader = csv.reader(weapon)
            main_weapon = random.sample([row[kind1] for row in reader], 2)
        with open('txt_files/weapons.csv', 'r') as weapon:
            reader = csv.reader(weapon)
            side_weapon = random.sample([row[kind2] for row in reader], 1)
        return main_weapon + side_weapon


if __name__ == '__main__':
    create_kind = int(input("\nWhat race you choose for your hero: \n1. Human\n2. Elf\n3. Dwarf\n4. Shifter"
                            "\n\t\t\tpick the number:"))
    race = {1: 'human', 2: 'elf', 3: 'dwarf', 4: 'shifter'}

    sample_hero = Hero(race[create_kind], get_hero_of_race(create_kind - 1))
    print(sample_hero.get_hero())
