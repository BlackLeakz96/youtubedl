import os
import sys
import subprocess
import platform
import setupui
import datetime
from setupui import *
from git import Repo
from datetime import datetime
#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *

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
                detdir = self.inpdir.text()
                Repo.clone_from("https://github.com/BlackLeakz96/youtubedl/", detdir)
                #Repo.clone_from("https://github.com/BlackLeakz96/youtubedl/", '%appdata%')
            #    self.log.append("\nDownloaded repository to %appdata%...\n")



            if ossys == 'Linux':
                self.log.append("How do you run an windows executable file without emulating windows on linux?lel, u wonder me <3 this is only the windows.exe installmanager <33")
        else:
            self.log.append("You need to accept the terms/conditions---" + current_time)
            return False
    #    while True:







def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
