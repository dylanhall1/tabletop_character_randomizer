'''
This character generator is based purely off the free
information found from the D&D 5e basic players guide at
http://dnd.wizards.com/products/tabletop/players-basic-rules

This is to create a basic character giving you a race, class,
traits, spells, and items for your character.

Author:  Dylan Hall
'''

from random import randint

class Character(object):

    def __init__(self):
        #runs the class, race, and stat generators
        self.characterclass = self.char_class()
        self.characterrace = self.char_race()
        self.stats = self.char_stats()
        self.traits = self.char_traits(self.characterrace)
    def char_class(self):
        classlist = [
                'Cleric',
                'Fighter',
                'Rogue',
                'Wizard']
        return classlist[randint(0, len(classlist)-1)]

    def char_race(self):
        #Could I expand this for subraces?
        #ex have Dwarf, Hill Dwarf, and Mountain dwarf?
        #name randomizer?
        racelist = [
                'Dwarf',
                'Elf',
                'Halfling',
                'Human'
                ]
        return racelist[randint(0,len(racelist)-1)]

    def char_stats(self):
        # roll 4 D6s drop the lowest number and add the highest 3
        # this is done for each stat slot
        s1,s2,s3,s4,s5,s6 = ([],[],[],[],[],[])
        for x in range(4):
            s1.append(randint(1,6))
            s2.append(randint(1,6))
            s3.append(randint(1,6))
            s4.append(randint(1,6))
            s5.append(randint(1,6))
            s6.append(randint(1,6))
        stat1 = sorted(s1)
        stat2 = sorted(s2)
        stat3 = sorted(s3)
        stat4 = sorted(s4)
        stat5 = sorted(s5)
        stat6 = sorted(s6)
        return sum(stat1[1:]),sum(stat2[1:]),sum(stat3[1:]),sum(stat4[1:]),sum(stat5[1:]),sum(stat6[1:])

    #this is a long list of traits for each race which will be said in the output of the chracter
    #Subraces might be considered
    def char_traits(self,race):
        self.race = race
        absc = ""
        age = ""
        size = ""
        speed = ""
        language = ""
        if race == 'Dwarf':
            absc = "Your Constitution score increases by 2."
            age = "Dwarves mature at the same rate as humans, but they're considered young until they reach the age of 50. On average, they live about 350 years."
            size = "Dwarves stand between 4 and 5 feet tall and average about 150 pounds. Your size is Medium."
            speed = "Your base walking speed is 25 feet. Your speed is not reduced by wearing heavy armor."
            language = "You can speak, read, and write Common and Dwarvish."
            special = ""
            return absc, age, size, speed, language
        elif race == 'Elf':
            absc = "Your Dexterity score increases by 2."
            age = "An Elf typically claims adulthood and an adult name around the age of 100 and can live to be 750 years old."
            size = "Elves range from under 5 to over 6 feet tall and have slender builds. Your size is Medium."
            speed = "Your base walking speed is 30 feet."
            language = "You can speak, read, and write Common and Elvish."
            special = ""
            return absc, age, size, speed, language
        elif race == 'Halfling':
            absc = "Your Dexterity score increases by 2."
            age = "A halfling reaches adulthood at the age of 20 and generally lives into the middle of his or her second century"
            size = "Halflings average about 3 feet tall and weigh about 40 pounds. Your size is Small."
            speed = "Your base walking speed is 25 feet."
            language = "You can speak, read, and write Common and Halfling"
            special = ""
            return absc, age, size, speed, language
        elif race == 'Human':
            absc = "Your ability scores each increase by 1."
            age = "Humans reach adulthood in their late teens and live less than a century."
            size = "Humans vary widely in height and build, from barely 5 feet to well over 6 feet tall. Your size is Medium."
            speed = "Your base walking speed is 30 feet."
            language = "You can speak, read and write Common and One extra language of your choosing. "
            special = ""
            return absc, age, size, speed, language
        else:
            return "What?"

    def char_spells(self, charclass):
        #may do this at some point
        exit(1)

    def char_items(self, charclass):
        #may do this at some point
        exit(1)

def character_info(character):
    print "\nYour class is {} and your race is {}\n".format(character.characterrace, character.characterclass)
    print '''roll 4 D6s drop the lowest number and add the highest 3 for your value.
This has been done 6 times, one for each stat. They are as follows:
{} {} {} {} {} {}
    '''.format(character.stats[0],character.stats[1],character.stats[2],character.stats[3],character.stats[4],character.stats[5])
    print "You can allocate these numbers into the following stats:\nWisdom, Constitution, Dexterity, Strength, Charisma, and Intelligence."
    print '''\nCharacter Information:
Ability Score: {}
Age: {}
Size: {}
Speed: {}
Language: {}
    '''.format(character.traits[0],character.traits[1],character.traits[2],character.traits[3], character.traits[4])

#character testing
char1 = Character()
character_info(char1)
