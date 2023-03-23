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
    def updateListsAndCombo(self, task, okno):
        self.tasksList.append(task)
        self.titlesList.append(task.Title)
        okno['titles_combo'].update(values=self.titlesList, value=self.titlesList[len(self.titlesList) - 1])
        self.showTask(self.findTaskWithTitle(task.Title), okno)
    def clearTaskandList(self, okno):
        okno['title'].update('')
        okno['description'].update('')
    def showTask(self, task, okno):
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
    def toggleTaskFinished(self, task, okno):
        if task is not None:
            task.Done = not task.Done
            self.showTask(task, okno)
    def deleteTask(self, title, okno):
        task = self.findTaskWithTitle(title)
        if task is not None:
            self.tasksList.remove(task)
            self.titlesList.remove(task.Title)
            okno['titles_combo'].update(values=self.titlesList, value="")
    def clearOutputs(self, okno):
        okno['inp_id'].update('')
        okno['inp_title'].update('')
        okno['inp_description'].update('')
        okno['inp_done'].update(False)
    def updateTaskFromTable(self, task, okno):
        #update the task data and update it in combo
        task.Title = okno['inp_title'].get()
        task.Description = okno['inp_description'].get()
        task.Done = okno['inp_done'].get()
        self.titlesList[self.tasksList.index(task)] = task.Title
        okno['titles_combo'].update(values=self.titlesList, value=task.Title)
        


gui.theme('DarkGrey4')
# GLOBALNE
tasksList = []
titlesList = []
taskManager = TODOTaskManager()

def MainWindow():
    taskNo = 1
    inputs_layout = [
        [gui.Text('Dodawanie zadania', font=('Comic Sans MS', 16))],
        [gui.Text('Tytul: '), gui.Input(key='title', size=(44, 1))],
        [gui.Multiline(key='description', size=(50, 4))]
    ]
    buttons_layout = [
        [
            gui.Button('Dodaj', key='add', size=(10, 1)),
            gui.Button('Zamknij', key='close', size=(10, 1)),
            gui.Button('Aktualizuj', key='update', size=(10, 1))
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
            gui.Input(key='inp_id', size=(3, 1), pad=(0, 0), disabled=True),
            gui.Input(key='inp_title', size=(15, 1), pad=(0, 0)),
            gui.Input(key='inp_description', size=(29, 1), pad=(0, 0)),
            gui.Checkbox("", key='inp_done', size=(0, 1), enable_events=True)
        ]
    ]
    delete_button = [
        [gui.Button('Usuń', key='delete', size=(55, 1))]
    ]
    logout_button = [
        [gui.Button('Wyloguj', key='logout', size=(55, 1))]
    ]
    layout = inputs_layout + buttons_layout + output_layout + headers + table + delete_button + logout_button
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
                taskManager.updateListsAndCombo(task, okno)
                taskManager.clearTaskandList(okno)
            else:
                gui.popup('Zadanie o takim tytule już istnieje!')
        if event == "close":
            break
        if event == "titles_combo":
            taskManager.showTask(taskManager.findTaskWithTitle(values['titles_combo']), okno)
        if event == "inp_done":
            taskManager.toggleTaskFinished(taskManager.findTaskWithTitle(values['titles_combo']), okno)
        if event == "delete":
            taskManager.deleteTask(values['titles_combo'], okno)
            taskManager.clearOutputs(okno)
        if event == "update":
            taskManager.updateTaskFromTable(taskManager.findTaskWithTitle(values['titles_combo']), okno)
            taskManager.clearOutputs(okno)
        if event == "logout":
            okno.close()
            loginWindow()
def loginWindow():
    login_area = [[gui.Text('Login: '), gui.Input(key='login', size=(20, 1))]]
    password_area = [[gui.Text('Hasło: '), gui.Input(key='password', size=(20, 1), password_char='•')]]
    buttons_bottom = [[gui.Button('Zaloguj', key='OK', size=(10, 1)), gui.Button('Załóż konto', key='register', size=(10, 1))]]

    layout = login_area + password_area + buttons_bottom

    okno = gui.Window("Login", layout, element_justification='right')
    while True:
        event, values = okno.read()
        if event == "OK":
            okno.close()
            MainWindow()
        if event == "register":
            okno.close()
            registerWindow()
def registerWindow():
    imie_area = [[gui.Text('Imię: '), gui.Input(key='imie', size=(20, 1))]]
    login_area = [[gui.Text('Login: '), gui.Input(key='login', size=(20, 1))]]
    password_area = [[gui.Text('Hasło: '), gui.Input(key='password', size=(20, 1), password_char='•')]]
    repeat_password_area = [[gui.Text('Powtórz hasło: '), gui.Input(key='repeat_password', size=(20, 1), password_char='•')]]
    buttons_bottom = [[gui.Button('Załóż konto', key='OK', size=(35, 1))]]

    layout = imie_area + login_area + password_area + repeat_password_area + buttons_bottom

    okno = gui.Window("Register", layout, element_justification='right')
    while True:
        event, values = okno.read()
        if event == "OK":
            break
if __name__ == '__main__':
    loginWindow()


            
