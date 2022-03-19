# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ContentEdit.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from widget import SuggestLineEdit


class Ui_ContentEdit(object):
    def setupUi(self, ContentEdit):
        if not ContentEdit.objectName():
            ContentEdit.setObjectName(u"ContentEdit")
        ContentEdit.resize(604, 405)
        self.horizontalLayout = QHBoxLayout(ContentEdit)
        self.horizontalLayout.setSpacing(18)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(ContentEdit)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.dateEdit_add = QDateEdit(ContentEdit)
        self.dateEdit_add.setObjectName(u"dateEdit_add")

        self.verticalLayout_3.addWidget(self.dateEdit_add)

        self.checkBox = QCheckBox(ContentEdit)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_3.addWidget(self.checkBox)

        self.stackedWidget = QStackedWidget(ContentEdit)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_plan = QWidget()
        self.page_plan.setObjectName(u"page_plan")
        self.verticalLayout_2 = QVBoxLayout(self.page_plan)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.page_plan)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.comboBox_status = QComboBox(self.page_plan)
        self.comboBox_status.setObjectName(u"comboBox_status")

        self.verticalLayout_2.addWidget(self.comboBox_status)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page_plan)
        self.page_finish = QWidget()
        self.page_finish.setObjectName(u"page_finish")
        self.verticalLayout = QVBoxLayout(self.page_finish)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.page_finish)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.dateEdit_fin = QDateEdit(self.page_finish)
        self.dateEdit_fin.setObjectName(u"dateEdit_fin")

        self.verticalLayout.addWidget(self.dateEdit_fin)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.page_finish)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.pushButton_delete = QPushButton(ContentEdit)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.verticalLayout_3.addWidget(self.pushButton_delete)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_tags = QVBoxLayout()
        self.verticalLayout_tags.setSpacing(2)
        self.verticalLayout_tags.setObjectName(u"verticalLayout_tags")
        self.label_5 = QLabel(ContentEdit)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.verticalLayout_tags.addWidget(self.label_5)

        self.lineEdit_tags = SuggestLineEdit(ContentEdit)
        self.lineEdit_tags.setObjectName(u"lineEdit_tags")

        self.verticalLayout_tags.addWidget(self.lineEdit_tags)


        self.verticalLayout_4.addLayout(self.verticalLayout_tags)

        self.verticalLayout_text = QVBoxLayout()
        self.verticalLayout_text.setSpacing(2)
        self.verticalLayout_text.setObjectName(u"verticalLayout_text")
        self.label_4 = QLabel(ContentEdit)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.verticalLayout_text.addWidget(self.label_4)

        self.plainTextEdit = QPlainTextEdit(ContentEdit)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_text.addWidget(self.plainTextEdit)


        self.verticalLayout_4.addLayout(self.verticalLayout_text)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(ContentEdit)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ContentEdit)
    # setupUi

    def retranslateUi(self, ContentEdit):
        ContentEdit.setWindowTitle(QCoreApplication.translate("ContentEdit", u"Form", None))
        self.label.setText(QCoreApplication.translate("ContentEdit", u"Added at", None))
        self.checkBox.setText(QCoreApplication.translate("ContentEdit", u"Mission Accomplished", None))
        self.label_3.setText(QCoreApplication.translate("ContentEdit", u"Status", None))
        self.label_2.setText(QCoreApplication.translate("ContentEdit", u"Finished at", None))
        self.pushButton_delete.setText("")
        self.label_5.setText(QCoreApplication.translate("ContentEdit", u"Tags (Separated with comma)", None))
        self.label_4.setText(QCoreApplication.translate("ContentEdit", u"Text (Markdown Supported)", None))
    # retranslateUi

