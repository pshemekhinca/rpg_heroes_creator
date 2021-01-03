from heroes import Hero, CreateTeam

intro_quest = input('Would You like to add hero/es?\n--> "Y" for yes or "q" to quit -> ')

while intro_quest != 'q':
    race = {1: 'human', 2: 'elf', 3: 'dwarf', 4: 'shifter'}
    pick_race = int(input("\nWhat race you choose for your hero: \n1. Human\n2. Elf\n3. Dwarf\n4. Shifter"
                          "\n\t\tpick the race number:"))
    heroes_qty = int(input(f"\nHow many of {race[pick_race]}s do you want to have? -> "))

    for i in range(heroes_qty):
        sample_hero = Hero(race[pick_race])
        print(sample_hero.get_hero())

    intro_quest = input('Would You like to add next hero/es?\n--> "Y" for yes or "q" to quit')
