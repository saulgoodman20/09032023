import PySimpleGUI as gui

# KLASY
class TODOTask:
    def __init__(self, id, title, description, done):
        self.Id = id
        self.Title = title
        self.Description = description
        self.Done = done

class TODOTaskManager:
    def __init__(self):
        self.tasksList = []
        self.titlesList = []
    def updateListsAndCombo(self):
        self.tasksList.append(task)
        self.titlesList.append(task.Title)
        okno['titles_combo'].update(values=self.titlesList, value=self.titlesList[len(self.titlesList) - 1])
        self.showTask(self.findTaskWithTitle(task.Title))
    def clearTaskandList(self):
        okno['title'].update('')
        okno['description'].update('')
    def showTask(self, task):
        okno['inp_id'].update(task.Id)
        okno['inp_title'].update(task.Title)
        okno['inp_description'].update(task.Description)
        okno['inp_done'].update(task.Done)
    def findTaskWithTitle(self, title):
        for task in self.tasksList:
            if task.Title == title:
                return task
        return None
    def checkIfTaskExists(self, title):
        for task in self.tasksList:
            if task.Title == title:
                return True
        return False
    def toggleTaskFinished(self, task):
        task.Done = not task.Done
        self.showTask(task)
    def deleteTask(self, task):
        self.tasksList.remove(task)
        self.titlesList.remove(task.Title)
        okno['titles_combo'].update(values=self.titlesList, value=self.titlesList[len(self.titlesList) - 1])
        self.clearTaskandList()




gui.theme('DarkGrey4')
# GLOBALNE
taskNo = 1
tasksList = []
titlesList = []
taskManager = TODOTaskManager()

inputs_layout = [
    [gui.Text('Dodawanie zadania', font=('Comic Sans MS', 16))],
    [gui.Text('Tytul: '), gui.Input(key='title', size=(44, 1))],
    [gui.Multiline(key='description', size=(50, 4))]
]

buttons_layout = [
    [
        gui.Button('Dodaj', key='add', size=(10, 1)),
        gui.Button('Zamknij', key='close', size=(10, 1))
    ]
]

output_layout = [
    [gui.Text('Lista zadań', font=('Comic Sans MS', 16))],
    [gui.Combo([], key='titles_combo', size=(50, 1), enable_events=True)]
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
        gui.Checkbox("", key='inp_done', size=(0, 1), enable_events=True)
    ]
]

delete_button = [
    [gui.Button('Usuń', key='delete', size=(55, 1))]
]

layout = inputs_layout + buttons_layout + output_layout + headers + table + delete_button

okno = gui.Window('TODO List', layout, font=('Comic Sans MS', 12), element_justification='center', element_padding=(10, 5), no_titlebar=True, grab_anywhere=True)

# FUNKCJE
def updateListsAndCombo():
    tasksList.append(task)
    titlesList.append(task.Title)
    okno['titles_combo'].update(values=titlesList, value=titlesList[len(titlesList) - 1])

while True:
    event, values = okno.read()
    if event == "add":
        if (taskManager.checkIfTaskExists(values['title']) == False):
            task = TODOTask(taskNo, values['title'], values['description'], False)
            taskNo += 1
            taskManager.updateListsAndCombo()
            taskManager.clearTaskandList()
        else:
            gui.popup('Zadanie o takim tytule już istnieje!')
    if event == "close":
        break
    if event == "titles_combo":
        taskManager.showTask(taskManager.findTaskWithTitle(values['titles_combo']))
    if event == "inp_done":
        taskManager.toggleTaskFinished(taskManager.findTaskWithTitle(values['titles_combo']))
    if event == "delete":
        taskManager.deleteTask(taskManager.findTaskWithTitle(values['titles_combo']))
