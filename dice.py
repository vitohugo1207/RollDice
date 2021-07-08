from random import randrange, choice, shuffle
from datetime import datetime
from time import sleep
from shuffle import shuffleMain
from choice import choiceMain

# Made by IkkiArtz


def lin():
    print('-+' * 20)

def help():
    print("""For use the dice: time_of_scroll_dice D range_0_to_10 +/- bonus, for exemple: 2d20+4
    \nThe dice's bonus not working without 'd' in dice, but scroll dice working without 'd'
    \nexit for close;
    \nHelp for see commands and how working;
    \nShuffle for shuffle the order of some words and/or number (still not working);
    \nChoice for choice one word or number (still not working);""")
    dice = ''

def diceMain(dice): # The variable of input is "dice"
    '''
    For use the dice: time_of_scroll_dice D range_0_to_10 +/- bonus, for exemple: 2d20+4
    The dice's bonus not working without 'd' in dice, but scroll dice working without 'd'
    '''

    diceMin = 1 # The minimum for start scroll dice
    
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
        except:
            print('I am sorry, did not understood. Type "help" for instructions.')
            sleep(5)
            dice = ''
            return

    if '-' in dice:
        try:
            diceLess = dice.find('-') # Find position of the scroll bonus
            rollBonus = dice[diceLess:].replace('-', '') # Remove the dice and "-"
            diceT = dice[:diceLess - 1].replace('-', '') # Remove the dice and "-"
            rollBonus = int(rollBonus) # Str for Int
            if len(diceT) > 2: # If characters of diceT (maximum limit of scroll dice) > 2.
                diceT = diceT[:len(diceT) - 1] # Remove the excess number.
        except:
            print('I am sorry, did not understood. Type "help" for instructions.')
            sleep(5)
            dice = ''
            return

    if diceT == '0': # If not have 'd' in dice
        diceA = 1
        diceT = dice

    # __Str for Int__
    try:
        diceT = int(diceT) + 1 # Counting with the 0
        diceA = int(diceA)
    except:
        print('I am sorry, did not understood. Type "help" for instructions.')
        sleep(5)
        dice = ''
        return

    rollList = [] # Created a list

    # __Loop of scroll dice time__
    try:
        for x in range(diceA):
            rollList.append(randrange(diceMin, diceT))  # diceMin (Minimum) between diceT (Total)
    except:
        print('I am sorry, did not understood. Type "help" for instructions.')
        sleep(5)
        dice = ''
        return

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
    time = timenow.strftime('%d/%m/%Y at %H:%M:%S') # Formatting time of scrolling dice
    print(time) # Show time of scrolling dice

    if len(rollList) > 1: # If characters of rollList (maximum limit of scroll dice) > one scroll dice
        print(f'List of dice roll: {", ".join(map(str, rollList))}') # Show list of scroll dice and bonus
    print(f'Total of dice roll: {rollTotal}') # Show total of scroll dice and bonus

def choiceMain():
    choice(choiceOne)

def shuffleMain():
    shuffle(deck)


if __name__ == '__main__':
    lin()  # Line
    while True:
        dice = str(input('-> ').replace(' ', '').lower())  # Data extraction, remove space and letter in lower
        if dice == 'exit':
            break
        elif dice == 'help':
            help()
        else:
            diceMain(dice)
            lin()
