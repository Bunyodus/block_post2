import datetime
import mysql.connector
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QListWidget, QListWidgetItem,
    QLabel, QLineEdit, QFrame
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class TwitterPost_(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Post Page")
        self.resize(500, 700)

       
        self.db = mysql.connector.connect(
            host="localhost", 
            user="root",      
            password="thisismysql",  
            database="twitter_clone"
        )
        self.cursor = self.db.cursor()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.new_post_frame = QFrame()
        self.new_post_layout = QVBoxLayout()
        self.new_post_frame.setLayout(self.new_post_layout)
        self.layout.addWidget(self.new_post_frame)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")
        self.new_post_layout.addWidget(self.username_input)

        self.new_post_text = QTextEdit()
        self.new_post_text.setPlaceholderText("What's happening?")
        self.new_post_text.setFixedHeight(100)
        self.new_post_layout.addWidget(self.new_post_text)

        self.post_button = QPushButton("Post")
        self.post_button.clicked.connect(self.add_post)
        self.new_post_layout.addWidget(self.post_button)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        self.layout.addWidget(separator)

        self.posts_list = QListWidget()
        self.layout.addWidget(self.posts_list)

        self.apply_styles()

        self.load_posts()

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                font-family: Arial, sans-serif;
            }
            QLineEdit, QTextEdit {
                border: 1px solid #ccd0d5;
                border-radius: 15px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #1DA1F2;
                color: white;
                font-weight: bold;
                padding: 10px;
                border: none;
                border-radius: 15px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0d8ddc;
            }
            QListWidget {
                border: none;
            }
            QLabel {
                font-size: 14px;
            }
        """)

    def add_post(self):
        username = self.username_input.text().strip()
        post_content = self.new_post_text.toPlainText().strip()
        timestamp = datetime.datetime.now()

        if username and post_content:
          
            sql = "INSERT INTO posts (username, content, timestamp) VALUES (%s, %s, %s)"
            values = (username, post_content, timestamp)
            self.cursor.execute(sql, values)
            self.db.commit()

            
            self.display_post(username, post_content, timestamp)

      
            self.new_post_text.clear()

    def display_post(self, username, post_content, timestamp):
        post_widget = QWidget()
        post_layout = QVBoxLayout()
        post_widget.setLayout(post_layout)
        post_widget.setStyleSheet("background-color: #f5f8fa; padding: 10px; border-bottom: 1px solid #e1e8ed;")

        header_layout = QHBoxLayout()
        profile_pic = QLabel()
        profile_pic.setPixmap(QPixmap('default_profile.png').scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        profile_pic.setStyleSheet("border-radius: 20px;")
        header_layout.addWidget(profile_pic)

        user_info_layout = QVBoxLayout()
        username_label = QLabel(f"<b>{username}</b>")
        username_label.setStyleSheet("font-size: 16px;")
        timestamp_label = QLabel(timestamp.strftime("%I:%M %p · %b %d, %Y"))
        timestamp_label.setStyleSheet("color: gray; font-size: 12px;")
        user_info_layout.addWidget(username_label)
        user_info_layout.addWidget(timestamp_label)
        header_layout.addLayout(user_info_layout)
        header_layout.addStretch()
        post_layout.addLayout(header_layout)

        content_label = QLabel(post_content)
        content_label.setWordWrap(True)
        content_label.setStyleSheet("font-size: 14px;")
        post_layout.addWidget(content_label)

        item = QListWidgetItem()
        item.setSizeHint(post_widget.sizeHint())
        self.posts_list.addItem(item)
        self.posts_list.setItemWidget(item, post_widget)

    def load_posts(self):
       
        self.cursor.execute("SELECT username, content, timestamp FROM posts ORDER BY timestamp DESC")
        posts = self.cursor.fetchall()

        for post in posts:
            username, content, timestamp = post
            self.display_post(username, content, timestamp)


app = QApplication([])
window = TwitterPost_()
window.show()
app.exec_()


