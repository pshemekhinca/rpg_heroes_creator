from heroes import Hero, CreateTeam

intro_quest = input('Would You like to add hero/es?\n--> "Y" for yes or "q" to quit -> ')

while intro_quest != 'q':
    race = {1: 'human', 2: 'elf', 3: 'dwarf', 4: 'shifter'}
    pick_race = int(input("\nWhat race you choose for your hero: \n1. Human\n2. Elf\n3. Dwarf\n4. Shifter"
                          "\n\t\tpick the race number (1-4):"))

    while pick_race not in range(1, 5):
        pick_race = int(input('Pick correct number 1-4: '))

    heroes_qty = int(input(f"\nHow many of {race[pick_race]}s do you want to have? -> "))
    race_team_name = (input(f"\nWhat will be the the name of the {race[pick_race]}s horde? -> "))

    sample_team = CreateTeam(race_team_name, race[pick_race], heroes_qty)
    print(sample_team)

    intro_quest = input('Would You like to add next hero/es?\n--> "Y" for yes or "q" to quit')
