students = [{'name':"Ivan", 'mark':82},    # Не відсортований список, який використовується для реалізація lambda-функцій
         {'name':"Bob", 'mark':93},
         {'name':"Anna", 'mark':66},
         {'name':"Zybr", 'mark':81},
         {'name':"Michael", 'mark':83}]

def sortlamb(students):                    # Фунція, яка використовується для сортування
    while True:
        op=input("Введіть операцію: sn - для сортування відносно ім'я | sm - для сортування відносно оцінок | ex - для виходу: ")
        match op:
            case "sn" | "SN":
                for elem in sorted(students, key=lambda student: student["name"]):      # Цикл в якому виводиться кожний елемент списку, який сортується через функцію sorted
                    print(f"| Ім'я опитаного: {elem['name']} | Оцінка опитаного: {elem['mark']} ") # З ключем lambda за допомогою якого можна вказати сортування саме за ім'ям
                print("Сортований список за ім'ям \n")
            case "sm" | "SM":
                for elem in sorted(students, key=lambda student: student["mark"], reverse=True):# Цикл в якому виводиться кожний елемент списку, який сортується через функцію sorted
                    print(f"| Ім'я опитаного: {elem['name']} | Оцінка опитаного: {elem['mark']} ") # З ключем lambda за допомогою якого можна вказати сортування саме за оцінкою
                print("Сортований список за оцінкою \n")
            case "ex" | "EX":
                break
            case _:
                print("Невірно вказана операція")

sortlamb(students)