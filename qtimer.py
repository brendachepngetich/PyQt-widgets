from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtWidgets import *
import sys

class WindowTimer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTimer")
        layout=QGridLayout()
        self.startbtn=QPushButton("Start")
        self.endbtn=QPushButton("Stop")
        self.label=QLabel('date today')
        layout.addWidget(self.startbtn)
        layout.addWidget(self.endbtn)
        layout.addWidget(self.label)
        self.tmr=QTimer()
        self.tmr.timeout.connect(self.show_time)
        self.setLayout(layout)
        self.startbtn.clicked.connect(self.start_timer)
        self.endbtn.clicked.connect(self.end_timer)
    def show_time(self):
        time=QDateTime.currentDateTime()
        display=time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.label.setText(display)
    def start_timer(self):
        self.tmr.start(1000)
        self.startbtn.setEnabled(False)
        self.endbtn.setEnabled(True)
    def end_timer(self):
        self.tmr.stop()
        self.startbtn.setEnabled(True)
        self.endbtn.setEnabled(False)

app=QApplication(sys.argv)
window=WindowTimer()
window.show()

sys.exit(app.exec())