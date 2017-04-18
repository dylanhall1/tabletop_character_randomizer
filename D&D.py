
'''
This character generator is based purely off the information
found from the D&D 53 basic players guide at
http://dnd.wizards.com/products/tabletop/players-basic-rules
'''

from random import randint

class Character(object):

    def __init__(self):
        #runs the class, race, and stat generators
        self.characterclass = self.char_class()
        self.characterrace = self.char_race()
        self.stats = self.char_stats()

    def char_class(self):
        self.classlist = [
                'Cleric',
                'Fighter',
                'Rogue',
                'Wizard']
        return self.classlist[randint(0, len(self.classlist)-1)]

    def char_race(self):
        self.racelist = [
                'Dwarf',
                'Elf',
                'Halfling',
                'Human'
                ]
        return self.racelist[randint(0,len(self.racelist)-1)]

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


def character_info(character):
    print "\nYour class is {} and your race is {}\n".format(character.characterclass, character.characterrace)
    print '''roll 4 D6s drop the lowest number and add the highest 3 for your value.
This has been done 6 times, one for each stat. They are as follows:
{} {} {} {} {} {}
    '''.format(character.stats[0],character.stats[1],character.stats[2],character.stats[3],character.stats[4],character.stats[5])
#two characters for testing to make sure the random generation is working
char1 = Character()
char2 = Character()

character_info(char1)
character_info(char2)
