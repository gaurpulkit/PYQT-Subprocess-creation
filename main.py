import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
import psutil
import subprocess


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(300, 200))

        self.newButton = QPushButton('Process 1 Start', self)
        self.newButton.clicked.connect(self.clickMethodA)
        self.newButton.show()
        self.newButton.move(0, 0)

        self.newButton2 = QPushButton('Process 2 Start', self)
        self.newButton2.clicked.connect(self.clickMethodB)
        self.newButton2.show()
        self.newButton2.move(100, 0)

        self.pauseButton = QPushButton('Process 1 Pause', self)
        self.pauseButton.clicked.connect(self.pauseMethodA)
        self.pauseButton.show()
        self.pauseButton.move(0, 30)
        self.pauseButton.setEnabled(False)

        self.pauseButton2 = QPushButton('Process 2 Pause', self)
        self.pauseButton2.clicked.connect(self.pauseMethodB)
        self.pauseButton2.show()
        self.pauseButton2.move(100, 30)
        self.pauseButton2.setEnabled(False)

        self.resumeButton = QPushButton('Process 1 Resume', self)
        self.resumeButton.clicked.connect(self.resumeMethodA)
        self.resumeButton.show()
        self.resumeButton.move(0, 60)
        self.resumeButton.setEnabled(False)

        self.resumeButton2 = QPushButton('Process 2 Resume', self)
        self.resumeButton2.clicked.connect(self.resumeMethodB)
        self.resumeButton2.show()
        self.resumeButton2.move(100, 60)
        self.resumeButton2.setEnabled(False)

        self.killButton = QPushButton('Process 1 Kill', self)
        self.killButton.clicked.connect(self.killMethodA)
        self.killButton.show()
        self.killButton.move(0, 90)
        self.killButton.setEnabled(False)

        self.killButton2 = QPushButton('Process 2 Kill', self)
        self.killButton2.clicked.connect(self.killMethodB)
        self.killButton2.show()
        self.killButton2.move(100, 90)
        self.killButton2.setEnabled(False)

    def clickMethodA(self):
        p1=subprocess.Popen(["python","file.py","-f","a.csv"])
        self.p1= psutil.Process(pid=p1.pid)
        self.pauseButton.setEnabled(True)
        self.killButton.setEnabled(True)
        self.newButton.setDisabled(True)

    def clickMethodB(self):
        p2=subprocess.Popen(["python","file.py","-f","b.csv"])
        self.p2= psutil.Process(pid=p2.pid)
        self.pauseButton2.setEnabled(True)
        self.killButton2.setEnabled(True)
        self.newButton2.setDisabled(True)

    def pauseMethodA(self):
        self.p1.suspend()
        self.pauseButton.setDisabled(True)
        self.resumeButton.setDisabled(False)

    def pauseMethodB(self):
        self.p2.suspend()
        self.pauseButton2.setDisabled(True)
        self.resumeButton2.setDisabled(False)

    def resumeMethodA(self):
        self.p1.resume()
        self.pauseButton.setDisabled(False)
        self.resumeButton.setDisabled(True)

    def resumeMethodB(self):
        self.p2.resume()
        self.pauseButton2.setDisabled(False)
        self.resumeButton2.setDisabled(True)

    def killMethodA(self):
        self.p1.kill()
        self.pauseButton.setEnabled(False)
        self.resumeButton.setEnabled(False)
        self.killButton.setEnabled(False)
        self.newButton.setEnabled(True)

    def killMethodB(self):
        self.p2.kill()
        self.pauseButton2.setEnabled(False)
        self.resumeButton2.setEnabled(False)
        self.killButton2.setEnabled(False)
        self.newButton2.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )