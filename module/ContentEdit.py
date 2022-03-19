from DTPySide import *
from session.MainSession import MainSession

from module.Ui_ContentEdit import Ui_ContentEdit
class ContentEdit(Ui_ContentEdit,QWidget):

    deleted=Signal()

    def __init__(self, Headquarter:MainSession) -> None:
        super().__init__()
        self.setupUi(self)
        self.Headquarter=Headquarter
        self.setStyleSheet("font-size:14pt")

        label_note=QLabel("(If left blank, tag is assumed to be 🏠 — the main page tag.)")
        label_note.setStyleSheet("font-size: 10pt;")
        self.verticalLayout_tags.insertWidget(1,label_note)

        self.comboBox_status.addItems(["🚄","☕","⌚","❌"])
        self.comboBox_status.setStyleSheet("font-size:14pt")
        self.plainTextEdit.setStyleSheet("font-size:12pt")
        self.setMinimumSize(600,300)

        def slot0():
            self.dateEdit_fin.setMinimumDate(self.dateEdit_add.date())
        self.dateEdit_add.dateChanged.connect(slot0)

        def slot1():
            if self.checkBox.checkState()==Qt.Checked:
                self.stackedWidget.setCurrentIndex(1)
            else:
                self.stackedWidget.setCurrentIndex(0)
        self.checkBox.stateChanged.connect(slot1)

        self.dateEdit_add.setDate(WhatDayIsToday(1))
        self.dateEdit_fin.setDate(WhatDayIsToday(1))

        self.lineEdit_tags.setHeadquarter(self.Headquarter)

        self.pushButton_delete.setStyleSheet("background:%s; border:none; min-height:32px; max-height:32px; min-width:32px; max-width:32px; icon-size:24px;"%self.Headquarter.app.color_list[2])
        self.pushButton_delete.setIcon(IconFromCurrentTheme("trash-2.svg"))
        
        def slot2():
            if DTFrame.DTConfirmBox(self,"Delete Confirm","Do you want to delete this plan?",DTIcon.Warning()).exec_():
                self.deleted.emit()
        self.pushButton_delete.clicked.connect(slot2)
    
    def setData(self, index):
        content=self.Headquarter.getData()[index]
        tags=content["tags"]
        text=content["text"]
        status=content["status"]
        date_add=content["date_add"]
        date_fin=content["date_fin"]
        self.dateEdit_add.setDate(QDate.fromString(date_add,"yyyy.M.d"))
        
        self.dateEdit_fin.setMinimumDate(self.dateEdit_add.date())
        if status=="✔":
            self.checkBox.setCheckState(Qt.Checked)
            self.dateEdit_fin.setDate(QDate.fromString(date_fin,"yyyy.M.d"))
        else:
            self.comboBox_status.setCurrentIndex(["🚄","☕","⌚","❌"].index(status))
        
        self.lineEdit_tags.setText(", ".join(tags))
        self.plainTextEdit.setPlainText(text)