class Students:                         # class - це власностворений тип (int,str та інші), в даному викпадку класс Студенти
    def __init__(self, name, age):      # Конструкторк __init__, необхідний для створення класу об'єкта, тут також визначаються атрибути об'єкту 
        self.name = name                # self - ключове слово через яке можна звертатися всередині класу до функціональності поточного об'єкта
        self.age = age

    def __str__(self):                  # __str__ використовується коли ми використовуємо print, щоб сформувати прийнятний вигляд виводу
        return f"Student name: {self.name} | Student age : {self.age}"

students = [Students("Ivan", 18),      # Список об'єктів класу Students
        Students("Maria", 28),
        Students("Boris", 16),
        Students("Gviana", 31)]

def sortlamb(students):                    # Фунція, яка використовується для сортування
    while True:
        op=input("Введіть операцію: sn - для сортування відносно ім'я | sa - для сортування відносно віку | ex - для виходу: ")
        match op:
            case "sn" | "SN":
                for student in sorted(students, key=lambda student: student.name):      # Цикл в якому виводиться кожний елемент списку, який сортується через функцію sorted
                    print(student)                                                      # З ключем lambda за допомогою якого можна вказати сортування саме за ім'ям
                print("Сортований список за ім'ям \n")
            case "sa" | "SA":
                for student in sorted(students, key=lambda student: student.age, reverse=True):# Цикл в якому виводиться кожний елемент списку, який сортується через функцію sorted
                    print(student)                                                             # З ключем lambda за допомогою якого можна вказати сортування саме за віком
                print("Сортований список за віком, від старшого до молодшого \n")
            case "ex" | "EX":
                break
            case _:
                print("Невірно вказана операція")

sortlamb(students)