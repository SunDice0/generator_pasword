from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_mainWindow
from random import randint

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.generate)
    def generate(self):
        if self.ui.check_num.isChecked() and self.ui.check_alp.isChecked():
            n=randint(8,16)
            res=""
            alp=["A", "B", "C", "D", "E","F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
            for i in range(n):
                j=randint(1,2)
                if j == 1:
                    g = randint(0,9)
                    res+=str(g)
                else:
                    g=randint(0,len(alp)-1)
                    y=randint(1,2)
                    if y == 1:
                        res+=alp[g]
                    else:
                        res+=alp[g].lower()
            self.ui.result.setText(res)
        elif self.ui.check_num.isChecked():
            n=randint(8,16)
            res = ""
            for i in range(n):
                j=randint(0,9)
                res+=str(j)
            self.ui.result.setText(res)
        elif self.ui.check_alp.isChecked():
            alp=["A", "B", "C", "D", "E","F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
            n=randint(8,16)
            res = ""
            for i in range(n):
                y=randint(1,2)
                j=randint(0,len(alp)-1)
                if y==1:
                    res+=alp[j]
                else:
                    res+=alp[j].lower()
            self.ui.result.setText(res)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()

