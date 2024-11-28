from askdata import askData,askOp         # В даному випадку from з import використовується для імпорту окремих елементів з модулю
from func import add,rem,mult,div

def calc(a):  # Функція в якій відбувається обрахунки калькулятора
    file.write(f"Begin of calc \n")      # write використовується для створення записів у файлі
    while True:
        op = askOp()
        a_prev = a  
        match op:                        # Конструкція match
            case "ex":                   # Якщо значення op ex то цикл завершується
                file.write(f"End of calc\n")
                return a
            case "+":                    # Якщо значення op + то виконується даний випадок
                a,b = add(a,askData())
            case "-":                    # Якщо значення op - то виконується даний випадок
                a,b = rem(a,askData())
            case "*":                    # Якщо значення op * то виконується даний випадок
                a,b = mult(a,askData())
            case "/":                    # Якщо значення op / то виконується даний випадок                
                a,b = div(a,askData())
        print("Значення a на даний момент: ", a) # Після виконання будь-якої операції, окрім виходу, виводить проміжне значення a
        if op == "/" and b == 0:         # Якщо відбулося ділення на 0 то про це повідомляється
            file.write(f"{a_prev} {op} {b} = Division is impossible. \n")
        else:                            # За інших випадків дані записуються в лог
            file.write(f"{a_prev} {op} {b} = {a}\n")

file = open("task2log", "a")             # Використовується для відкритя файлу
print(f"Фінальний результат: {calc(askData())}")
file.close()                             # Використовується для завершення сеансу з файлом