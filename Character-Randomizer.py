#!/usr/bin/env python
'''
This character generator is based purely off the free
information found from the D&D 5e basic players guide at
http://dnd.wizards.com/products/tabletop/players-basic-rules

This is to create a basic character giving you a race, class,
traits, spells, and items for your character.

Author:  Dylan Hall
'''
from random import *

class Character(object):

    def __init__(self):
        #runs the class, race, and stat generators
        self.characterclass = self.char_class()
        self.characterrace = self.char_race()
        self.stats = self.char_stats()
        self.traits = self.char_traits()
        self.spells = self.char_spells()
        self.character_info()

    def char_class(self):
        return choice(['Cleric','Fighter','Rogue','Wizard'])

    def char_race(self):
        return choice(['Hill Dwarf','Mountain Dwarf','High Elf','Wood Elf','Lightfoot Halfling','Stout Halfling','Human'])

    def char_stats(self):
        # roll 4 D6s drop the lowest number and add the highest 3
        # this is done for each stat slot
        stats = []
        for x in range(6):
            rolls =[randint(1,6) for i in range(4)]
            rolls.sort()
            stats.append(sum(rolls[1:]))
        return stats

    """this is a long list of traits for each race which will be said in the output of the character"""
    def char_traits(self):
        race = self.characterrace
        #Dwarf
        if race == 'Hill Dwarf' or race == 'Mountain Dwarf':
            if race == 'Hill Dwarf':
                absc = "Your Constitution score increases by 2 and your Wisdom score increased by 1."
            else:
                absc = "Your Constitution score increases by 2 and your Strength score increased by 2."
            age = "Dwarves mature at the same rate as humans, but they're considered young until they reach the age of 50.\n\t On average, they live about 350 years."
            size = "Dwarves stand between 4 and 5 feet tall and average about 150 pounds. Your size is Medium."
            speed = "Your base walking speed is 25 feet. Your speed is not reduced by wearing heavy armor."
            language = "You can speak, read, and write Common and Dwarvish."
            if race == 'Hill Dwarf':
                special = "Dwarven Toughness: Your hit point maximum increased by 1, and increased by 1 everytime you gain a level"
            else:
                special = "Dwarven Armor Training: You have proficiency with light and medium armor."
            return absc, age, size, speed, language, special
        #Elf
        elif race == 'High Elf' or race == 'Wood Elf':
            if race == 'High Elf':
                absc = "Your Dexterity score increases by 2 and your Intelligence score increases by 1."
            else:
                absc = "Your Dexterity score increased by 2 and your Wisdom score increases by 1."
            age = "An Elf typically claims adulthood and an adult name around the age of 100 and can live to be 750 years old."
            size = "Elves range from under 5 to over 6 feet tall and have slender builds. Your size is Medium."
            speed = "Your base walking speed is 30 feet."
            language = "You can speak, read, and write Common and Elvish."
            if race == 'High Elf':
                special = "Elf Weapon Training: You have proficiency with the longsword, shortsword, shortbow, and longbow.\nCantrip: You know one cantrip of your choice from the wizard spell list.\nExtra Language: You can speak, read, and write one extra language of your choice."
            else:
                special = "Elf Weapon Training: You have proficiency with the longsword, shortsword, shortbow, and longbow.\nFleet of Foot: Your base walking speed increases to 35 feet.\nMask of the Wild: You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, and other natural phenomena."
            return absc, age, size, speed, language, special
        #Halfling
        elif race == 'Lightfoot Halfling' or race == 'Stout Halfling':
            if race == 'Lightfoot Halfling':
                absc = "Your Dexterity score increases by 2 and your Charisma score increases by 1."
            else:
                absc = "Your Dexterity score increases by 2 and your Constitution score increases by 1."
            age = "A halfling reaches adulthood at the age of 20 and generally lives into the middle of his or her second century"
            size = "Halflings average about 3 feet tall and weigh about 40 pounds. Your size is Small."
            speed = "Your base walking speed is 25 feet."
            language = "You can speak, read, and write Common and Halfling"
            if race == 'Lightfoot Halfling':
                special = "Naturally Stealthy: You can attempt to hide even when you are obscured by a creature that is at least one size larger than you."
            else:
                special = "Stout Resilience: You have advantage on saving throws against poison, and you have resistance against poison damage."
            return absc, age, size, speed, language, special
        #Human
        elif race == 'Human':
            absc = "Your ability scores each increase by 1."
            age = "Humans reach adulthood in their late teens and live less than a century."
            size = "Humans vary widely in height and build, from barely 5 feet to well over 6 feet tall. Your size is Medium."
            speed = "Your base walking speed is 30 feet."
            language = "You can speak, read and write Common and One extra language of your choosing. "
            special = ""

            return absc, age, size, speed, language, special
        else:
            return "What?"

    def char_spells(self):
        if self.characterclass == 'Cleric' or self.characterclass == 'Wizard':
            num0 = 3
            num1 = 2
        else:
            break
        cantrip_spells = []
        level_1_spells = []
        cantrips = ['Acid Splash',
        'Dancing Lights',
        'Fire Bolt',
        'Guidance',
        'Light',
        'Mage Hand',
        'Minor Illusion',
        'Poison Spray',
        'Prestidigitation',
        'Ray Of Frost',
        'Resistance',
        'Sacred Flame',
        'Shocking Grasp',
        'Spare the Dying',
        'Thaumaturgy']

        level_1 = ['Bless',
        'Burning Hands',
        'Charm Person',
        'command',
        'Comprehend Languages',
        'Cure Wounds',
        'Detect Magic',
        'Disguise self',
        'Faerie fire',
        'Guiding Bolt',
        'Healing Word',
        'Identify',
        'Inflict Wounds',
        'Mage Armor',
        'Magic Missile',
        'Sanctuary',
        'Shield',
        'Shield of Faith',
        'Silent Image',
        'Sleep',
        'Thunderwave']
        for x in range(num0):
            lvl0 = cantrips[randint(0,len(cantrips)-1)]
            cantrip_spells.append(lvl0)
            cantrips.remove(lvl0)

        for y in range(num1):
            lvl1 = level_1[randint(0,len(level_1)-1)]
            level_1_spells.append(lvl1)
            level_1.remove(lvl1)

        return cantrip_spells, level_1_spells

    def char_items(self, charclass):
        #may do this at some point
        exit(1)

    def character_info(self):
        #all my newlines and tabs are because I like the command line more neat, in reality it doesnt matter.
        stat_name = ['Strength','Wisdom','Intelligence','Constitution','Dexterity','Charisma']
        FINAL_STATS = []
        print "\n\tYour race is {} and your class is {}\n".format(self.characterrace,self.characterclass )
        print "Please choose one of the following for your stat: {}".format(self.stats)
        for stat_num in range(len(self.stats)):
            while True:
                user = raw_input("Please input one of these stats for your " + stat_name[stat_num] + ": ")
                if user.isdigit():
                    stat_choice = int(user)
                    if stat_choice in self.stats:
                        FINAL_STATS.append(str(stat_name[stat_num]) + ": " + str(stat_choice) )
                        self.stats.remove(stat_choice)
                        break

        print "\n\tSUMMARY"
        print "\n\tYour class is {} and your race is {}\n".format(self.characterrace,self.characterclass)
        print '''
    \tCharacter Information:\n
    Ability Score: {}
    Language: {}
    Size: {}
    Speed: {}
    Age: {}
    {}
     '''.format(self.traits[0], self.traits[1], self.traits[2], self.traits[3], self.traits[4], self.traits[5])

        print "\t\t\tYour final stats are as follows:\n\t{} {} {} {} {} {}".format(FINAL_STATS[0],FINAL_STATS[1],FINAL_STATS[2],FINAL_STATS[3],FINAL_STATS[4],FINAL_STATS[5])

#character testing
if __name__ == "__main__":
    print "Welcome to my Dungeons & Dragons character randomizer"
    first_character = Character()
    while raw_input("\nWould you like to create a character?(no to Quit)\n") !=  'no':
        random_character = Character()
