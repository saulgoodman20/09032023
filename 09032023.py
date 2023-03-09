import PySimpleGUI as gui
gui.theme('DarkGrey4')

inputs_layout = [
    [gui.Text('Dodawanie zadania', font=('Comic Sans MS', 16))],
    [gui.Text('Tytul: '), gui.Input(key='title', size=(44, 1))],
    [gui.Multiline(key='description', size=(50, 4))],
]

buttons_layout = [
    [gui.Button('Dodaj', key='add', size=(10, 1)), gui.Button('Zamknij', key='close', size=(10, 1))]
]

output_layout = [
    [gui.Text('Lista zadań', font=('Comic Sans MS', 16))],
    [gui.Combo([], key='titles_combo', size=(50, 1))]
]

layout = inputs_layout + buttons_layout + output_layout

okno = gui.Window('TODO List', layout, font=('Comic Sans MS', 12), element_justification='center')
okno.read()
