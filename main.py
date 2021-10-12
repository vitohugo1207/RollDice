from shuffle import shuffleMain
from choice import choiceMain
from dice import *

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

if __name__ == "__main__":
    while True:
        lin()
        dice = str(input('-> ').replace(' ', '').lower())  # Data extraction, remove space and set letter in lower
        if dice == 'exit':
            break
        else:
            diceImport = diceMain(dice)
            diceImport.diceRoll()