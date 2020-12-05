from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import MySQLdb
from PyQt5.uic import loadUiType

ui,_ = loadUiType('UI.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.buttons()

    def buttons(self):
        self.usersTabButton.clicked.connect(self.openUsersTab)
        self.booksTabButton.clicked.connect(self.openBooksTab)
        self.AddBookB.clicked.connect(self.test)
        self.DelBookB.clicked.connect(self.test)
        self.DelBookSB.clicked.connect(self.test)

    def test(self):
        print("działa")
    ### tabs
    def openUsersTab(self):
        self.tabWidget.setCurrentIndex(1)

    def openBooksTab(self):
        self.tabWidget.setCurrentIndex(2)

     ### books
    def addBook(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='arek', db='library')
        self.cur = self.db.cursor()

        book_title = self.AddBookTitle.text()
        book_author = self.AddBookAuthor.text()
        status = "available"
    def searchBook(self):
        pass

    def deleteBook(self):
        pass

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()






