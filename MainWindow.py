# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 475)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(30, 60, 545, 300))
        self.table.setObjectName("table")
        self.table.setColumnCount(3)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setDefaultSectionSize(175)
        self.table.verticalHeader().setSortIndicatorShown(False)
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(30, 380, 93, 28))
        self.add_button.setStyleSheet("background: \'#5B5\';")
        self.add_button.setObjectName("add_button")
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(140, 380, 93, 28))
        self.delete_button.setStyleSheet("background: \'#C55\';")
        self.delete_button.setObjectName("delete_button")
        self.find_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.find_edit.setGeometry(QtCore.QRect(30, 20, 171, 22))
        self.find_edit.setInputMask("")
        self.find_edit.setText("")
        self.find_edit.setObjectName("find_edit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Пароли"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Пароль"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Сайт"))
        self.add_button.setText(_translate("MainWindow", "Добавить"))
        self.delete_button.setText(_translate("MainWindow", "Удалить"))
        self.find_edit.setPlaceholderText(_translate("MainWindow", "Найти по имени..."))
