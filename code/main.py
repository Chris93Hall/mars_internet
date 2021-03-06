"""
main.py

https://zetcode.com/pyqt/qwebengineview/
https://doc.qt.io/qt-5/qtwebengine-webenginewidgets-contentmanipulation-example.html
"""

from PyQt5.QtCore import QUrl, QFile, QIODevice
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QApplication, QVBoxLayout, QMessageBox, QLineEdit, QToolBar, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

import sys
import time

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()
        return

    def init_ui(self):
        self.toolbar = QToolBar(self) 
        self.addToolBar(self.toolbar)

        self.btn_back = QPushButton(self)
        self.btn_back.setEnabled(False)
        self.btn_back.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/left-32.png'))
        self.btn_back.clicked.connect(self.go_back)
        self.toolbar.addWidget(self.btn_back)

        self.btn_forward = QPushButton(self)
        self.btn_forward.setEnabled(False)
        self.btn_forward.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/right-32.png'))
        self.btn_forward.clicked.connect(self.go_forward)
        self.toolbar.addWidget(self.btn_forward)

        self.address = QLineEdit(self)
        self.address.returnPressed.connect(self.load_page)
        self.toolbar.addWidget(self.address) 

        self.btn_cache = QPushButton('Cache', self)
        #self.btn_cache.clicked.connect()
        self.toolbar.addWidget(self.btn_cache)

        self.btn_queue = QPushButton('Queue', self)
        #self.btn_queue.clicked.connect()
        self.toolbar.addWidget(self.btn_queue)

        self.btn_settings = QPushButton('Settings', self)
        #self.btn_settings.clicked.connect()
        self.toolbar.addWidget(self.btn_settings)        

        self.web_engine_view = QWebEngineView()
        self.web_engine_view.setUrl(QUrl('http://www.google.com'))
        self.setCentralWidget(self.web_engine_view)

        self.web_engine_view.page().urlChanged.connect(self.on_load_finished)

        self.web_engine_view.page().titleChanged.connect(self.setWindowTitle)
        self.web_engine_view.page().urlChanged.connect(self.url_changed)
        self.web_engine_view.page().loadFinished.connect(self.content_manip)

        #jquery = QFile(':/jquery.min.js')
        jquery = QFile('/home/chris/research_notes/mars_internet/code/jquery-3.6.0.min.js')
        isopen = jquery.open(QFile.ReadOnly)
        self.jquery_code = bytes(jquery.readAll()).decode('utf-8')
        self.web_engine_view.page().runJavaScript(self.jquery_code)
        jquery.close()

        self.setGeometry(0, 0, 1080, 800)
        self.setWindowTitle('Mars Browser')
        self.show()

    def load_page(self):
        #time.sleep(5)
        url = QUrl.fromUserInput(self.address.text())
        if url.isValid():
            self.web_engine_view.load(url)
        return

    def on_load_finished(self):
        if self.web_engine_view.history().canGoBack():
            self.btn_back.setEnabled(True)
        else:
            self.btn_back.setEnabled(False)

        if self.web_engine_view.history().canGoForward():
            self.btn_forward.setEnabled(True)
        else:
            self.btn_forward.setEnabled(False)

    def go_back(self):
        self.web_engine_view.page().triggerAction(QWebEnginePage.Back)

    def go_forward(self):
        self.web_engine_view.page().triggerAction(QWebEnginePage.Forward)

    def url_changed(self, url):
        self.address.setText(url.toString())

    def content_manip(self):
        self.web_engine_view.page().runJavaScript(self.jquery_code)
        code = "var qt = {'jQuery': jQuery.noConflict(true)};"
        code += "qt.jQuery('a').each(function () {qt.jQuery(this).css('background-color', 'yellow')});"
        code += "qt.jQuery('a').each(function () {qt.jQuery(this).append('(cached)')});"
        self.web_engine_view.page().runJavaScript(code)
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()

