# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Block.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Block(object):
    def setupUi(self, Block):
        if not Block.objectName():
            Block.setObjectName(u"Block")
        Block.resize(362, 203)
        self.horizontalLayout = QHBoxLayout(Block)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 12, 5)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_status = QLabel(Block)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.label_status)

        self.pushButton_edit = QPushButton(Block)
        self.pushButton_edit.setObjectName(u"pushButton_edit")
        self.pushButton_edit.setFlat(True)

        self.verticalLayout_3.addWidget(self.pushButton_edit)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_text = QLabel(Block)
        self.label_text.setObjectName(u"label_text")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_text.sizePolicy().hasHeightForWidth())
        self.label_text.setSizePolicy(sizePolicy)
        self.label_text.setTextFormat(Qt.MarkdownText)
        self.label_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_text.setWordWrap(True)
        self.label_text.setOpenExternalLinks(True)
        self.label_text.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_4.addWidget(self.label_text)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_tags = QLabel(Block)
        self.label_tags.setObjectName(u"label_tags")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_tags.sizePolicy().hasHeightForWidth())
        self.label_tags.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.label_tags)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_add = QLabel(Block)
        self.label_add.setObjectName(u"label_add")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_add.sizePolicy().hasHeightForWidth())
        self.label_add.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.label_add)

        self.label_fin = QLabel(Block)
        self.label_fin.setObjectName(u"label_fin")
        sizePolicy2.setHeightForWidth(self.label_fin.sizePolicy().hasHeightForWidth())
        self.label_fin.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.label_fin)

        self.verticalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.retranslateUi(Block)

        QMetaObject.connectSlotsByName(Block)
    # setupUi

    def retranslateUi(self, Block):
        Block.setWindowTitle(QCoreApplication.translate("Block", u"Form", None))
        self.label_status.setText("")
        self.pushButton_edit.setText("")
        self.label_text.setText("")
        self.label_tags.setText("")
        self.label_add.setText("")
        self.label_fin.setText("")
    # retranslateUi

