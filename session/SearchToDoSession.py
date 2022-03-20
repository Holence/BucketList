# # --
from DTPySide import *

class SearchToDoSession(DTFrame.DTMainWindow):
    
    closed=Signal()

    def closeEvent(self, event):
        super().closeEvent(event)
        self.deleteLater()
        self.closed.emit()
    
    def __init__(self, app: DTAPP, Headquarter):
        super().__init__(app)
        self.Headquarter=Headquarter
        self.setMinimumSize(400,500)
        self.initialize()

    def initializeWindow(self):
        super().initializeWindow()
        self.setWindowTitle("Search ToDo")

        from module import SearchToDo
        self.search_ToDo_module=SearchToDo(self, self.Headquarter)
        self.setCentralWidget(self.search_ToDo_module)
        self.search_ToDo_module.lineEdit.setFocus()

        self.resize(self.minimumWidth(),self.minimumHeight())
        self.adjustSize()
        MoveToCenterOfScreen(self)