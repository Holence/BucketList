# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(476, 362)
        self.actionAdd_ToDo = QAction(MainWindow)
        self.actionAdd_ToDo.setObjectName(u"actionAdd_ToDo")
        self.actionExport_to_Json = QAction(MainWindow)
        self.actionExport_to_Json.setObjectName(u"actionExport_to_Json")
        self.actionCheck_Data_Completeness = QAction(MainWindow)
        self.actionCheck_Data_Completeness.setObjectName(u"actionCheck_Data_Completeness")
        self.actionCheck_Data_Completeness.setShortcutContext(Qt.ApplicationShortcut)
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(MainWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.tabWidget)

        self.frame = QFrame(MainWindow)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 456, 320))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.frame)

        self.checkBoxsGroup = QWidget(MainWindow)
        self.checkBoxsGroup.setObjectName(u"checkBoxsGroup")
        self.checkBoxLayout = QHBoxLayout(self.checkBoxsGroup)
        self.checkBoxLayout.setSpacing(12)
        self.checkBoxLayout.setObjectName(u"checkBoxLayout")
        self.checkBoxLayout.setContentsMargins(12, 10, 0, 6)

        self.verticalLayout.addWidget(self.checkBoxsGroup)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.actionAdd_ToDo.setText(QCoreApplication.translate("MainWindow", u"Add ToDo", None))
#if QT_CONFIG(tooltip)
        self.actionAdd_ToDo.setToolTip(QCoreApplication.translate("MainWindow", u"Add ToDo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionAdd_ToDo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionExport_to_Json.setText(QCoreApplication.translate("MainWindow", u"Export to Json", None))
        self.actionCheck_Data_Completeness.setText(QCoreApplication.translate("MainWindow", u"Check Data Completeness", None))
#if QT_CONFIG(shortcut)
        self.actionCheck_Data_Completeness.setShortcut(QCoreApplication.translate("MainWindow", u"F4", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

