import PySimpleGUI as gui

# KLASY
class TODOTask:
    def __init__(self, id, title, description, done):
        self.Id = id
        self.Title = title
        self.Description = description
        self.Done = done



gui.theme('DarkGrey4')
# GLOBALNE
taskNo = 1
tasksList = []
titlesList = []

inputs_layout = [
    [gui.Text('Dodawanie zadania', font=('Comic Sans MS', 16))],
    [gui.Text('Tytul: '), gui.Input(key='title', size=(44, 1))],
    [gui.Multiline(key='description', size=(50, 4))],
]

buttons_layout = [
    [
        gui.Button('Dodaj', key='add', size=(10, 1)),
        gui.Button('Zamknij', key='close', size=(10, 1))
    ]
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

okno = gui.Window('TODO List', layout, font=('Comic Sans MS', 12), element_justification='center', element_padding=(10, 5), no_titlebar=True, grab_anywhere=True)

# FUNKCJE
def updateListsAndCombo():
    tasksList.append(task)
    titlesList.append(task.Title)
    okno['titles_combo'].update(values=titlesList, value=len(titlesList) - 1)

while True:
    event, values = okno.read()
    if event == "add":
        task = TODOTask(taskNo, values['inp_title'], values['inp_description'], False)
        taskNo += 1
        updateListsAndCombo()
    if event == "close":
        break
