import os
import sys
import datetime
import platform
import PyQt5
import youtube_dl
from datetime import datetime
#from git import Repo
from PyQt5 import QtCore, QtGui, QtWidgets

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

class Ui_Installer(object):
    def setupUi(self, InstWin):
        InstWin.setObjectName("InstWin")
        InstWin.resize(800, 600)
        InstWin.setStyleSheet("background-color:    rgb(17, 17, 17);\n"
"color:    rgb(0, 255, 225);\n"
"")
        self.centralwidget = QtWidgets.QWidget(InstWin)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 20, 301, 31))
        self.label.setObjectName("label")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 550, 791, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 320, 381, 19))
        self.checkBox.setObjectName("checkBox")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 350, 80, 21))
        self.pushButton.setObjectName("pushButton")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 60, 761, 251))
        self.textBrowser.setObjectName("textBrowser")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(InstWin)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(InstWin)
        QtCore.QMetaObject.connectSlotsByName(InstWin)

    def retranslateUi(self, InstWin):
        _translate = QtCore.QCoreApplication.translate
        InstWin.setWindowTitle(_translate("InstWin", "InstWin"))
        self.label.setText(_translate("InstWin", "Youtube-Downloader Installation-Manager | by blackspace.cf"))
        self.checkBox.setText(_translate("InstWin", "Accept"))
        self.pushButton.setText(_translate("InstWin", "Install"))

class InstWin(QtWidgets.QMainWindow, Ui_Installer):
    def __init__(self, *args, obj=None, **kwargs):
        super(InstWin, self).__init__(*args, **kwargs)
        self.setupUi(self)






class Ui_MainWindow(object):
    def setupUix(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 472)
        MainWindow.setStyleSheet("background-color:    rgb(0, 0, 0);\n"
"color: rgb(0, 255, 106);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.inpuri = QtWidgets.QLineEdit(self.centralwidget)
        self.inpuri.setGeometry(QtCore.QRect(10, 350, 681, 21))
        self.inpuri.setObjectName("inpuri")

        self.dlbtn = QtWidgets.QPushButton(self.centralwidget)
        self.dlbtn.setGeometry(QtCore.QRect(710, 350, 80, 21))
        self.dlbtn.setObjectName("dlbtn")
        self.dlbtn.clicked.connect(self.load)

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 781, 281))
        self.groupBox.setObjectName("groupBox")

        self.console = QtWidgets.QTextBrowser(self.groupBox)
        self.console.setGeometry(QtCore.QRect(0, 20, 781, 261))
        self.console.setObjectName("console")
        self.console.append("\n================================================\n")
        self.console.append("\n== Youtube-Downloader |by BlackLeakz 16042022 ==\n")
        self.console.append("\n================================================\n")
        self.console.append("\n== This is the console log - verbose = True   ==\n")
        self.console.append("\n================================================\n")
        self.console.append("\n~~~ https://github.com/BlackLeakz96/youtubedl ~~\n")
        self.console.append("\nConsoleLog@" + current_time + " oClock")
        self.console.append("\n\n\n")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 330, 251, 16))
        self.label.setObjectName("label")

        self.groupBox.raise_()
        self.inpuri.raise_()
        self.dlbtn.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menuBar.setObjectName("menuBar")

        self.menuMain = QtWidgets.QMenu(self.menuBar)
        self.menuMain.setObjectName("menuMain")
        MainWindow.setMenuBar(self.menuBar)

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")

        self.actionAbout_2 = QtWidgets.QAction(MainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")

        self.actionUpdate_2 = QtWidgets.QAction(MainWindow)
        self.actionUpdate_2.setObjectName("actionUpdate_2")

        self.actionWebsite = QtWidgets.QAction(MainWindow)
        self.actionWebsite.setObjectName("actionWebsite")

        self.menuMain.addAction(self.actionAbout_2)
        self.menuMain.addAction(self.actionUpdate_2)
        self.menuMain.addAction(self.actionWebsite)
        self.menuBar.addAction(self.menuMain.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube-Downloader"))
        self.dlbtn.setText(_translate("MainWindow", "Download"))
        self.groupBox.setTitle(_translate("MainWindow", "Console"))
        self.label.setText(_translate("MainWindow", "Enter download- url: "))
        self.menuMain.setTitle(_translate("MainWindow", "Main"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionAbout_2.setText(_translate("MainWindow", "About"))
        self.actionUpdate_2.setText(_translate("MainWindow", "Update"))
        self.actionWebsite.setText(_translate("MainWindow", "Website"))

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
