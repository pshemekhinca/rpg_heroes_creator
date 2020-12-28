import random
import json


def get_name(race):
    with open(f'txt_files/name_{race}.txt') as f:
        names = f.read().splitlines()
        name = random.choice(names)
        return name

def get_hero_items(distance):
    with open(f'txt_files/{distance}_weapon.txt') as f:
        weapons = f.read().splitlines()
        weapon = random.sample(weapons, 3)
        return list(weapon)


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
        hero = {'name': self.name, 'power': self.power, 'agile': self.agile, 'durability': self.durability, 'iq': self.iq,
                'intuition': self.intuition, 'charisma': self.charisma, 'items': get_hero_items('close')}
        return hero


if __name__ == '__main__':
    a = Hero(get_name('human'))
    print(a.get_hero())
