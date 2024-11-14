import requests                   # import використовується для використання вмісту модуля, в даному випадку requests
r = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json") # За домогою requests.get можна отримати дані з сайтів

def sum():                        # Функція sum використовується для визначення сумми, яку потрібно конвертувати
    while True:
        try:
            sum = float(input("Введіть сумму валюти, яку ви хочете конвертувати: "))
        except ValueError:       # except використовується для виконання інструкцій у випадку виняткової ситуації. В даному випадку ValueError
            print(" Помилка, введене значення не число ")
        else:
            break
    return sum

def shownames(r):                 # Функція shownames використовується для виводу коротких назв та їх ціни за одиницю
    for elem in r.json():
        print(f"Коротка назва валюти {elem['cc']} з ціною в грн {elem['rate']}")

def convert(r):                   # Функція convert використовується для конвертування валюти 
    while True:
        name = input("Введіть коротку назву валюти ")
        for elem in r.json():
            if (name.upper() == elem['cc']):  # Якщо назва валюти співпадає з однією з назв у списку то курс отримується зі списку. Upper використовується, щоб перевести ввід користувача у великі літери
                Curr = elem['rate']
                while True:
                    con = input("Оберіть: \n c - конвертувати вказану валюту у гривню \n rc - конвертувати гривню у вказану валюту:\n ")
                    if con == "c":
                        return print(f"Результат переводу вказаної валюти у гривню: {Curr*sum()}")
                    elif con == "rc":
                        return print(f"Результат переводу грн у вказану вами валюту: {sum()/Curr}")
                    else:
                        print("Невірно вказана операція")
        print("Невірно вказана валюта")

def operation():                   # Функція operation використовується для вибору операцій
    while True:
        op = input("Введіть операцію [s,c,ex]: ")
        match op:
            case "s" | "S":
                shownames(r)
            case "c" | "C":
                convert(r)
            case "ex" | "EX":
                print("Виход")
                break
            case _:
                print("Неправильно вказана команда")

operation()