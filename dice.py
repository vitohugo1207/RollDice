from random import randrange, choice, shuffle
from datetime import datetime
from time import sleep

# Made by IkkiArtz


def diceMain():
    roll = randrange(diceMin, diceT) # diceMin (Minimum) between diceT (Total)
    return roll # Return variable scroll for list

def lin():
    print('-+' * 20)

def error():
    print('I am sorry, did not understood. Type "help" for instructions.')
    sleep(5)
    exit()

def choiceMain():
    choice(choiceOne)


def shuffleMain():
    shuffle(deck)



if __name__ == '__main__':
    while True:
        # __Data extraction__
        lin() # Line
        dice = str(input('-> ').replace(' ', '').lower()) # Data extraction, remove space and letter in lower

        if dice == 'exit': # Break the Loop
            break

        if dice == 'help': # Help
            print("""For use the dice: time_of_scroll_dice D range_0_to_10 +/- bonus, for exemple: 2d20+4
            \nexit for close;
            \nHelp for see commands and how working;
            \nShuffle for shuffle the order of some words and/or number (still not working);
            \nChoice for choice one word or number (still not working);""")
            dice = ''

        if 'shuffle' in dice:
            dice = '' # Clean variable dice, for not conflict
            pass

        if 'choice' in dice:
            dice = '' # Clean variable dice, for not conflict
            pass

        if not dice == '': # If dice is empty pass.
            # __Dice scroll times__
            diceFindD = dice.find('d') # Find "d" position
            diceA = dice[:diceFindD].replace('d', '') # Extraction time of dice roll and remove "d"
            if diceA == '': # If not was defined time of dice roll at variable
                diceA = 1 # Roll the dice one time

            diceT = dice[diceFindD:].replace('d', '') # Extraction interval of draw

            # __Bonus extraction__
            if '+' in dice:
                try:
                    diceMore = dice.find('+') # Find position of the scroll bonus
                    rollBonus = dice[diceMore:].replace('+', '') # Remove the dice and "+"
                    diceT = diceT[:diceMore - 1].replace('+', '') # Remove the dice and "+"
                    rollBonus = int(rollBonus) # Str for Int
                    if len(diceT) > 2: # If characters of diceT (maximum limit of scroll dice) > 2
                        diceT = diceT[:len(diceT) - 1] # Remove the excess number
                    print(diceT, diceA, rollBonus)
                except:
                    error()

            if '-' in dice:
                try:
                    diceLess = dice.find('-') # Find position of the scroll bonus
                    rollBonus = dice[diceLess:].replace('-', '') # Remove the dice and "-"
                    diceT = dice[:diceLess - 1].replace('-', '') # Remove the dice and "-"
                    rollBonus = int(rollBonus) # Str for Int
                    if len(diceT) > 2: # If characters of diceT (maximum limit of scroll dice) > 2.
                        diceT = diceT[:len(diceT) - 1] # Remove the excess number.
                    print(diceT, diceA, rollBonus)
                except:
                    error()

            # __Str for Int__
            try:
                diceT = int(diceT) + 1 # Counting with the 0
                diceA = int(diceA)
            except:
                error()

            # __Created a variable diceMin__
            diceMin = 0 # The minimum for start scroll dice

            rollList = [] # Created a list

            # __Loop of scroll dice time__
            try:
                for X in range(diceA):
                    rollList.append(diceMain()) # Call def and save data at list
            except:
                error()

            # __Sum List of dice roll and roll bonus__
            if '+' in dice:
                rollTotal = sum(rollList) + rollBonus # Sum list and roll
                rollList.append(f'+{rollBonus}') # Add rollBonus at list
                rollBonus = '' # Clean variable rollBonus

            elif '-' in dice:
                rollTotal = sum(rollList) - rollBonus # subtract list and roll
                rollList.append(f'-{rollBonus}') # Add rollBonus at list
                rollBonus = '' # Clean variable rollBonus
            else:
                rollTotal = sum(rollList) # Sum if not has rollBonus

            # __Data show__
            timenow = datetime.now() # Acquiring time of scrolling dice
            time = timenow.strftime('%d/%m/%y at %H:%M:%S') # Formatting time of scrolling dice
            print(time) # Show time of scrolling dice
            if len(rollList) > 1: # If characters of rollList (maximum limit of scroll dice) > one scroll dice
                print(f'List of dice roll: {rollList}') # Show list of scroll dice and bonus
            print(f'Total of dice roll: {rollTotal}') # Show total of scroll dice and bonus
