from shuffle import shuffleMain
from choice import *
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
        roll = str(input('-> ').replace(' ', '').lower())  # Data extraction, remove space and set letter in lower
        if roll == 'exit':
            break
        else:
            if ',' in roll:
                choiceImport = choiceClass(choiceOne = roll)
                choiceImport.choiceDef()
            else:
                diceImport = diceMain(dice = roll)
                diceImport.main()
