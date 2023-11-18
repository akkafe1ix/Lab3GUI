import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
import tkinter as tk
from tkinter import filedialog
import numpy as np
import math


# Загрузка интерфейса из файла PostMachine.ui
class Ui(QtWidgets.QMainWindow):
    
    #Инициализация
    def __init__(self):
        
        super(Ui, self).__init__()
        uic.loadUi("GUInterface.ui", self)
        
        #Присвоение кнопкам методов
        self.pushButton.clicked.connect(self.start)
        self.pushButton_clear.clicked.connect(self.Clear_Table)
        
        #Настройка таблицы для вывода и ввода команд
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(("x","f(x)"))
        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,250)

    #Запуск расчёта значений функции
    def start(self):
        if self.lineEdit_a.text() and self.lineEdit_b.text() and self.lineEdit_h.text() and self.lineEdit_m.text() !="":
            a = float(self.lineEdit_a.text())
            b = float(self.lineEdit_b.text())
            h = float(self.lineEdit_h.text())
            m = float(self.lineEdit_m.text())
            rowCount = self.tableWidget.rowCount()
            while(a<=b):
                result=pow(b, 3)-m*math.sin(b)
                self.tableWidget.insertRow(rowCount)
                self.tableWidget.setItem(rowCount,0,QTableWidgetItem(str(b)))
                self.tableWidget.setItem(rowCount,1,QTableWidgetItem(str(result)))
                b=b-h
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Неверно введённые данные!")
        
    #Метод для очистки таблицы
    def Clear_Table(self):
        
        # Очистить содержимое ячеек
        self.tableWidget.clearContents()  
        
        # Установить количество строк в 0
        self.tableWidget.setRowCount(0) 
           
    #Метод для изменения нумерации ячеек    
    def rowsEdit(self):
        for i in range(self.tableWidget.rowCount()):
            item = QTableWidgetItem(str(i))
            self.tableWidget.setVerticalHeaderItem(i, item)
        
#Настройка формы
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())