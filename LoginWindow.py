# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(533, 349)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_edit.setGeometry(QtCore.QRect(180, 70, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_edit.setFont(font)
        self.name_edit.setText("")
        self.name_edit.setObjectName("name_edit")
        self.password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_edit.setGeometry(QtCore.QRect(180, 130, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_edit.setFont(font)
        self.password_edit.setObjectName("password_edit")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(60, 229, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("")
        self.login_button.setObjectName("login_button")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(60, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.choose_act_button = QtWidgets.QPushButton(self.centralwidget)
        self.choose_act_button.setGeometry(QtCore.QRect(330, 250, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choose_act_button.setFont(font)
        self.choose_act_button.setStyleSheet("")
        self.choose_act_button.setObjectName("choose_act_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 533, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "??????????????????????"))
        self.login_button.setText(_translate("MainWindow", "??????????"))
        self.label_1.setText(_translate("MainWindow", "??????"))
        self.label_2.setText(_translate("MainWindow", "????????????"))
        self.choose_act_button.setText(_translate("MainWindow", "??????????????????????"))
