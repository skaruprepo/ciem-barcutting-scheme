# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maingui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainGUI(object):
    def setupUi(self, MainGUI):
        if not MainGUI.objectName():
            MainGUI.setObjectName(u"MainGUI")
        MainGUI.resize(800, 143)
        self.actionClear = QAction(MainGUI)
        self.actionClear.setObjectName(u"actionClear")
        self.actionClose = QAction(MainGUI)
        self.actionClose.setObjectName(u"actionClose")
        self.centralwidget = QWidget(MainGUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(150, 0))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.stockLength = QLineEdit(self.centralwidget)
        self.stockLength.setObjectName(u"stockLength")

        self.horizontalLayout.addWidget(self.stockLength)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(150, 0))
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.outputPath = QLineEdit(self.centralwidget)
        self.outputPath.setObjectName(u"outputPath")

        self.horizontalLayout_2.addWidget(self.outputPath)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnSearchPath = QPushButton(self.centralwidget)
        self.btnSearchPath.setObjectName(u"btnSearchPath")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnSearchPath.sizePolicy().hasHeightForWidth())
        self.btnSearchPath.setSizePolicy(sizePolicy1)
        self.btnSearchPath.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.btnSearchPath)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btnRun = QPushButton(self.centralwidget)
        self.btnRun.setObjectName(u"btnRun")
        sizePolicy1.setHeightForWidth(self.btnRun.sizePolicy().hasHeightForWidth())
        self.btnRun.setSizePolicy(sizePolicy1)
        self.btnRun.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.btnRun)

        self.btnClose = QPushButton(self.centralwidget)
        self.btnClose.setObjectName(u"btnClose")
        sizePolicy1.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy1)
        self.btnClose.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        MainGUI.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainGUI)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuFiles = QMenu(self.menubar)
        self.menuFiles.setObjectName(u"menuFiles")
        MainGUI.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainGUI)
        self.statusbar.setObjectName(u"statusbar")
        MainGUI.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFiles.menuAction())
        self.menuFiles.addAction(self.actionClear)
        self.menuFiles.addAction(self.actionClose)

        self.retranslateUi(MainGUI)
        self.actionClose.triggered.connect(MainGUI.close)
        self.btnClose.clicked.connect(MainGUI.close)

        QMetaObject.connectSlotsByName(MainGUI)
    # setupUi

    def retranslateUi(self, MainGUI):
        MainGUI.setWindowTitle(QCoreApplication.translate("MainGUI", u"Bar Cutting Scheme Generator (Revit 2023)", None))
        self.actionClear.setText(QCoreApplication.translate("MainGUI", u"Clear", None))
        self.actionClose.setText(QCoreApplication.translate("MainGUI", u"Close", None))
        self.label.setText(QCoreApplication.translate("MainGUI", u"Stock Length (mm)", None))
        self.label_2.setText(QCoreApplication.translate("MainGUI", u"Output Path", None))
        self.btnSearchPath.setText(QCoreApplication.translate("MainGUI", u". . .", None))
        self.btnRun.setText(QCoreApplication.translate("MainGUI", u"Run", None))
        self.btnClose.setText(QCoreApplication.translate("MainGUI", u"Close", None))
        self.menuFiles.setTitle(QCoreApplication.translate("MainGUI", u"File", None))
    # retranslateUi

