from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget



class POST12(QWidget):
    def __init__(self):
        super().__init__()
        self.v_main = QVBoxLayout()
        self.p_edit = QLineEdit()
        self.p_edit.setPlaceholderText("enter post...")
        self.push_btn = QPushButton("OK",clicked = self.OK)
        self.exit_btn = QPushButton("BACK",clicked = self.BACK)
        self.h_main = QHBoxLayout()
        self.h_main.addWidget(self.p_edit)
        self.h_main.addWidget(self.push_btn)
        self.v_main.addLayout(self.h_main)
        self.v_main.addWidget(self.exit_btn)
        self.setLayout(self.v_main)


    def OK(self):
        pass

    def BACK(self):
        from post import POST
        self.post = POST()
        self.post.show()
        self.hide()
        

