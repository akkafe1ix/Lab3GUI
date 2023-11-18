import numpy as np
import math

#Вывод информации
print ("Функция:")
print ("F(x)=x^3-m*sin(x)")

#Метод для счёта всех значений функции
def FirstFunction(a,b,h,m):
    count=0
    print("№       x        f(x)")
    while(a<=b):
        count=count+1
        result=pow(a, 3)-m*math.sin(a)
        print(str(count)+"     "+str(a)+"     "+str(result))
        a=a+h

#Ввод параметров
a=float(input("Введите a: "))
b=float(input("Введите b: "))
h=float(input("Введите h: "))
m=float(input("Введите m: "))
FirstFunction(a,b,h,m)
        
        
        
        