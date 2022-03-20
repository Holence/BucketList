from DTPySide import *
from session.MainSession import MainSession

from module.Ui_SearchToDo import Ui_SearchToDo
class SearchToDo(Ui_SearchToDo,QWidget):
    def __init__(self, parent, Headquarter:MainSession) -> None:
        super().__init__(parent)
        self.Headquarter=Headquarter
        self.setupUi(self)

        self.lineEdit.returnPressed.connect(self.showSearch)
        self.lineEdit.setFocus()
    
    def showSearch(self):
        search=self.lineEdit.text().lower()
        result=""
        for content in self.Headquarter.getData():
            text=content["text"].lower()
            if search in text:
                text="\n".join(["\n> "+i+"\n>" for i in content["text"].split()]).replace("-","\\-")
                result+=f"""**Tags**: {content["tags"]}

**Text**: { text }

**Status**: {content["status"]}

**Date Added**: {content["date_add"]}

**Date Finished**: {content["date_fin"]}

---

"""
        self.textBrowser.setMarkdown(result[:-7])