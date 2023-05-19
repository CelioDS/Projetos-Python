import PySimpleGUI as sg
from PySimpleGUI import *


class calculadora():
    def __init__(self):
       pass


    def iniciar(self):
        # GUI Layout
        layout = [[Text('' * 10, background_color='grey')],
                  [Output(size=(18, 1), font=('Helvetica', 18),text_color='black', key='input', background_color='white')],
                  [Text('' * 10, key='erro', size=(31, 1),text_color='red')],
                  [sg.Text('PI 3,14',text_color='black', background_color='grey'),ReadFormButton('C',border_width=5), ReadFormButton('◀',border_width=5),sg.Text('15926 π',text_color='black', background_color='grey'),], #button_color=sg.TRANSPARENT_BUTTON, border_width=0
                  [ReadFormButton('7'), ReadFormButton('8'), ReadFormButton('9'), ReadFormButton('/')],
                  [ReadFormButton('4'), ReadFormButton('5'), ReadFormButton('6'), ReadFormButton('*')],
                  [ReadFormButton('1'), ReadFormButton('2'), ReadFormButton('3'), ReadFormButton('-')],
                  [ReadFormButton('.'), ReadFormButton('0'), ReadFormButton('='), ReadFormButton('+')],
                  ]
        #colors
        SetOptions(background_color='grey' )

        # Set PySimpleGUI
        form = FlexForm('CALCULATOR', default_button_element_size=(6, 2),
                        auto_size_buttons=False, grab_anywhere=False)

        form.Layout(layout)

        # Result Value
        Result = ''

        # Make Infinite Loop
        while True:
            # Button Values
            button, value = form.Read()

            # Check Press Button Values
            if button == 'C':
                Result = ''
                self.erro2 = ''
                form.FindElement('input').Update(Result)
                form.FindElement('erro').Update(self.erro2)

            elif button == '◀':
                Result = Result[:-1]
                form.FindElement('input').Update(Result)
            elif len(Result) == 18:
                self.erro2 = 'LIMITE ATINGIDO - Aperte C'
                form.FindElement('erro').Update(self.erro2)
            # Result
            elif button == '=':
                Answer = eval(Result)
                Answer = str(round(float(Answer), 3))
                form.FindElement('input').Update(Answer)
                Result = Answer
             # close the window
            elif button == 'Quit' or button == None:
                break
            else:
                Result += button
                form.FindElement('input').Update(Result)


calculadora = calculadora()
calculadora.iniciar()