from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from post1 import POST12

class POST(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(220,200)
        self.v_main = QHBoxLayout()
        self.push_bnt = QPushButton("CREATE POST",clicked = self.create)
        self.exi_bnt = QPushButton("BACK",clicked = self.hide)
        self.push_bnt.clicked.connect
        self.v_main.addWidget(self.push_bnt)
        self.v_main.addWidget(self.exi_bnt)
        self.setLayout(self.v_main)
    
    def create(self):
        self.hide()
        self.wing = POST12()
        self.wing.show()

if __name__=='__main__':
    app = QApplication([])
    win = POST()
    win.show()
    app.exec_()