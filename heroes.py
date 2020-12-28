class Hero:
    def __init__(self, name: str, power=10, agile=10, armor=10, iq=10, intuition=10, charisma=10):
        self.name = name
        self.power = power
        self.agile = agile
        self.armor = armor
        self.iq = iq
        self.intuition = intuition
        self.charisma = charisma
        self.items: list[str] = []

    def get_hero(self):
        hero = {'name': self.name, 'power': self.power, 'agile': self.agile, 'armor': self.armor, 'iq': self.iq,
                'intuition': self.intuition, 'charisma': self.charisma, 'items': self.items}
        return hero


if __name__ == '__main__':
    a = Hero('Mojmir')
    print(a.get_hero())
