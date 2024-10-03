def askNumb():                   # Функція в якій відбувається введення даних користувачем
    a = int(input("Введіть a: ")) # Користувач вводить дані типу int
    b = int(input("Введіть b: "))
    c = int(input("Введіть c: "))
    return a, b, c

def calcDisc(a, b, c):           # Функція в якій відбувається обрахунок дискримінанту
    D = (b**2-(4*a*c))           # Обчислення дискримінанту **-піднесення до ступеня 
    return D
    
a, b, c = askNumb()     # Значення отримуються з функції
Disc = calcDisc(a, b, c) # Значення дискримінанту обчислюється використовуючи значення, отримані з попередньої функції

if Disc > 0:            # Умовний оператор if. Якщо дискримінант більше 0, то він має два корені
    x1 = (-b + (Disc**0.5))/2*a
    x2 = (-b - (Disc**0.5))/2*a
    print("Перший корінь = ", x1, "Другий корінь = ", x2)
elif Disc == 0:        # Якщо дискримінант дорівнює 0, то він має один корінь
    x = (-b/2*a)
    print ("Корінь =", x)
else:                  # Якщо дискримінант менше 0, то він не має коренів
    print("Квардратне рівняння коренів не має")