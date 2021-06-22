import PySimpleGUI as sg
from dice import *

# _________UI__________
sg.theme('Dark')

layoutDice = [
    [sg.Button('d20'), sg.Button('2d8')],
    [sg.In(key='dice')],
]
layoutShuffle = [
    [sg.Text('Shuffle')],
]
layoutChoice = [
    [sg.Text('Choice')],
]
layoutHistory = [
    [sg.Text('History')]
]

layoutMain = [
    [sg.TabGroup(
        [[sg.Tab('Dice', layoutDice),
          sg.Tab('Shuffle', layoutShuffle),
          sg.Tab('Choice', layoutChoice),
          sg.Tab('History', layoutHistory),
        ]],)]
]
window = sg.Window('RollDice', layoutMain)


# ________Main________
while True:
    event, values = window.read()
    print(layoutMain)
    if 'd' in event:
        dice = event
        diceMain(dice)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
