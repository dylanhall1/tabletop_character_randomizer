#!/usr/bin/env python
'''
This character generator is based purely off the free
information found from the D&D 5e basic players guide at
http://dnd.wizards.com/products/tabletop/players-basic-rules

This is to create a basic character giving you a race, class,
traits, spells, and items for your character.

I used Py2Exe to make a runnable .exe file

Author:  Dylan Hall
'''
from random import *

class Character(object):
    def __init__(self):
        #runs the class, race, and stat generators
        self.characterclass = self.char_class()
        self.characterrace = self.char_race()
        self.intro_summary()
        self.stats = self.char_stats()
        self.traits = self.char_traits()
        self.items = self.char_items()
        self.character_summary()


    def char_class(self):
        return choice(['Cleric', 'Fighter', 'Rogue', 'Wizard'])

    def char_race(self):
        return choice(['Hill Dwarf', 'Mountain Dwarf', 'High Elf', 'Wood Elf',
                       'Lightfoot Halfling', 'Stout Halfling','Human'])

    def intro_summary(self):
        print'''
        Your Randomized Race and Class is as Follows:
        Race:  {}
        Class: {}
        '''.format(self.characterrace,self.characterclass)

    def char_stats(self):
        # roll 4 D6s drop the lowest number and add the highest 3
        # this is done for each stat slot
        character_stats = {
            'Strength': 0,
            'Wisdom': 0,
            'Intelligence': 0,
            'Constitution': 0,
            'Dexterity': 0,
            'Charisma': 0
        }

        stats = []
        for x in range(6):
            rolls = [randint(1, 6) for i in range(4)]
            rolls.sort()
            stats.append(sum(rolls[1:]))

        for i in character_stats:
            while True:
                input = raw_input("What stat would you like to be for {}\nYour stats to choose from are {}\n".format(i, stats))
                if input.isdigit():
                    input = int(input)
                    if input in stats:
                        character_stats[i] = input
                        stats.remove(input)
                        break
        return character_stats


    def char_traits(self):
    # character traits for each race to be used in the output of the character and adds to their stats
        race = self.characterrace
        #Dwarf
        if race == 'Hill Dwarf' or race == 'Mountain Dwarf':
            self.stats['Constitution'] += 2
            if race == 'Hill Dwarf':
                self.stats['Wisdom'] +- 1
                modifystats = "Hill Dwarves are Sturdy and receive an additional +2 Constitition and +1 Wisdom ability scores."
            else:
                self.stats['Strength'] += 2
                modifystats = "Mountain Dwarves are Strong and receive an addition +2 Constitution and +2 Strength ability scores. "
            age = "Dwarves mature at the same rate as humans, but they're considered young until they reach the age of 50.\n\t On average, they live about 350 years."
            size = "Dwarves stand between 4 and 5 feet tall and average about 150 pounds. Your size is Medium."
            speed = "Your base walking speed is 25 feet. Your speed is not reduced by wearing heavy armor."
            language = "You can speak, read, and write Common and Dwarvish."
            if race == 'Hill Dwarf':
                special = "Dwarven Toughness: Your hit point maximum increased by 1, and increased by 1 everytime you gain a level"
            else:
                special = "Dwarven Armor Training: You have proficiency with light and medium armor."
            return modifystats, age, size, speed, language, special
        #Elf
        elif race == 'High Elf' or race == 'Wood Elf':
            self.stats['Dexterity'] += 2
            if race == 'High Elf':
                self.stats['Intelligence'] += 1
                modifystats = "High Elves are lithe and intelligent and receive an additional +2 Dexterity and +1 Intelligence ability scores."
            else:
                self.stats['Wisdom'] += 1
                modifystats = "Wood Elves are lithe and cunning and receive an additional +2 dexterity and +1 Wisdom ability scores."
            age = "An Elf typically claims adulthood and an adult name around the age of 100 and can live to be 750 years old."
            size = "Elves range from under 5 to over 6 feet tall and have slender builds. Your size is Medium."
            speed = "Your base walking speed is 30 feet."
            language = "You can speak, read, and write Common and Elvish."
            if race == 'High Elf':
                special = "Elf Weapon Training: You have proficiency with the longsword, shortsword, shortbow, and longbow.\nCantrip: You know one cantrip of your choice from the wizard spell list.\nExtra Language: You can speak, read, and write one extra language of your choice."
            else:
                special = "Elf Weapon Training: You have proficiency with the longsword, shortsword, shortbow, and longbow.\nFleet of Foot: Your base walking speed increases to 35 feet.\nMask of the Wild: You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, and other natural phenomena."
            return modifystats,age, size, speed, language, special
        #Halfling
        elif race == 'Lightfoot Halfling' or race == 'Stout Halfling':
            self.stats['Dexterity'] += 2
            if race == 'Lightfoot Halfling':
                self.stats['Charisma'] += 1
                modifystats = "Lightfoot Halflings are lithe and charismatic receiving an additional +2 Dexterity and +1 Charisma ability scores."
            else:
                self.stats['Constitution'] += 1
                modifystats = "Stout Halfings are lithe and hardy receiving an additional +2 Dexterity and +1 Constitution ability scores."
            age = "A halfling reaches adulthood at the age of 20 and generally lives into the middle of his or her second century"
            size = "Halflings average about 3 feet tall and weigh about 40 pounds. Your size is Small."
            speed = "Your base walking speed is 25 feet."
            language = "You can speak, read, and write Common and Halfling"
            if race == 'Lightfoot Halfling':
                special = "Naturally Stealthy: You can attempt to hide even when you are obscured by a creature that is at least one size larger than you."
            else:
                special = "Stout Resilience: You have advantage on saving throws against poison, and you have resistance against poison damage."
            return modifystats, age, size, speed, language, special
        #Human
        elif race == 'Human':
            self.stats['Dexterity'] += 1
            self.stats['Strength'] += 1
            self.stats['Constitution'] += 1
            self.stats['Wisdom'] += 1
            self.stats['Intelligence'] += 1
            self.stats['Charisma'] += 1
            modifystats = "Humans are very resilient and receive a +1 to all ability scores."
            age = "Humans reach adulthood in their late teens and live less than a century."
            size = "Humans vary widely in height and build, from barely 5 feet to well over 6 feet tall. Your size is Medium."
            speed = "Your base walking speed is 30 feet."
            language = "You can speak, read and write Common and One extra language of your choosing. "
            special = ""

            return modifystats,age, size, speed, language, special
        else:
            return "What?"

    def char_spells(self):
        num0 = 3
        num1 = 2
        cantrips = sample(['Acid Splash',
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
        'Thaumaturgy'],num0)

        level_1 = sample(['Bless',
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
        'Thunderwave'],num1)
        return cantrips, level_1

    def print_spells(self):
        #spells looks like this ([cantrip1,cantrip2],[spell1,spell2])
        #using 2 for loops for desired spelllist output
        spells = self.char_spells()
        print "\nCantrips:"
        for x in spells[0]:
            print "\t" + x
        print "Level 1:"
        for y in spells[1]:
            print "\t" + y

    def char_items(self):
        #gold
        if self.characterclass == 'Cleric' or self.characterclass == 'Fighter':
            num = 5
        else:
            num = 4
        gold = 0
        for x in range(num):
            goldroll = randint(1,4)
            gold += goldroll
        gold *= 10
        return gold


    def character_summary(self):
        print "\t\tSUMMARY OF CHARACTER"
        print "RACE & CLASS"
        print "Your race is that of a {}\nYour class is that of a {}".format(self.characterrace, self.characterclass)
        print "You Start with {} gold\n".format(self.items)
        print "TRAITS"
        for i in range (len(self.traits)):
            print self.traits[i]

        print "\nSTATS"
        for i in self.stats:
            print "{}:{} ".format(i,self.stats[i]),#this comma keeps it on one line, remove to make it vertical

        if self.characterclass =='Cleric ' or self.characterclass == 'Wizard':
            self.print_spells()

if __name__ == "__main__":
    print "Welcome to my Dungeons & Dragons character randomizer"
    first_character = Character()
    while raw_input("\nWould you like to create a character?(no to Quit)\n") !=  'no':
        next_character = Character()
