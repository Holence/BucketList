from DTPySide import *

class MainSession(DTSession.DTMainSession):
    def __init__(self, app):
        super().__init__(app)

        self.status_type=["🚄","☕","⌚","✔","❌"]
        self.status_list=[True,True,True,True,True]
        self.sorting_type=2
        self.seperate_status=True

    def initializeWindow(self):
        super().initializeWindow()

        from module.MainWindow import MainWindow
        self.mainwindow=MainWindow(self)
        self.setCentralWidget(self.mainwindow)
        self.setMinimumSize(500,400)

    def initializeSignal(self):
        super().initializeSignal()
        self.addAction(self.mainwindow.actionAdd_ToDo)
        self.addAction(self.mainwindow.actionExport_to_Json)
        self.addAction(self.mainwindow.actionCheck_Data_Completeness)
        self.addAction(self.mainwindow.actionSearch_ToDo)
        
        self.actionSort_list=[
            QAction("Seperate by Status",checkable=True),
            QAction("Ascending Sort by Date Added",checkable=True),
            QAction("Descending Sort by Date Added",checkable=True),
            QAction("Ascending Sort by Date Finished",checkable=True),
            QAction("Descending Sort by Date Finished",checkable=True),
        ]
        
        def slot(index):
            if index==0:
                self.seperate_status=self.actionSort_list[0].isChecked()
            else:
                if self.actionSort_list[index].isChecked():
                    self.sorting_type=index
                    for i in range(1,5):
                        if i!=self.sorting_type:
                            self.actionSort_list[i].setChecked(False)
                else:
                    self.sorting_type=None

            self.mainwindow.refreshPage()
            
        self.actionSort_list[0].triggered.connect(lambda:slot(0))
        self.actionSort_list[0].setIcon(IconFromCurrentTheme("align-left.svg"))
        self.actionSort_list[0].setChecked(True)
        self.seperate_status=True

        self.actionSort_list[1].triggered.connect(lambda:slot(1))
        self.actionSort_list[1].setIcon(IconFromCurrentTheme("chevrons-up.svg"))

        self.actionSort_list[2].triggered.connect(lambda:slot(2))
        self.actionSort_list[2].setIcon(IconFromCurrentTheme("chevrons-down.svg"))
        self.actionSort_list[2].setChecked(True)
        self.sorting_type=2

        self.actionSort_list[3].triggered.connect(lambda:slot(3))
        self.actionSort_list[3].setIcon(IconFromCurrentTheme("chevrons-up.svg"))
        
        self.actionSort_list[4].triggered.connect(lambda:slot(4))
        self.actionSort_list[4].setIcon(IconFromCurrentTheme("chevrons-down.svg"))

    
    def initializeMenu(self):
        self.addActionToMainMenu(self.mainwindow.actionAdd_ToDo)
        self.addActionToMainMenu(self.mainwindow.actionSearch_ToDo)

        self.menuSort=QMenu("Sort")
        self.menuSort.setIcon(IconFromCurrentTheme("bar-chart-2.svg"))
        self.menuSort.addActions(self.actionSort_list)
        self.addMenuToMainMenu(self.menuSort)

        self.menuData=QMenu("Data")
        self.menuData.setIcon(IconFromCurrentTheme("database.svg"))
        self.menuData.addAction(self.mainwindow.actionCheck_Data_Completeness)
        self.menuData.addAction(self.mainwindow.actionExport_to_Json)
        self.addMenuToMainMenu(self.menuData)

        super().initializeMenu()
    
    def loadData(self):
        
        data_dir=os.path.join(self.app.DataDir(),"data.dlcw")
        if os.path.exists(data_dir):
            self.data=Symmetric_Decrypt_Load(self.password(), data_dir, iteration=self.iteration())
            if self.data==False:
                DTFrame.DTMessageBox(self,"Error","Data error!")
                self.app.quit()
        else:
            self.data=[]
            Symmetric_Encrypt_Save(self.password(), self.data, data_dir, iteration=self.iteration())
    
    def saveData(self):
        try:
            data_dir=os.path.join(self.app.DataDir(),"data.dlcw")
            Symmetric_Encrypt_Save(self.password(), self.data, data_dir, iteration=self.iteration())
        except Exception as e:
            self.app.showMessage("Error","Error occured during Data Saving!\n\n%s"%e,DTIcon.Error())
    
    def saveAllEncryptData(self):
        super().saveAllEncryptData()
        self.saveData()
	
    def refresh(self):
        self.mainwindow.initializeWindow(refresh=True)
    
    def getData(self):
        return self.data
    
    def appendData(self,tags:list,text,status,date_add:QDate,date_fin:QDate):
        date_add=date_add.toString("yyyy.MM.dd")

        if status=="✔":
            date_fin=date_fin.toString("yyyy.MM.dd")
        else:
            date_fin=None
        
        self.data.append({
            "tags": tags,
            "text": text,
            "status": status,
            "date_add": date_add,
            "date_fin": date_fin
        })
    
    def editData(self,index,tags:list,text,status,date_add:QDate,date_fin:QDate):
        date_add=date_add.toString("yyyy.MM.dd")
        
        if status=="✔":
            date_fin=date_fin.toString("yyyy.MM.dd")
        else:
            date_fin=None
        
        self.data[index]={
            "tags": tags,
            "text": text,
            "status": status,
            "date_add": date_add,
            "date_fin": date_fin
        }
    
    def deleteData(self,index):
        self.data.pop(index)
    
    def ConvertToTagList(self,tags_text,add_home=True):

        tags_text=re.sub("^[, ]*","",tags_text)
        tags_text=re.sub("[, ]*$","",tags_text)
        tags=[i.strip() for i in tags_text.split(",") if i.strip()!=""]

        # 去重
        unique_tags=[]
        for i in tags:
            if i not in unique_tags:
                unique_tags.append(i)
        
        if "📃" in unique_tags:
            DTFrame.DTMessageBox(self,"Warning","📃 is a reserved word, it will be removed from the tag list!",DTIcon.Warning())
            unique_tags.remove("📃")
        
        if add_home==True:
            # 如果tag为空，自动加到🏠中
            if unique_tags==[]:
                unique_tags=["🏠"]
        
        return unique_tags