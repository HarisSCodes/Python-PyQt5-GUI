
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(85, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Clicker = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.clicked(""))
        self.Clicker.setGeometry(QtCore.QRect(280, 220, 261, 91))
        self.Clicker.setStyleSheet("QPushButton\n"
"{\n"
"     border-radius: 20px;\n"
"     \n"
"    font: 22pt \"MS Sans Serif\";\n"
"    background-color: rgb(170, 0, 255);\n"
"}")
        self.Clicker.setObjectName("Clicker")
        self.Clicks = QtWidgets.QLabel(self.centralwidget)
        self.Clicks.setGeometry(QtCore.QRect(330, 50, 151, 61))
        self.Clicks.setStyleSheet("QLabel\n"
"{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    font: 24pt \"MS Shell Dlg 2\";\n"
"}")
        self.Clicks.setAlignment(QtCore.Qt.AlignCenter)
        self.Clicks.setObjectName("Clicks")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def clicked(self, pressed):
        self.Clicks.setText(str(eval(self.Clicks.text()+"+1")))
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Clicker.setText(_translate("MainWindow", "Click here!"))
        self.Clicks.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
