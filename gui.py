'''
User interface for desktop
'''
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QTextEdit, QLineEdit, 
                                QHBoxLayout, QVBoxLayout, QDialog, QTextBrowser, QComboBox)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.txtBox = QLineEdit(self)
        self.subButton = QPushButton('SUBMIT')
        self.title = QLabel('What can NATE help you with?')
        self.ans = QLabel('')
        vbox = QVBoxLayout()
        vbox.addWidget(self.title)
        vbox.addWidget(self.txtBox)
        vbox.addWidget(self.subButton)
        vbox.addWidget(self.ans)

        self.setLayout(vbox)
        self.subButton.clicked.connect(self.on_click)

    def on_click(self):
        self.ans.setText('woah ur so cool')





# runs the program
app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec())