from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class Registor_(QWidget):
    def __init__(self):
        super().__init__()
        self.V_main_lay = QVBoxLayout()
        
        self.edit_name = QLineEdit()
        self.edit_name.setPlaceholderText("Name")
        self.edit_surname = QLineEdit()
        self.edit_surname.setPlaceholderText("Surname")
        self.edit_tellNumber = QLineEdit()
        self.edit_tellNumber.setPlaceholderText("Tell Number")
        self.edit_username = QLineEdit()
        self.edit_username.setPlaceholderText("Username")
        
        self.btn_ok = QPushButton("OK", clicked = self.OK)
        self.btn_back = QPushButton("Back", clicked = self.Back)
        
        
        self.V_main_lay.addWidget(self.edit_name)
        self.V_main_lay.addWidget(self.edit_surname)
        self.V_main_lay.addWidget(self.edit_tellNumber)
        self.V_main_lay.addWidget(self.edit_username)
        self.V_main_lay.addWidget(self.btn_ok)
        self.V_main_lay.addWidget(self.btn_back)
        
        self.setLayout(self.V_main_lay)
        
        
    def OK(self):
        
        import mysql.connector

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "HAJIME",
            database = "writers",
        )


        crs = mydb.cursor()

        crs.execute(f"""
                    insert into registor(name, surname, tell_number, username) values
                    ('{self.edit_name.text()}', '{self.edit_surname.text()}', {self.edit_tellNumber.text()},'{self.edit_username.text()}' )""")

        mydb.commit()
        print(crs.rowcount)    
        
            
        
        
    def Back(self):
        from main import MyWindow
        self.mywin = MyWindow()
        self.mywin.show()
        self.hide()
        

class Sign_In_(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()
        
        self.edit_username = QLineEdit()
        self.edit_username.setPlaceholderText("Username")
        self.edit_tellnumber = QLineEdit()
        self.edit_tellnumber.setPlaceholderText("Tell Number")
        
        self.btn_ok = QPushButton("OK", clicked = self.OK_)
        self.btn_back = QPushButton("Back", clicked = self.Back_)
        
        self.v_main_lay.addWidget(self.edit_username)
        self.v_main_lay.addWidget(self.edit_tellnumber)
        self.v_main_lay.addWidget(self.btn_ok)
        self.v_main_lay.addWidget(self.btn_back)
        
        self.setLayout(self.v_main_lay)
        
    def OK_(self):
        
        import mysql.connector

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "HAJIME",
            database = "writers",
        )


        mycursor = mydb.cursor()

        mycursor.execute(f"""Select * from registor where {int(self.edit_tellnumber.text())} = tell_number and '{self.edit_username.text()}' = username """)
        res = mycursor.fetchall()
        if res:
            print(True)
            
        #print(mycursor)         
                
        
            
        
            
        
        
    def Back_(self):
        from main import MyWindow
        self.mywin = MyWindow()
        self.mywin.show()
        self.hide()        
        
        
        


        
if __name__ == "__main__":
    app = QApplication([])
    win = Registor_()
    win.show()
    app.exec_()