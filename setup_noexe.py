import os
import sys
import subprocess
import platform
import setupui
import datetime
from setupui import *
from git import Repo
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


    def install(self):
        checkx = self.accept.isChecked()
        if checkx == True:
            self.log.append("\nStarting installation....\n" + current_time)
            return True
        else:
            self.log.append("You need to accept the terms/conditions---" + current_time)
            return False
        while True:
            ossys = platform.system()
            self.log.append("\nDetected OverdriveSystem: " + ossys)
            self.log.append("\Configuring setup for your system....\n")
            if ossys == 'Windows':
                self.log.append("\nRequirements passed.\n")
                os.system('python3 -m pip install PySide2')
                os.system('python3 -m pip install PySide6')
                os.system('python3 -m pip install GitPython')
                os.system('python3 -m pip install pyqt5')
                os.system('python3 -m pip install PyQt5')
                os.system('python3 -m pip install pyqt5')
                Repo.clone_from("https://github.com/BlackLeakz96/youtubedl/", dlpath)
            if ossys == 'Linux':
                self.log.append("\nRequirements passed.\n")
                os.system('python3 -m pip install PySide2')
                os.system('python3 -m pip install PySide6')
                os.system('python3 -m pip install GitPython')
                os.system('python3 -m pip install pyqt5')
                os.system('python3 -m pip install PyQt5')
                os.system('python3 -m pip install pyqt5')
                Repo.clone_from("https://github.com/BlackLeakz96/youtubedl/", dlpath)






def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
