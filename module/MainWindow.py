from DTPySide import *
from session.MainSession import MainSession
from widget.Block import Block

class Separator(DTWidget.DTLine):
    def __init__(self, parent, shape: QFrame.Shape = QFrame.HLine, shadow: QFrame.Shadow = QFrame.Sunken) -> None:
        super().__init__(parent, shape, shadow)
        self.setStyleSheet("margin-right: 12px;")

from module.Ui_MainWindow import Ui_MainWindow
class MainWindow(Ui_MainWindow,QWidget):
    def __init__(self, Headquarter:MainSession) -> None:
        super().__init__(Headquarter)
        self.setupUi(self)
        self.Headquarter=Headquarter
        self.bar_tag_list=[]
        self.current_index=0
        self.adding_tab=False
        self.current_tag=""

        self.initialize()
    
    def initialize(self):
        self.initializeSignal()
        self.initializeWindow()
    
    def initializeWindow(self, refresh=False):
        # 初始化
        if refresh==False:
            self.scrollArea.setContentsMargins(QMargins(0,0,0,0))
            self.scrollAreaWidgetContents.setContentsMargins(QMargins(0,0,0,0))
            self.VLayout=QVBoxLayout()
            self.VLayout.setMargin(0)
            self.scrollAreaWidgetContents.setLayout(self.VLayout)

        color=self.Headquarter.app.color_list[0]
        
        self.frame.setStyleSheet(f"QFrame #frame {{ border-top: 6px solid {color};}};")

        self.tabWidget.setStyleSheet(f"""
            QTabBar::tab {{
                font-size: 16pt;
                min-height: 40px;
                min-width: 40px;
            }};
        """)
        self.checkBoxsGroup.setStyleSheet(f"#checkBoxsGroup {{ border-top: 5px ridge {color};}}")
        
        self.refresh()

    def initializeSignal(self):
        
        self.actionAdd_ToDo.triggered.connect(self.addToDo)
        self.actionAdd_ToDo.setIcon(IconFromCurrentTheme("plus.svg"))

        self.tabWidget.currentChanged.connect(self.refreshPage)
        self.tabWidget.tabBarDoubleClicked.connect(self.changeTagName)

        self.actionExport_to_Json.triggered.connect(self.ExportToJson)
        self.actionExport_to_Json.setIcon(IconFromCurrentTheme("upload-cloud.svg"))

        self.actionCheck_Data_Completeness.triggered.connect(self.checkDataCompleteness)
        self.actionCheck_Data_Completeness.setIcon(IconFromCurrentTheme("shield.svg"))
    
    def addToDo(self):
        dlg=DTFrame.DTDialog(self,"Add ToDo")
        
        from module.ContentEdit import ContentEdit
        widget=ContentEdit(self.Headquarter)
        widget.pushButton_delete.hide()

        current_page_tag=self.bar_tag_list[self.tabWidget.currentIndex()]
        if current_page_tag!="📃":
            widget.lineEdit_tags.setText(current_page_tag)
        
        true_list=[index for index, status in enumerate(self.Headquarter.status_list) if status == True]
        if len(true_list)>=1:
            selected_status=self.Headquarter.status_type[true_list[0]]
            if selected_status in ["🚄","☕","⌚","❌"]:
                widget.comboBox_status.setCurrentIndex(["🚄","☕","⌚","❌"].index(selected_status))
            elif selected_status=="✔":
                widget.checkBox.setChecked(True)
        
        dlg.setCentralWidget(widget)
        dlg.adjustSize()
        MoveToCenterOfScreen(dlg)

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
            self.Headquarter.appendData(tags,text,status,date_add,date_fin)
        
            self.refresh()
    
    def refresh(self):
        self.refreshTabBar()
        self.refreshPage()
    
    def refreshTabBar(self):
        # 根据data，生成tab
        
        self.bar_tag_list=[]
        for content in self.Headquarter.getData():
            tags=content["tags"]
            for tag in tags:
                if tag not in self.bar_tag_list and tag!="🏠":
                    self.bar_tag_list.append(tag)
        self.bar_tag_list.sort()
        self.bar_tag_list.insert(0,"🏠")
        self.bar_tag_list.append("📃")
        
        # tabWidget.clear()的时候会触发currentChanged，导致许多不必要的refreshPage，这里设置一个阀门
        ##################################
        self.adding_tab=True

        self.tabWidget.clear()
        for tag in self.bar_tag_list:
            self.tabWidget.addTab(QWidget(),tag)
        
        self.tabWidget.setCurrentIndex(self.current_index) # 同理，这里即使触发了currentChanged，也不会进行refreshPage

        self.adding_tab=False
        ##################################
    
    def refreshPage(self,index=None):
        if self.adding_tab==True:
            return
        
        # 刷新当前的tab
        if index!=None:
            self.current_index=index
        
        if self.current_index!=-1:
            while True:
                try:
                    self.current_tag=self.bar_tag_list[self.current_index]
                    break
                except:
                    self.current_index=self.current_index-1
                    self.tabWidget.setCurrentIndex(self.current_index)
                    continue

        content_splitted_by_status_list=[[],[],[],[],[]]

        data=self.Headquarter.getData()
        for i in range(len(data)):
            content=data[i]
            if self.current_tag!="📃":
                if self.current_tag in content["tags"]:
                    content_splitted_by_status_list[self.Headquarter.status_type.index(content["status"])].append(i)
            else:
                content_splitted_by_status_list[self.Headquarter.status_type.index(content["status"])].append(i)

        self.total=0
        self.checkBox_list=[]
        Clear_Layout(self.checkBoxLayout)
        for i in range(len(content_splitted_by_status_list)):

            old_check=self.Headquarter.status_list[i]
            if content_splitted_by_status_list[i]!=[]:

                self.total+=len(content_splitted_by_status_list[i])

                status=self.Headquarter.status_type[i]
                
                checkbox=QCheckBox(status+" %s"%len(content_splitted_by_status_list[i]))
                if old_check==True or old_check==None:
                    checkbox.setChecked(True)
                elif old_check==False:
                    checkbox.setChecked(False)
                
                checkbox.stateChanged.connect(self.refresh_list)
                self.checkBox_list.append((checkbox,status))
                self.checkBoxLayout.addWidget(self.checkBox_list[-1][0])
            else:
                if old_check==True or old_check==None:
                    self.Headquarter.status_list[i]=None
                # elif old_check==False:
                #     self.Headquarter.status_list[i]=False
        
        self.checkBoxLayout.addStretch(100)
        
        self.total_label=QLabel()
        self.total_label.setStyleSheet("font-size: 11pt;")
        self.total_label.setAlignment(Qt.AlignRight)
        self.checkBoxLayout.addWidget(self.total_label)

        self.refresh_list()
    
    def refresh_list(self):

        def sort_by_date(index_list):
            
            date_type,reverse=[("date_add",False),("date_add",True),("date_fin",False),("date_fin",True)][self.Headquarter.sorting_type-1]
            
            data=self.Headquarter.getData()
            sorted_list=[]
            
            #
            if date_type=="date_add":
                for index in index_list:
                    content=data[index]
                    date_add=content[date_type]
                    sorted_list.append((date_add,index))
                sorted_list.sort(reverse=reverse)
                index_list=[i[1] for i in sorted_list]
            else:
                # 未完成的date_fin为None，没法比较，所以挑出来放在最后
                not_finish=[]
                for index in index_list:
                    content=data[index]
                    date_fin=content[date_type]
                    if date_fin!=None:
                        sorted_list.append((date_fin,index))
                    else:
                        not_finish.append(index)
                sorted_list.sort(reverse=reverse)
                index_list=[i[1] for i in sorted_list]
                index_list.extend(not_finish)

            return index_list

        selected_status_list=[]
        for (checkbox,status) in self.checkBox_list:
            if checkbox.checkState()==Qt.Checked:
                selected_status_list.append(status)
                self.Headquarter.status_list[self.Headquarter.status_type.index(status)]=True
            else:
                self.Headquarter.status_list[self.Headquarter.status_type.index(status)]=False
        
        # 开始
        content_list=[]
        # 如果status分裂开
        if self.Headquarter.seperate_status:

            content_splitted_by_status_list=[[],[],[],[],[]]

            data=self.Headquarter.getData()
            for i in range(len(data)):
                content=data[i]
                if self.current_tag!="📃":
                    if self.current_tag in content["tags"] and content["status"] in selected_status_list:
                        content_splitted_by_status_list[self.Headquarter.status_type.index(content["status"])].append(i)
                else:
                    if content["status"] in selected_status_list:
                        content_splitted_by_status_list[self.Headquarter.status_type.index(content["status"])].append(i)
            
            for content_splitted_by_status in content_splitted_by_status_list:
                if content_splitted_by_status!=[]:
                    
                    # 如果要按照时间排序
                    if self.Headquarter.sorting_type!=None:
                        content_list.extend(sort_by_date(content_splitted_by_status))
                    else:
                        content_list.extend(content_splitted_by_status)

        else:
            
            data=self.Headquarter.getData()
            for i in range(len(data)):
                content=data[i]
                if self.current_tag!="📃":
                    if self.current_tag in content["tags"] and content["status"] in selected_status_list:
                        content_list.append(i)
                else:
                    if content["status"] in selected_status_list:
                        content_list.append(i)
            
            if self.Headquarter.sorting_type!=None:
                content_list=sort_by_date(content_list)
            else:
                pass
        
        # 最后
        Clear_Layout(self.VLayout)
        head=True
        for i in content_list:
            if head==True:
                head=False
            else:
                self.VLayout.addWidget(Separator(self))
            self.VLayout.addWidget(Block(self.Headquarter,i))
        
        self.VLayout.addStretch(100)

        self.total_label.setText("Total: %s/%s"%(len(content_list),self.total))

    def changeTagName(self,index):
        current_tag=self.bar_tag_list[index]

        if current_tag=="📃":
            return
        
        dlg=DTFrame.DTDialog(self,"Move to Other Tag")

        label=QLabel("Move the ToDos under current tag to...")
        
        from widget.SuggestLineEdit import SuggestLineEdit
        lineedit=SuggestLineEdit(None)
        lineedit.setHeadquarter(self.Headquarter)

        label_note=QLabel("If contains current tag, the operation will be like adding other tags to these ToDos :)")
        label_note.setStyleSheet("font-size: 10pt;")
        
        layout=QVBoxLayout()
        layout.setMargin(0)
        layout.addWidget(label)
        layout.addWidget(lineedit)
        layout.addWidget(label_note)
        widget=QWidget()
        widget.setLayout(layout)

        dlg.setCentralWidget(widget)
        dlg.adjustSize()
        MoveToCenterOfScreen(dlg)

        if dlg.exec_():
            tags=self.Headquarter.ConvertToTagList(lineedit.text(),add_home=False)
            if tags==[]:
                confirm=DTFrame.DTConfirmBox(self,"Warning","Tags are empty!\n\nDo you want to move them into 🏠?",DTIcon.Warning())
                if confirm.exec_():
                    tags=["🏠"]
                else:
                    return
            
            for content in self.Headquarter.getData():
                if current_tag in content["tags"]:
                    content["tags"].remove(current_tag)
                    content["tags"].extend(tags)
            
            self.refresh()
    
    def ExportToJson(self):
        url=os.path.abspath("./Export_Data_%s.json"%WhatDayIsToday(1).toString("yyyyMMdd"))
        res=Json_Save(self.Headquarter.data,url)
        if res==True:
            self.Headquarter.app.showMessage("Information", "Data Export Successfully!", DTIcon.Information(), clicked_slot=lambda:os.popen("explorer /select,\"%s\""%url))
        else:
            self.Headquarter.app.showMessage("Error","Error occured during Data Export!",DTIcon.Error())
    
    def checkDataCompleteness(self):

        def check():
            data=self.Headquarter.getData()

            error="Check Started: %s\n\n"%QLocale().toString(QDateTime().currentDateTime(),"yyyy.M.d hh:mm:ss")
            
            if type(data)!=list:
                error+="type(data)!=list\n"
            else:
                for i in range(len(data)):
                    content=data[i]
                    if type(content)!=dict:
                        error+="type(content)!=dict\n"
                    else:
                        try:
                            if type(content["tags"])!=list:
                                error+="index %s tags is not list\n%s\n\n"%(i,content["tags"])
                            else:
                                for tag in content["tags"]:
                                    if type(tag)!=str:
                                        error+="index %s tag %s is not str\n%s\n\n"%(i,tag)

                            if type(content["text"])!=str:
                                error+="index %s text is not str\n%s\n\n"%(i,content["text"])
                            
                            if type(content["status"])!=str:
                                error+="index %s status is not str\n%s\n\n"%(i,content["status"])
                            else:
                                if content["status"] not in self.Headquarter.status_type:
                                    error+="index %s status is not valid\n%s\n\n"%(i,content["status"])
                            
                            if type(content["date_add"])!=str:
                                error+="index %s date_add is not str\n%s\n\n"%(i,content["date_add"])
                            else:
                                if not QDate.fromString(content["date_add"],"yyyy.M.d").isValid():
                                    error+="index %s date_add is not valid\n%s\n\n"%(i,content["date_add"])
                            
                            if content["date_fin"]!=None:
                                if type(content["date_fin"])!=str:
                                    error+="index %s date_fin is not str\n%s\n\n"%(i,content["date_fin"])
                                else:
                                    if not QDate.fromString(content["date_fin"],"yyyy.M.d").isValid():
                                        error+="index %s date_fin is not valid\n%s\n\n"%(i,content["date_fin"])
                            else:
                                if content["status"]=="✔":
                                    error+="index %s date_fin is not None but status is ✔\n%s\n\n"%(i,content["date_fin"])
                            
                        except Exception as e:
                            error+="%s \n"%(content,e)
            
            error+="\n\nCheck Finished: %s"%QLocale().toString(QDateTime().currentDateTime(),"yyyy.M.d hh:mm:ss")
            return error
        
        def slot():
            self.DataChecker.deleteLater()
            del self.DataChecker
        
        error=check()
        
        try:
            self.DataChecker.errorText.setPlainText(error)
        except:
            self.DataChecker=DTFrame.DTMainWindow(self.Headquarter.app)
            self.DataChecker.initialize()
            self.DataChecker.setWindowTitle("Check Data Completeness")

            self.DataChecker.actionExit.triggered.disconnect(self.DataChecker.close)
            self.DataChecker.actionExit.triggered.connect(slot)
            self.DataChecker.TitleBar.btn_close.clicked.disconnect(self.DataChecker.close)
            self.DataChecker.TitleBar.btn_close.clicked.connect(slot)

            self.DataChecker.errorText=QPlainTextEdit(error)
            self.DataChecker.errorText.setReadOnly(True)
            self.DataChecker.setMinimumSize(500,500)
            self.DataChecker.setCentralWidget(self.DataChecker.errorText)
            self.DataChecker.adjustSize()
            MoveToCenterOfScreen(self.DataChecker)
            self.DataChecker.show()
        
        self.DataChecker.showNormal()
        self.DataChecker.raise_()