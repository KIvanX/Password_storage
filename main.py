import random
import sys
import json
import pyperclip
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from PyQt6.QtGui import QColor
from MainWindow import Ui_MainWindow as MainWindowClass
from LoginWindow import Ui_MainWindow as LoginWindowClass
from cryptography.fernet import Fernet


class LoginWindow(QMainWindow, LoginWindowClass):
    def __init__(self, *args, **kwargs):
        super(LoginWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.act = 'Авторизация'
        self.login_button.clicked.connect(self.login)
        self.choose_act_button.clicked.connect(self.choose_act)

    def login(self):
        name = self.name_edit.text()
        key = self.password_edit.text()
        if self.act == 'Авторизация':
            if name in users and key == users[name]['master_password']:
                main_window.start(name)
                self.close()
            elif name not in users:
                self.name_edit.setStyleSheet('background: #F55')
                self.password_edit.setStyleSheet('background: white')
            else:
                self.name_edit.setStyleSheet('background: white')
                self.password_edit.setStyleSheet('background: #F55')
        else:
            if name not in users:
                users[name] = {'master_password': key, 'keys': {}}
                main_window.start(name)
                self.close()
            elif name in users:
                self.name_edit.setStyleSheet('background: #F55')

    def choose_act(self):
        self.name_edit.setStyleSheet('background: white')
        self.password_edit.setStyleSheet('background: white')
        self.choose_act_button.setText(self.act)
        self.act = 'Регистрация' if self.act == 'Авторизация' else 'Авторизация'
        self.setWindowTitle(self.act)
        self.login_button.setText('Войти' if self.act == 'Авторизация' else 'Зарегистрироваться')


class MainWindow(QMainWindow, MainWindowClass):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.name = ''
        self.add_button.clicked.connect(self.add_line)
        self.delete_button.clicked.connect(self.delete_lines)
        self.table.clicked.connect(self.table_click)
        self.find_edit.textChanged.connect(self.find_lines)

    def start(self, name):
        self.name = name
        self.show()
        for k, value in users[name]['keys'].items():
            self.add_line([k, len(value['password'])*'•', value['link']])

    def add_line(self, data=None):
        chars = [chr(i) for i in range(128) if 'a' <= chr(i).lower() <= 'z' or '0' <= chr(i) <= '9']
        password = ''.join([random.choice(chars) for _ in range(12)])

        n = self.table.rowCount()
        self.table.insertRow(n)
        self.table.setItem(n, 0, QTableWidgetItem(data[0] if data else ''))
        self.table.setItem(n, 1, QTableWidgetItem(data[1] if data else password))
        self.table.setItem(n, 2, QTableWidgetItem(data[2] if data else ''))

    def delete_lines(self):
        for row in range(self.table.rowCount()-1, -1, -1):
            for column in range(self.table.columnCount()-1, -1, -1):
                if self.table.item(row, column).isSelected():
                    self.table.removeRow(row)
                    break

    def find_lines(self):
        text = self.find_edit.text().lower()
        for row in range(self.table.rowCount()):
            t1, t2 = self.table.item(row, 0).text(), self.table.item(row, 2).text()
            if text and (text in t1.lower() or text in t2.lower()):
                for column in range(self.table.columnCount()):
                    self.table.item(row, column).setBackground(QColor(250, 150, 150))
            else:
                for column in range(self.table.columnCount()):
                    self.table.item(row, column).setBackground(QColor('white'))

    def table_click(self):
        for row in range(self.table.rowCount()):
            name = self.table.item(row, 0).text()
            if self.table.item(row, 1).isSelected():
                if name in users[self.name]['keys']:
                    self.table.item(row, 1).setText(users[self.name]['keys'][name]['password'])
                    pyperclip.copy(self.table.item(row, 1).text())

    def closeEvent(self, event):
        keys = {}
        for row in range(self.table.rowCount()):
            name = self.table.item(row, 0).text()
            psw = '' if name not in users[self.name]['keys'] else users[self.name]['keys'][name]['password']
            password = psw if psw else self.table.item(row, 1).text()
            link = self.table.item(row, 2).text()
            keys[name] = {'password': password, 'link': link}
        users[self.name]['keys'] = keys

        for user1 in users.values():
            user1['master_password'] = cipher.encrypt(user1['master_password'].encode()).decode()
            for key1 in user1['keys'].values():
                key1['password'] = cipher.encrypt(key1['password'].encode()).decode()

        with open('data.json', 'w') as file:
            json.dump(users, file, indent=4)


cipher = Fernet(b'LXcJ0NlNh9hPlNDkTfy1DKLh0BYJxElfuDJ7xnm2RW8=')
with open('data.json') as f:
    users = json.load(f)

for user in users.values():
    user['master_password'] = cipher.decrypt(user['master_password'].encode()).decode()
    for key in user['keys'].values():
        key['password'] = cipher.decrypt(key['password'].encode()).decode()

app = QApplication(sys.argv)
main_window = MainWindow()
login_window = LoginWindow()
login_window.show()
app.exec()
