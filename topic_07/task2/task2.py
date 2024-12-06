from askdata import Ask         # В даному випадку from з import використовується для імпорту окремих елементів з модулю
from func import Function       # В даному випадку class Функцій та отримання даних 

class Calcuation:               
    def __init__(self):
        self.func = Function()  # Створюю нові об'єкти двох класів Function та Ask, який буде зберігатися в даному класі
        self.opd = Ask()        # Це можна використовувати для виклику операцій в інших класах

    def calc(self):             # Метод в класі, які представляють функції, які визначені всередині класу і які визначають його поведінку. 
        a = self.opd.askData()
        while True:
            a_prev = a
            op = self.opd.askOp()
            if op == "ex":       # Якщо значення op ex то цикл завершується
                with open("topic_07/task2/task2log", "a") as file:
                    file.write(f"End of calc\n")
                return a
            else:
                a,b = self.Operation(a,op)
                print("Значення a на даний момент: ", a) # Після виконання будь-якої операції, окрім виходу, виводить проміжне значення a
                self.save(a,a_prev,b,op)
    
    def Operation(self,a,op):
        match op:                        # Конструкція match
                case "+":                    # Якщо значення op + то виконується даний випадок
                    a,b = self.func.add(a,self.opd.askData())
                    return a,b
                case "-":                    # Якщо значення op - то виконується даний випадок
                    a,b = self.func.rem(a,self.opd.askData())
                    return a,b
                case "*":                    # Якщо значення op * то виконується даний випадок
                    a,b = self.func.mult(a,self.opd.askData())
                    return a,b
                case "/":                    # Якщо значення op / то виконується даний випадок                
                    a,b = self.func.div(a,self.opd.askData())
                    return a,b


    def save(self,a,a_prev,b,op):
        with open("topic_07/task2/task2log", "a") as file: # Використовується для відкритя файлу
            if op == "/" and b == 0:         # Якщо відбулося ділення на 0 то про це повідомляється
                file.write(f"{a_prev} {op} {b} = Division is impossible. \n")
            else:                            # За інших випадків дані записуються в лог
                file.write(f"{a_prev} {op} {b} = {a}\n")

def main():
    with open("topic_07/task2/task2log", "a") as file:
        file.write(f"Start of calc \n")
    calc = Calcuation()           # Об'єкт класу Calculation
    calc.calc()                   # Використовуючи ім'я об'єкта можна звернутися до його методів. При цьому поза класом self використовувати не потрібно 

main()