from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.V_main_lay = QVBoxLayout()
        self.regist = QPushButton("Registor", clicked = self.registor)
        self.sign_in = QPushButton("Sign in", clicked = self.Sign_In)
        
        self.V_main_lay.addWidget(self.regist)
        self.V_main_lay.addWidget(self.sign_in)
        self.setLayout(self.V_main_lay)
        
    
    def registor(self):
        from Registor import Registor_
        self.hide()
        self.regist = Registor_()
        self.regist.show()
    
    def Sign_In(self):
        from Registor import Sign_In_
        self.hide()
        self.signin = Sign_In_()
        self.signin.show()
        



        
if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()
