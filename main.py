from DTPySide import *
from session.MainSession import MainSession

app=DTAPP(sys.argv)

app.setWindowIcon(DTIcon.HoloIcon2())
app.setApplicationName("Bucket List")
app.setApplicationVersion("1.0.0.3 build with DTPySide 0.1.4")
app.setAuthor("鍵山狐")
app.setLoginEnable(True)

app.setDataList(["data.dlcw"])
app.setBackupEnable(True)

mainsession=MainSession(app)
app.setMainSession(mainsession)

# app.debugRun("123",True)
app.run()