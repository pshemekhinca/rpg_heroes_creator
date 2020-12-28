import random


def get_name(race):
    with open(f'txt_files/name_{race}.txt') as f:
        names = f.read().splitlines()
        name = random.choice(names)
        return name


def get_hero_items(distance):
    if distance == 'close':
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


class Hero:
    def __init__(self, name: str, power=10, agile=10, durability=10, iq=10, intuition=10, charisma=10):
        self.name = name
        self.power = power
        self.agile = agile
        self.durability = durability
        self.iq = iq
        self.intuition = intuition
        self.charisma = charisma
        self.items: list[str] = []

    def get_hero(self):
        hero = {'name': self.name, 'power': self.power, 'agile': self.agile, 'durability': self.durability,
                'iq': self.iq,
                'intuition': self.intuition, 'charisma': self.charisma, 'items': get_hero_items('distance')}
        return hero


if __name__ == '__main__':
    a = Hero(get_name('elf'))
    print(a.get_hero())

