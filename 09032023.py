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

headers = [
    [
        gui.Text('ID', size=(7, 1), pad=(0, 0), justification='left'),
        gui.Text('Tytul', size=(15, 1), pad=(0, 0), justification='left'),
        gui.Text('Opis', size=(26, 1), pad=(0, 0), justification='center'),
        gui.Text('✓', size=(2, 1), pad=(0, 0), justification='left')
    ]
]

table = [
    [
        gui.Input(key='inp_id', size=(3, 1), pad=(0, 0)),
        gui.Input(key='inp_title', size=(15, 1), pad=(0, 0)),
        gui.Input(key='inp_description', size=(29, 1), pad=(0, 0)),
        gui.Checkbox("", key='inp_done', size=(0, 1))
    ]
]

layout = inputs_layout + buttons_layout + output_layout + headers + table

okno = gui.Window('TODO List', layout, font=('Comic Sans MS', 12), element_justification='center')
okno.read()
