from DTPySide import *

from session.MainSession import MainSession
from widget.Ui_Block import Ui_Block
class Block(Ui_Block,QWidget):
    def __init__(self, Headquarter:MainSession, index) -> None:
        super().__init__()
        self.setupUi(self)
        self.Headquarter=Headquarter
        self.index=index
    
        color=self.Headquarter.app.color_list[0]
        color2=self.Headquarter.app.color_list[1]
        self.label_status.setStyleSheet("min-height:44px; max-height:44px; min-width:44px; max-width:44px; border-bottom: 2px ridge %s"%color)
        self.label_text.setStyleSheet("font-size:16pt; border:5px ridge %s; background: %s;"%(color,color2)) # 为什么不加上background，就显示不出markdown的分割线？？
        self.pushButton_edit.setStyleSheet("background:%s; border:none; min-height:20px; max-height:20px; min-width:20px; max-width:20px; icon-size:16px;"%self.Headquarter.app.color_list[2])
        self.pushButton_edit.setIcon(IconFromCurrentTheme("edit-3.svg"))
        self.label_tags.setStyleSheet(f"border-left: 5px ridge {color}; font-size:12pt;")
        self.label_add.setStyleSheet("font-size:13pt")
        self.label_fin.setStyleSheet("font-size:13pt")
        self.pushButton_edit.clicked.connect(self.edit)

        self.refresh()
    
    def refresh(self):

        content=self.Headquarter.getData()[self.index]
        text=content["text"]
        status=content["status"]
        tags=content["tags"]
        date_add=content["date_add"]
        date_fin=content["date_fin"]

        self.label_status.setText(status)
        self.label_text.setText(text)
        self.label_tags.setText("   "+", ".join(tags))
        self.label_add.setText("Added at: %s"%date_add)
        if date_fin!=None:
            self.label_fin.setText("Finished at: %s"%date_fin)
        else:
            self.label_fin.hide()
    
    def edit(self):
        dlg=DTFrame.DTDialog(self.window(),"Edit")
        
        from module.ContentEdit import ContentEdit
        widget=ContentEdit(self.Headquarter)
        dlg.setCentralWidget(widget)
        widget.setData(self.index)
        
        dlg.adjustSize()
        MoveToCenterOfScreen(dlg)
        
        def slot():
            dlg.close()
            self.Headquarter.deleteData(self.index)
            
            self.deleteLater()
            self.Headquarter.mainwindow.refreshTabBar()

        widget.deleted.connect(slot)

        if dlg.exec_():

            tags=self.Headquarter.ConvertToTagList(widget.lineEdit_tags.text())
            
            text=widget.plainTextEdit.toPlainText()
            if text=="":
                DTFrame.DTMessageBox(self.window(),"Warning","text is empty!",DTIcon.Warning())
                return
            
            if widget.checkBox.checkState()==Qt.Checked:
                status="✔"
                date_fin=widget.dateEdit_fin.date()
            else:
                status=widget.comboBox_status.currentText()
                date_fin=None
            date_add=widget.dateEdit_add.date()
            self.Headquarter.editData(self.index,tags,text,status,date_add,date_fin)
            
            self.refresh()
            QTimer.singleShot(0, self.window().mainwindow.refresh)