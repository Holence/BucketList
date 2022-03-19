from DTPySide import *

class SuggestLineEdit(QLineEdit):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.suggest_list=QStringListModel(self)

        self.complter=QCompleter(self.suggest_list,self)
        self.complter.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.complter)
        self.complter.activated.connect(self.selected)
        self.textEdited.connect(self.showDropList)
    
    def setHeadquarter(self,Headquarter):
        self.Headquarter=Headquarter
    
    def selected(self, s):
        self.current_text=self.current_text+", "+s
        self.current_text=re.sub("^[, ]*","",self.current_text)
        self.current_text=re.sub("[, ]*$","",self.current_text)
        
        def slot():
            self.setText(self.current_text)
        
        QTimer.singleShot(0, slot)
    
    
    def showDropList(self):
        self.current_text=self.text()
        self.current_text=re.sub("^[, ]*","",self.current_text)
        self.current_text=re.sub("[, ]*$","",self.current_text)

        tags=[i.strip() for i in self.current_text.split(",")]

        suggest_list=[]
        for content in self.Headquarter.getData():
            for tag in content["tags"]:
                if tag not in suggest_list and tag not in tags:
                    suggest_list.append(tag)
		
        self.suggest_list.setStringList(suggest_list)