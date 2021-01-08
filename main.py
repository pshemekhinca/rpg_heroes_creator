from heroes import Hero, CreateTeam
from colors import FColor, BColor
import random


def check_if_int(message):
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print(f'{FColor.RED}It must be a number!{FColor.END}')


intro_quest = input('\nWould you like to recruit some hero/es to your team?'
                    f'\n{FColor.BOLD}--> [Y]eah, sure or [N]ope -> {FColor.END}')
player_team = {}
comp_team = {}
RACE_LIST = {1: 'human', 2: 'elf', 3: 'dwarf', 4: 'shifter'}
team_name = input(f'{FColor.YELLOW}Name the flag for your warriors: {FColor.END}')

while intro_quest.lower() != 'n':
    if intro_quest.lower() != 'n' and intro_quest.lower() != 'y':
        print(f'\n{FColor.YELLOW}As our LEADER, you should be FOCUSED ...a little bit more.{FColor.END}')
        intro_quest = input('So? Would you like to recruit some hero/es to your team?\n--> [Y]eah, sure or [N]ope -> ')

    if intro_quest.lower() == 'y':
        growing_team = {}
        while intro_quest.lower() != 'e':

            temp_team = {}
            pick_race = check_if_int(
                "\nWhat race you choose for your team: \n[1] Human\n[2] Elf\n[3] Dwarf\n[4] Shifter"
                f"\n\t\t{FColor.BOLD}pick the race number (1-4):{FColor.END}")

            while int(pick_race) not in list(RACE_LIST):
                print(f'\n{FColor.YELLOW}Stay FOCUSED!{FColor.END} Type a NUMBER from 1 to 4 only!')
                pick_race = check_if_int(f'{FColor.YELLOW}Pick correct number 1-4: {FColor.END}')

            heroes_qty = check_if_int(f"\nHow many {RACE_LIST[int(pick_race)]} warriors do you want to recruit? -> ")
            sample_team = CreateTeam(RACE_LIST[int(pick_race)], heroes_qty)
            temp_team[RACE_LIST[int(pick_race)]] = sample_team
            growing_team[team_name] = temp_team
            print(f'Now your crew consist of:\n {growing_team}')
            # temp_team = {RACE_LIST[int(pick_race)]: sample_team}
            intro_quest = input("\nWould you like to add next hero/es to your team?\n"
                                "--> [Y]eah, sure or [E]nough! let's find enemies: ")

        print(f"\n\nWarriors recruitment complete!!!\n\nHere is your impressive army:\n"
              f"\nV'V'V'V'V'V'V'V'V'V'V'V'V'V\n{growing_team}")
        intro_quest = input(
            f"\n{FColor.BOLD}Do you want to [F]ight or you ru[N] away scared of the enemy{FColor.END}\n")

print(
    f'\n{FColor.BOLD}It was nice to have you here for the while.{FColor.END}\n{FColor.MAGENTA}'
    f'See you later... Bye, bye...{FColor.END}')
