"""
A small generator to randomly generate silly names from two tuples.

The goal of this script is to conform to PEP 8 and PEP 257 and achieve
a rating of 10/10 when running pylint on this file.
"""

import sys
import random


def main():
    """Choose names at random from two tuples and print to screen."""
    print("Welcome to the 'Psych Sidekick Name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n\n")

    first_names = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'BeenieWeenie'",
                   "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
                   'Butterbean', 'Buttermilk', 'Buttocks', 'Chad',
                   'Chesterfield', 'Chewy', 'Chigger', 'Cinnabuns', 'Cleet',
                   'Cornbread', 'Crab Meat', 'Crapps', 'Dark Skies',
                   'Dennis Clawhammer', 'Dicman', 'Elphonso', 'Fancypants',
                   'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
                   'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'",
                   'Johnny', 'Lemongrass', 'Lil Debil', 'Longbranch',
                   '"Lunch Money"', 'Mergatroid', '"Mr Peabody"', 'OilCan',
                   'Oinks', 'Old Scratch', 'Ovaltine', 'Pennywhistle',
                   'Pitchfork Ben', 'Potato Bug', 'Pushmeet', 'Rock Candy',
                   'Schlomo', 'Scratchensniff', 'Scut', "Sid 'The Squirts'",
                   'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki',
                   'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
                   'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
                   "Winston 'Jazz Hands'", 'Worms')

    last_names = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
                  'Breedslovetrout', 'Butterbaugh', 'Clovenhoof',
                  'Clutterbuck', 'Cocktoasten', 'Endicott', 'Fewhairs',
                  'Gooberdapple', 'Goodensmith', 'Goodpasture', 'Guster',
                  'Henderson', 'Hooperbag', 'Hoosenater', 'Hootkins',
                  'Jefferson', 'Jenkins', 'JingleySchmidt', 'Johnson',
                  'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine',
                  'Nettles', 'Noseworthy', 'Olivetti', 'Outerbridge',
                  'Overpeck', 'Overturf', 'Oxhandler', 'Pealike',
                  'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton',
                  'Porkins', 'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal',
                  'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern', 'Stevens',
                  'Stroganoff', 'SugarGold', 'Swackhamer', 'Tippins',
                  'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger',
                  'Weewax', 'Weiners', 'Whipkey', 'Wigglesworth',
                  'Wimplesnatch', 'Winterkorn', 'Woolysocks')

    while True:
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)

        print('\n\n')
        print(f'{first_name} {last_name}', file=sys.stderr)
        print('\n\n')

        try_again = input("Try again? (Press Enter else 'n' to quit)\n")
        if try_again.lower() == 'n':
            break


if __name__ == '__main__':
    main()
