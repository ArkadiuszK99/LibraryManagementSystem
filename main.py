from PyQt5 import QtWidgets, QtGui, QtCore, uic
__all__ = [QtWidgets, QtGui, QtCore, uic]
import sys
import MySQLdb

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('UI.ui', self)
        self.buttons()
        self.show()

    def buttons(self):
        self.usersTabButton.clicked.connect(self.openUsersTab)
        self.booksTabButton.clicked.connect(self.openBooksTab)
        self.AddBookB.clicked.connect(self.addBook)
        self.DelBookB.clicked.connect(self.test)
        self.DelBookSB.clicked.connect(self.test)

    def test(self):
        print("works")
    ### tabs
    def openUsersTab(self):
        self.tabWidget.setCurrentIndex(1)

    def openBooksTab(self):
        self.tabWidget.setCurrentIndex(2)

    ### books
    def addBook(self):
        self.db = MySQLdb.connect(host='localhost', user='arek', password ='', db='library')
        self.cur = self.db.cursor()
        book_title = self.AddBookTitle.text()
        book_author = self.AddBookAuthor.text()
        status = "available"
        self.cur.execute('''
                    INSERT INTO books(book_title,book_author,status) VALUES (%s , %s , %s)
                ''', (book_title, book_author, status))
        self.db.commit()
        print('New Book Added')
        self.AddBookTitle.setText('')
        self.AddBookAuthor.setText('')
        self.statusBar().showMessage('New Book Added')

    def searchBook(self):
        pass

    def deleteBook(self):
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()

if __name__ == '__main__':
    main()






