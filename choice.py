from random import choice

class choiceClass():
    def __init__(self, choiceOne):
        self.choiceOne = choiceOne

    def strForList(self):
        self.choiceOne = list(self.choiceOne.split(","))

    def dataShow():
        print(f'')

    def choiceDef(self):
        self.strForList()
        chosen = choice(self.choiceOne)