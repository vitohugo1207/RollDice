import PySimpleGUI as sg
from dice import *


class ui:
    def __init__(self):
        sg.theme('Dark')

        layoutDice = [
            [sg.Button('d20'), sg.Button('2d8')],
            [sg.Input(key='dice')],
            [sg.Text('Test'), sg.Button('Ok')],
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
                  ]], )]
        ]
        window = sg.Window('rolldice', layoutMain)
        self.event, self.values = window.Read()

    def start(self):
        while True:
            if (self.event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or self.event == 'Exit') and sg.popup_yes_no(
                    'Do you really want to exit?') == 'Yes':
                break
            dice = self.values['dice']
            diceMain(dice)

ui().start()
