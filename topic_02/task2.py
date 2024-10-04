def askData():                   # Функція в якій відбувається введення даних користувачем
    a = int(input("Введіть a: ")) # Користувач вводить дані типу int
    b = int(input("Введіть b: "))
    op = input("Введіть операцію [+ - * / ]: ") # Ввід операції
    return a, b, op

def add(a, b):                   # Функція в якій відбувається додвання
    c = a + b
    return c

def rem(a, b):                   # Функція в якій відбувається віднімання
    c = a - b
    return c

def mult(a,b):                   # Функція в якій відбувається множення
    c = a * b
    return c

def div(a,b):                    # Функція в якій відбуваєтсья ділення
    if b == 0:         # Якщо друге значення дорівнює 0 то ділення неможливе
        c = "Операція неможлива"
        return c
    else:
        c = a / b
        return c

a, b, op = askData()             # Значення отримуються з функції

if op == "+":                    # Умовний оператор if-elif-else
    result = add(a, b)
    print(result)
elif op == "-":
    result = rem(a, b)
    print(result)
elif op == "*":
    result = mult(a,b)
    print(result)
elif op == "/":
    result = div(a,b)
    print(result)
else:                          # Виконуються, якщо значення op не відповідає попереднім умовам
    print("Невірно вказано дані")