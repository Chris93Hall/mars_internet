"""
main.py

https://zetcode.com/pyqt/qwebengineview/
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QApplication, QVBoxLayout, QMessageBox 
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

import sys
import time

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        return

    def init_ui(self):   
        vbox = QVBoxLayout(self)
        hbox = QHBoxLayout()

        self.web_engine_view = QWebEngineView()
        self.web_engine_view.setUrl(QUrl('http://www.google.com'))

        btn1 = QPushButton('Back', self)
        #btn1.clicked.connect(self.function)
        hbox.addWidget(btn1)

        vbox.addWidget(self.web_engine_view)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(0, 0, 1080, 800)
        self.setWindowTitle('Mars Browser')
        self.show()

    def load_page(self, delay=5):
        time.sleep(delay)
        html = '<h1>hello world</h1>'
        self.browser.setHtml(html)
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()

