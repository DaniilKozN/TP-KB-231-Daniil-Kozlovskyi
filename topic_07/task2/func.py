class Function:

    def add(self,a, b):                   # Функція в якій відбувається додвання
        a = a + b
        return a,b

    def rem(self,a, b):                   # Функція в якій відбувається віднімання
        a = a - b
        return a,b

    def mult(self,a,b):                   # Функція в якій відбувається множення
        a = a * b
        return a,b
        
    def div(self,a,b):                    # Функція в якій відбуваєтсья ділення                
        try:
            a = a / b
        except ZeroDivisionError:           # Якщо значення b = 0, то буде виняткова ситуація "ZeroDivisionError", тоді буде повідомлення, що операція неможлива
            print(" Помилка, ділення на нуль неможливе")
        return a,b                  # Значення а або не зміниться (якщо b = 0), або буде поділенно на b.
