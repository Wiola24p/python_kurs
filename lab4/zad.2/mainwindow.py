from PySide2.QtWidgets import *

class QTekstEdit:
    pass

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main widget")
        self.initializeMenu()

        self.edit = QTextEdit(self)
        self.setCentralWidget(self.edit)
        self.path=""
        
    
    def initializeMenu(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("File")
        newAction =fileMenu.addAction("New")
        openAction =fileMenu.addAction("Open")
        saveAction = fileMenu.addAction("Save")
        saveAsAction = fileMenu.addAction("Save as")
        newAction.triggered.connect(self.OnNewAction)
        openAction.triggered.connect(self.OnOpenAction)
        saveAsAction.triggered.connect(self.onSaveAsAction)
        saveAction.triggered.connect(self.onSaveAsAction)

    def OnNewAction(self):
        self.edit.clear()
        self.path =""


    def OnOpenAction(self):
        path,_ = QFileDialog.getOpenFileName(self,"Open file", "")
        if len(path) > 0:
           self.path = path
           file = open(path,"r")
           data = file.read()
           self.edit.setText(data)


    def onSaveAsAction(self):
        path = QFileDialog.getSaveFilename(self,"Save file")
        if len(path) > 0:
            self.save(path)

    def onSaveAction(self):
        if self.path == "":
            self.onSaveAsAction()

        else:
            self.save(self.path)

    def save(self):
        file = open(path, "w")
        data = self.edit.toPlainText()
        file.write(data)
        file.close()
        self.path = path

