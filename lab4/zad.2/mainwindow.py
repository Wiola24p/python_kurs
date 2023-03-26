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
        
    
    def initializeMenu(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("File")
        newAction =fileMenu.addAction("New")
        openAction =fileMenu.addAction("Open")
        saveAction = fileMenu.addAction("Save")
        saveAsAction = fileMenu.addAction("Save as")
        newAction.triggered.connect(self.OnNewAction)
        openAction.triggered.connect(self.OnOpenAction)

    def OnNewAction(self):
        self.edit.clear()


    def OnOpenAction(self):
        path,_ = QFileDialog.getOpenFileName(self,"Open file", "")
        if len(path) > 0:
           file = open(path,"r")
           data = file.read()
           self.edit.setText(data)
        
