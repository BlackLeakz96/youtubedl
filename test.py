import os
import sys
import subprocess
import platform
import setupui
import PyQt5
import autosetup
import mainwindow
from autosetup import *
from mainwindow import *
from setupui import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUix(self)


def autosetup():
    dlpath = input("Enter Download-Path:~$ ")
    sysxx = platform.system()
    if sysxx == 'Windows':
        windows()
    if sysxx == 'Linux':
        linux()
    else:
        print("OS not supported, exit().")
        sys.exit()

    print("\Auto setup... please wait while trying to setup *\n" + current_time)
    print("\nDetecting now runnin' os... \n")

    def windows():
        print("\nSeting up youtubedl for a Windows system!\n" + current_time)
        conf()
    #    Repo.clone_from("https://github.com/BlackLeakz96/youtubedl/", dlpath)
        os.system("cd " + dlpath)
        os.system("icacls " + dlpath + " /q /c /t /grant Users:F")
        os.system("python3 -m pip install -r requirements.txt")

    def linux():
        print("\nSeting up youtubedl for a linux system!\n" + current_time)
        conf()
    #    Repo.clone_from("https://github.com/BlackLeakz96/youtubedl/", dlpath)
        os.system("cd " + dlpath)
        os.system("sudo chmod 777 -R ./* && me=$(whoami) && sudo chown $me -hR ./*")
        os.system("python3 -m pip install -r requirements.txt")


def app_main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


def installer_main():
    app = QtWidgets.QApplication(sys.argv)
    window = InstWin()
    window.show()
    app.exec()


def main():
    decision = input("Do you want to install youtubedl ?(y/n) : > ")
    if decision == "y":
        print("Do you want to try (1)commandline-install or (2)gui?(1/2):> ")
        dec = input("nr.:> ")
        if dec == "1":
            autosetup()
        if dec == "2":
            installer_main()

    if decision == "n":
        app_main()






if __name__ == '__main__':
    main()
