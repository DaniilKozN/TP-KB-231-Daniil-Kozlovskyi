from askdata import askData         # В даному випадку from з import використовується для імпорту окремих елементів з модулю
from func import add,rem,mult,div

def calc(a):  # Функція в якій відбувається обрахунки калькулятора
    while True:
        op = input(" Введіть операцію [+ - * / ], або ex, для того щоб завершити операцію: ")    
        match op:                        # Конструкція match
            case "ex":                   # Якщо значення op ex то цикл завершується
                return a
            case "+":                    # Якщо значення op + то виконується даний випадок
                a = add(a,askData())
            case "-":                    # Якщо значення op - то виконується даний випадок
                a = rem(a,askData())
            case "*":                    # Якщо значення op * то виконується даний випадок
                a = mult(a,askData())
            case "/":                    # Якщо значення op / то виконується даний випадок                
                a = div(a,askData())
            case _:                      # Якщо значення op не відповідає попереднім випадкам то виконується даний випадок.
                print(" Невірно вказані дані")
        print("Значення a на даний момент: ", a) # Після виконання будь-якої операції, окрім виходу, виводить проміжне значення a
            
print(f"Фінальний результат: {calc(askData())}")