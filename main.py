from gui.QuirkMailU import Ui_MainWindow
from gui.dialog import Ui_Dialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class QuirkMail(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(QuirkMail, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_4.clicked.connect(self.on_pushButton_clicked)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        dialog = QDialog()
        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()
        dialog.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuirkMail()
    main.show()
    sys.exit(app.exec_())