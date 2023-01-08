from DTPySide import *
from session.MainSession import MainSession

app=DTAPP(sys.argv)

app.setWindowIcon(DTIcon.HoloIcon2())
app.setApplicationName("Bucket List")
app.setApplicationVersion("1.0.0.5 build with DTPySide %s"%importlib.metadata.version('DTPySide'))
app.setAuthor("鍵山狐")
app.setLoginEnable(True)

app.setDataList(["data.dlcw"])
app.setBackupEnable(True)

mainsession=MainSession(app)
app.setMainSession(mainsession)

# app.debugRun("123",True)
app.run()