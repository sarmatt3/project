from register2 import *
from tkinter import filedialog
class Main(Ui_MainWindow):
    def __init__(self):
        self.baseList = []
        self.click()
    def getInfo(self):
        self.baseList += [self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_4.text()]
        h = hash(tuple(self.baseList[1]))
        self.baseList[1] = h
        
        file = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        
        if file != "":
           
            with open(file, "a", encoding='utf-8') as f:
                f.write(f'{h}\n')
                f.close()
        print(h)
    def click(self):
        self.pushButton.clicked.connect(self.getInfo)
app = QApplication(sys.argv)
win = QMainWindow()  
ui = Ui_MainWindow()
ui.setupUi(win)  # Настройка интерфейса
win.show()  # Отображение окна
sys.exit(app.exec())