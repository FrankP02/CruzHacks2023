'''
User interface for desktop
'''
import sys
import test
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout)


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
        userQuestion = self.txtBox.text()
        if userQuestion:
            answer = test.get_openai_response(userQuestion)
            self.ans.setText(answer)


# runs the program
app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec())