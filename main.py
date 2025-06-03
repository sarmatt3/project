from register2 import *
from PySide6.QtWidgets import QApplication, QMainWindow  
from PySide6.QtCore import QFile 
from tkinter import filedialog
from tkinter.messagebox import showerror
import sys

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Настройка интерфейса
        self.baseList = []
        self.pushButton.clicked.connect(self.getInfo)
        
    def getInfo(self):
        check =  [0,0,0,0]
        
        if self.lineEdit_2.text() != self.lineEdit_3.text():
            showerror('Ошибка', "Пароли не совпадают")
            return
        for i in self.lineEdit_2.text():
            if i in '123456789': check[0] += 1
            elif i in 'qwertyuiopasdfghjklzxcvbnm': check[1] += 1
            elif i in 'QWERTYUIOPASDFGHJKLZXCVBNM': check[2] += 1
            elif i in '!.*@%&#?': check[3] += 1
        if not(check[0] >=1 and check[1] >=1 and check[2] >=1 and check[3] >=1 and len(self.lineEdit_2.text())>=8):
            showerror('Ошибка', "Пароль не надежный")
        elif self.lineEdit.text() == '' or self.lineEdit_2.text() == '' or self.lineEdit_3.text() == '' or self.lineEdit_4.text() == '':
            showerror('Ошибка', "Заполните все поля")
        else:
            self.baseList = [self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_4.text()]
            h = hash(tuple(self.baseList[1]))
            self.baseList[1] = h
            
            file = filedialog.asksaveasfilename(
                defaultextension='.txt', 
                filetypes=[('Text files', '*.txt'), ('All files', '*.*')]
            )
            
            if file:
                with open(file, "a", encoding='utf-8') as f:
                    f.write(f'login - {self.baseList[0]}: password - {h}: phoneNumber - {self.baseList[2]}\n')
            print(h)
        
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()  # Создаем экземпляр нашего главного окна
    win.show()  # Отображение окна
    sys.exit(app.exec())  # Запуск главного цикла приложения