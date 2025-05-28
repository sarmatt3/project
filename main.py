from pyside6.QtWidgets import QApplication
from design import Ui_MainWindow
import sys
mainWindow = Ui_MainWindow()
class MainWin(Ui_MainWindow):
    self.__init__()
    self.setupUi()

app =QApplication(sys.arg)
win = MainWin()
win.show()