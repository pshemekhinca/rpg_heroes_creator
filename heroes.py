import random


def get_hero_of_race(race):
    with open(f'txt_files/name_{race}.txt') as f:
        names = f.read().splitlines()
        name = random.choice(names)
        return name


class Hero:
    def __init__(self, name: str, race: str, power=10, agile=10, durability=10, intellect=10, intuition=10, charisma=10):
        self.name = name
        self.race = race
        self.power = power
        self.agile = agile
        self.durability = durability
        self.intellect = intellect
        self.intuition = intuition
        self.charisma = charisma

    def get_hero(self):
        hero = {'name': self.name, 'race': self.race, 'power': self.power, 'agile': self.agile,
                'durability': self.durability, 'intellect': self.intellect, 'intuition': self.intuition, 'charisma': self.charisma,
                'items': self.get_hero_items()}
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
    # create_kind = input("What race do you want to have for your hero: ")
    create_kind = 'shifter'
    sample_hero = Hero(get_hero_of_race(create_kind), create_kind)
    print(sample_hero.get_hero())
