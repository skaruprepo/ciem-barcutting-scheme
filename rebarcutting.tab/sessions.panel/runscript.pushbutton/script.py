#! python3
import sys
import os
import logging

sysPath = [
    'C:\\Users\\saris\\AppData\\Local\\Programs\\Python\\Python38',
    'C:\\Users\\saris\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip',
    'C:\\Users\\saris\\AppData\\Local\\Programs\\Python\\Python38\\DLLs',
    'C:\\Users\\saris\\AppData\\Local\\Programs\\Python\\Python38\\lib',
    'C:\\Users\\saris\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages',
    'C:\\Users\\saris\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages\\win32',
    'C:\\Users\\saris\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages\\win32\\lib',
    'C:\\Users\\saris\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages\\Pythonwin',
    'C:\\Users\\saris\\AppData\\Roaming\\pyRevit\\Extensions\\rebarcutting.extension\\libs',
    'C:\\Users\\saris\\AppData\\Roaming\\pyRevit\\Extensions\\rebarcutting.extension\\gui',
]

#    'C:\\Users\\Saris.Krainara\\AppData\\Roaming\\Python\\Python38\\site-packages',
#    'C:\\Users\\Saris.Krainara\\AppData\\Roaming\\Python\\Python38\\site-packages\\win32',
#    'C:\\Users\\Saris.Krainara\\AppData\\Roaming\\Python\\Python38\\site-packages\\win32\\lib',
#    'C:\\Users\\Saris.Krainara\\AppData\\Roaming\\Python\\Python38\\site-packages\\Pythonwin',

for path in sysPath:
    sys.path.append(path)

fileDirectory = os.path.dirname(os.path.realpath(__file__))
os.chdir(fileDirectory)

from PySide2.QtWidgets import QApplication
from barcutclass import RebarCache
from maingui import MainGUI

if __name__ == "__main__":

    RebarCache.clearCache()
    if QApplication.instance() is None:
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    window = MainGUI()
    window.show()
    app.exec_()