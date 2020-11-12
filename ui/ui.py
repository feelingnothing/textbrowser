# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.minimize = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimize.sizePolicy().hasHeightForWidth())
        self.minimize.setSizePolicy(sizePolicy)
        self.minimize.setMinimumSize(QtCore.QSize(30, 30))
        self.minimize.setMaximumSize(QtCore.QSize(30, 30))
        self.minimize.setText("")
        self.minimize.setFlat(True)
        self.minimize.setObjectName("minimize")
        self.gridLayout.addWidget(self.minimize, 0, 4, 1, 1)
        self.hide = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hide.sizePolicy().hasHeightForWidth())
        self.hide.setSizePolicy(sizePolicy)
        self.hide.setMinimumSize(QtCore.QSize(30, 30))
        self.hide.setMaximumSize(QtCore.QSize(30, 30))
        self.hide.setText("")
        self.hide.setFlat(True)
        self.hide.setObjectName("hide")
        self.gridLayout.addWidget(self.hide, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 1, 1, 1)
        self.close = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close.sizePolicy().hasHeightForWidth())
        self.close.setSizePolicy(sizePolicy)
        self.close.setMinimumSize(QtCore.QSize(30, 30))
        self.close.setMaximumSize(QtCore.QSize(30, 30))
        self.close.setText("")
        self.close.setFlat(True)
        self.close.setObjectName("close")
        self.gridLayout.addWidget(self.close, 0, 5, 1, 1)
        self.menubar = QtWidgets.QMenuBar(self.centralwidget)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.gridLayout.addWidget(self.menubar, 1, 0, 1, 5)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setObjectName("text")
        self.gridLayout.addWidget(self.text, 2, 0, 1, 6)
        main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusBar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "TextBrowser"))
        self.title.setText(_translate("main", "TextBrowser"))