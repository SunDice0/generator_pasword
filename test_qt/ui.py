# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generate.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(519, 402)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Text = QtWidgets.QLabel(self.centralwidget)
        self.Text.setGeometry(QtCore.QRect(180, 10, 195, 24))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.Text.setFont(font)
        self.Text.setAlignment(QtCore.Qt.AlignCenter)
        self.Text.setObjectName("Text")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(170, 100, 195, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.result.setFont(font)
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setObjectName("result")
        self.check_num = QtWidgets.QCheckBox(self.centralwidget)
        self.check_num.setGeometry(QtCore.QRect(10, 140, 521, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.check_num.setFont(font)
        self.check_num.setObjectName("check_num")
        self.check_alp = QtWidgets.QCheckBox(self.centralwidget)
        self.check_alp.setGeometry(QtCore.QRect(10, 180, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.check_alp.setFont(font)
        self.check_alp.setObjectName("check_alp")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 250, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("Border:3px solid yellow;\n"
"Border-radius:10px; \n"
"Background-color:grey;\n"
"color:yellow;\n"
"padding:10px;")
        self.pushButton.setObjectName("pushButton")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Вікно"))
        self.Text.setText(_translate("mainWindow", "Генератор паролів"))
        self.result.setText(_translate("mainWindow", "Тут буде результат"))
        self.check_num.setText(_translate("mainWindow", "Використовувати числа"))
        self.check_alp.setText(_translate("mainWindow", "Використовувати алфавіт"))
        self.pushButton.setText(_translate("mainWindow", "Сгенерувати"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
