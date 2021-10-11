from random import randrange, choice, shuffle
from datetime import datetime
from time import sleep

class diceMain:
    def __init__(self, dice):
        self.dice = dice
        self.diceT = 0
        self.diceA = 0
        self.diceMin = 1 # The minimum for start scroll dice
        self.rollList = []
        self.rollBonus = 0

    def getScrollTimes(dice):
        '''Dice scroll times'''
        
        diceFindD = self.dice.find('d')
        self.diceA = self.dice[:diceFindD].replace('d', '') # Extraction time of dice roll and remove "d"
        if self.diceA == '':
            self.diceA = 1
        self.diceT = self.dice[diceFindD:].replace('d', '') # Extraction interval of draw

    def bonus(self):
        '''Bonus extraction'''

        if '+' in self.dice:
            diceFindBonus = self.dice.find('+')
            rollBonus = self.dice[diceFindBonus:].replace('+', '')
            self.diceT = self.diceT[:diceFindBonus - 1].replace('+', '')
            try:
                rollBonus = int(rollBonus)
            except ValueError:
                dice = self.dice[:diceFindBonus]

        elif '-' in self.dice:
            diceFindBonus = self.dice.find('-')
            rollBonus = self.dice[diceFindBonus:].replace('-', '')
            self.diceT = self.diceT[:diceFindBonus - 1].replace('-', '')
            try:
                rollBonus = int(rollBonus)
            except ValueError:
                dice = self.dice[:diceFindBonus]

        elif '*' in self.dice:
            diceFindBonus = self.dice.find('*')
            rollBonus = self.dice[diceFindBonus:].replace('*', '')
            self.diceT = self.diceT[:diceFindBonus - 1].replace('*', '')
            try:
                rollBonus = int(rollBonus)
            except ValueError:
                dice = self.dice[:diceFindBonus]

        elif '/' in self.dice:
            diceFindBonus = self.dice.find('/')
            rollBonus = self.dice[diceFindBonus:].replace('/', '')
            self.diceT = self.diceT[:diceFindBonus - 1].replace('/', '')
            try:
                rollBonus = int(rollBonus)
            except ValueError:
                dice = self.dice[:diceFindBonus]
        
        if self.diceT == '0': # If not have 'd' in dice
            self.diceA = 1
            self.diceT = dice

    def sumDice(self):
        '''Sum List of dice roll and roll bonus'''

        if '+' in self.dice:
            rollTotal = sum(self.rollList) + rollBonus
            self.rollList.append(f'+{rollBonus}')
            rollBonus = ''

        elif '-' in self.dice:
            rollTotal = sum(self.rollList) - rollBonus
            self.rollList.append(f'-{rollBonus}')
            rollBonus = ''

        elif '*' in self.dice:
            rollTotal = sum(self.rollList) * rollBonus
            self.rollList.append(f'*{rollBonus}')
            rollBonus = ''

        elif '/' in self.dice:
            rollTotal = sum(self.rollList) / rollBonus
            self.rollList.append(f'/{rollBonus}')
            rollBonus = ''

        else:
            rollTotal = sum(self.rollList)

    def dataShow(self):
        '''Data show'''
        timenow = datetime.now() # Acquiring time of scrolling dice
        time = timenow.strftime('%d/%m/%Y at %H:%M:%S') # Formatting time of scrolling dice
        print(time) # Show time of scrolling dice

        if len(self.rollList) > 1: # If characters of self.rollList (maximum limit of scroll dice) > one scroll dice
            print(f'List of dice roll: {", ".join(map(str, self.rollList))}') # Show list of scroll dice and bonus
        print(f'Total of dice roll: {self.rollTotal}') # Show total of scroll dice and bonus

    def dice(self):
        self.getScrollTimes()
        self.bonus()

        try:
            # __Str for Int__
            self.diceT = int(self.diceT) + 1 # Counting with the 0
            self.diceA = int(self.diceA)
        except:
            print('I am sorry, did not understood. Type "help" for instructions.')
            sleep(5)
            dice = ''
            return

        # __Loop of scroll dice time__
        try:
            for x in range(self.diceA):
                self.rollList.append(randrange(self.diceMin, self.diceT))  # self.diceMin (Minimum) between self.diceT (Total)
        except:
            print('I am sorry, did not understood. Type "help" for instructions.')
            sleep(5)
            dice = ''
            return

        self.sumDice()
        self.dataShow()
