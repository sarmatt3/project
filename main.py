from register import *
app = QApplication(sys.argv)
win = QMainWindow()
    
ui = Ui_MainWindow()
ui.setupUi(win)  # Настройка интерфейса

win.show()  # Отображение окна

sys.exit(app.exec())