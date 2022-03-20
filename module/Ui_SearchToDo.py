# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SearchToDo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SearchToDo(object):
    def setupUi(self, SearchToDo):
        if not SearchToDo.objectName():
            SearchToDo.setObjectName(u"SearchToDo")
        SearchToDo.resize(382, 317)
        self.verticalLayout = QVBoxLayout(SearchToDo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(SearchToDo)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.textBrowser = QTextBrowser(SearchToDo)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)


        self.retranslateUi(SearchToDo)

        QMetaObject.connectSlotsByName(SearchToDo)
    # setupUi

    def retranslateUi(self, SearchToDo):
        SearchToDo.setWindowTitle(QCoreApplication.translate("SearchToDo", u"Form", None))
    # retranslateUi

