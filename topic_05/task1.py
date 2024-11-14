import random                   # import використовується для використання вмісту модуля, в даному випадку random 

def Answer(pch):                # Функція в якій вирішується хто переміг, комп'ютер чи учасник
    pcch = random.choice(["stone", "scissor", "paper"]) # за допомогою random.choice обирається один з 3 елементів списку
    print(f"Ви обрали {pch}\nКомп'ютер обрав {pcch}")
    if pch == pcch:
        print("Нічья")
    else:
        match pch:
            case "stone":
                if pcch == "scissor":
                    print("Ви перемогли")
                else:
                    print("Ви програли")
            case "scissor":
                if pcch == "paper":
                    print("Ви перемогли")
                else:
                    print("Ви програли")
            case "paper":
                if pcch == "stone":
                    print("Ви перемогли")
                else:
                    print("Ви програли")

def Pch(Plist):                # Функція в якій учасник обирає, що він обирає: камінь, ножиці чи бумагу
    while True:
        pch = input("Оберіть stone, scissor або paper: ")
        for elem in Plist:
            if pch == elem:
                return pch
        print(" Невірно вказані дані, введіть повторно")

Plist = ["stone", "scissor", "paper"]
Answer(Pch(Plist))