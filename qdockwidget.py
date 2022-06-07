#!/usr/bin/python3.9
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
class WindowDocker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Manager")
        bar=self.menuBar()
        file=bar.addMenu('File')
        file.addAction('New')
        file.addAction('Save')
        file.addAction('quit')
        edit=bar.addMenu('Edit')
        edit.addAction('Copy')
        edit.addAction('Paste')
        help=bar.addMenu('Help')
        help.addAction('Contact')
        self.dock=QDockWidget('Docker', self)
        self.label=QLabel('PYTHON FOR QGIS')
        self.dock.setWidget(self.label)
        self.dock.setFloating(False)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

        #another dock

        self.dock2=QDockWidget('ITEMS', self)
        self.listWidget=QListWidget()
        self.listWidget.addItem('Item1')
        self.listWidget.addItem('Item2')
        self.listWidget.addItem('Item3')
        self.listWidget.addItem('Item4')

        self.dock2.setWidget(self.listWidget)
        self.dock2.setFloating(False)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock2)
        self.listWidget.itemClicked.connect(clicked)
def clicked(self):
    #item=self.listWidget.currentItem()
    #if item is not None:
        print("you have clicked an item")

        


app= QApplication(sys.argv)
window= WindowDocker()
window.show()
sys.exit(app.exec())
