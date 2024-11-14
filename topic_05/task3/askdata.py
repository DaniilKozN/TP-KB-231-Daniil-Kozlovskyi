def askData():                   # Функція в якій відбувається введення даних користувачем
    while True:             # Цикл, який працює доки не буде вказано дані типу float
        try:                     # try використовується для відстеження виняткових ситуацій.
            a = float(input(" Введіть числове значення: ")) # Користувач вводить дані типу float, щоб використувати в операціях не цілі числа
        except ValueError:       # except використовується для виконання інструкцій у випадку виняткової ситуації. В даному випадку ValueError
            print(" Помилка, введене значення не число ")
        else:
            break
    return a