def askData():                   # Функція в якій відбувається введення даних користувачем
    a = float(input("Введіть a: ")) # Користувач вводить дані типу float, щоб використувати в операціях не цілі числа
    return a

def add(a, b):                   # Функція в якій відбувається додвання
    a = a + b
    return a

def rem(a, b):                   # Функція в якій відбувається віднімання
    a = a - b
    return a

def mult(a,b):                   # Функція в якій відбувається множення
    a = a * b
    return a

def div(a,b):                    # Функція в якій відбуваєтсья ділення                
    a = a / b
    return a

def calc(a):  # Функція в якій відбувається обрахунки калькулятора
    while True:
            op = input("Введіть операцію [+ - * / ], або ex, для того щоб завершити операцію: ")    #  Ввід операції, якщо значення буде ex то це припиняє цикл, якщо інше то цикл продовжується
            if op == "ex":
                return a  # Якщо значення op, буде ex то повертаэ значення a і зупиняє цикл
                break
            else:
                b = float(input("Введіть b: ")) # Користувач вводить дані типу float, щоб використувати в операціях не цілі числа
                match op:                        # Конструкція match
                    case "+":                    # Якщо значення op + то виконується даний випадок
                        a = add(a,b)
                    case "-":                    # Якщо значення op - то виконується даний випадок
                        a = rem(a,b)
                    case "*":                    # Якщо значення op * то виконується даний випадок
                        a = mult(a,b)
                    case "/":                    # Якщо значення op / то виконується даний випадок
                        if b == 0:               # Якщо друге значення дорівнює 0 то ділення неможливе
                            print("Операція неможлива, значення b = 0")
                        else:                          
                            a = div(a,b)
                    case _:                      # Якщо значення op не відповідає попереднім випадкам то виконується даний випадок.
                        print("Невірно вказані дані")
            print("Значення a на даний момент: ", a) # Після виконання будь-якої операції, окрім виходу, виводить проміжне значення a
            

a = askData() # Значення отримуються з функції
result = calc(a)
print("Результат обчислень: ", result)
