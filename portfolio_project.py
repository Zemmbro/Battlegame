import random


class Characters():
    def __init__(self, randomness=False):
        self.lookup = {"mage": {"hp": 120, "abilities": {"Fireball": 15, "Scorch": 10, "Fire Blast": 30, "Pyroblast": 45}},
                       "warrior": {"hp": 120, "abilities": {"Bloodthirst": 20, "Raging Blow": 15, "Slam": 25, "Execute": 40}},
                       "shaman": {"hp": 120, "abilities": {"Earth Shock": 10, "Elemental Blast": 25, "Earthquake": 20, "Fire Elemental": 45}},
                       "warlock": {"hp": 120, "abilities": {"Shadow Bolt": 20, "Call Dreadstalkers": 25, "Hand of Gul'Dan": 25, "Demonbolt": 30}},
                       "druid": {"hp": 120, "abilities": {"Wrath": 10, "Starfire": 15, "Starfall": 20, "Starsurge": 50}},
                       "hunter": {"hp": 120, "abilities": {"Steady Shot": 15, "Arcane Shot": 20, "Rapid Fire": 25, "Aimed Shot": 40}}
                       }
        if randomness == True:
            self.name = self.computer_choice()
        else:
            self.name = self.print_character_menu()
        self.hp = self.lookup[self.name]["hp"]
        self.abilities = self.lookup[self.name]["abilities"]

    def print_character_menu(self):
        print(
            """
        --- Choose Your Character ---
    --------------------------------------
    |       Mage      |      Warrior     |
    --------------------------------------
    |      Shaman     |      Warlock     |
    --------------------------------------
    |      Druid      |      Hunter      |
    --------------------------------------
        """
        )

        character_choice = input("Please choose your character: ")
        if character_choice.lower() not in self.lookup.keys():
            print("Invalid choice. Try again!")
            return self.print_character_menu()
        else:
            return character_choice.lower()

    def computer_choice(self):
        ran_list = random.randint(0, 5)
        print(
            f"Your opponent has chosen: {list(self.lookup.keys())[ran_list]}")
        return list(self.lookup.keys())[ran_list]

    def take_damage(self, damage_received):
        self.hp -= damage_received
        if self.hp < 1:
            return True
        else:
            return False


class Game():

    def __init__(self):
        pass

    def welcome(self):
        print(
            """
    Welcome to the Battle Simulator! This is a turn-based battle simulator where there can only be one winner.\n

    \t\t\t\t--- How to play ---\n
    First you will choose your character, then the computer will choose one at random.
    Once the characters have been selected, you will take turns with your opponent choosing a move.\n

    Moves have a variety of damage, but watch out for those pesky miss chances!
    Think ahead as some abilities have a cooldown until they can be used again.\n

    Each player will start with 120 health, and the first player to reduce their opponent to 0 is the winner.
    You do not know how much damage each ability does.\n

    Good luck!
    """
        )
        # Miss chances, cooldowns, and crit chances to be added later

    def print_abilities(self):
        print(
            f"""
        --- Choose Your Ability ---
        - {list(self.player_character.abilities.keys())[0]}
        - {list(self.player_character.abilities.keys())[1]}
        - {list(self.player_character.abilities.keys())[2]}
        - {list(self.player_character.abilities.keys())[3]}
        """
        )
        ability_choice = input("Choice: ")
        return self.player_character.abilities[ability_choice]

    def random_abilities(self):
        rand_ability_int = random.randint(0, 3)
        # print(len(list(self.computer_character.abilities.keys())), "len(keys())")
        print(
            f"Your opponent strikes you with: {list(self.computer_character.abilities.keys())[rand_ability_int]}")
        chosen_ability_name = list(self.computer_character.abilities.keys())[
            rand_ability_int]
        return self.computer_character.abilities[chosen_ability_name]
        # Flavor text to be added later. A list to pull random dialogue from

    def play(self):
        self.welcome()
        self.player_character = Characters()
        self.computer_character = Characters(True)
        while True:
            win = self.computer_character.take_damage(self.print_abilities())
            print(
                f"Your enemy's hp has been reduced to: {self.computer_character.hp}\n")
            if win:
                print("You won!")
                break
            win = self.player_character.take_damage(self.random_abilities())
            print(
                f"Your health has been reduced to: {self.player_character.hp}")
            if win:
                print("You won!")
                break


Game().play()

# while (self.hp != 0 or self.hp != 0):

#     miss = False

#     if player_turn:
#         print("Please select a move: ")
#         #Show moves from selected character
#         move_miss = random.randint(1,10)
