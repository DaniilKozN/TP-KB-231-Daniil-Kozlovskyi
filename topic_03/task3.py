def dictupdate(somedict):                            # Функція update використовуються для об'єднання двох словників
    somenewdict = {"Belgium": 3, "Switzerland": 2 }
    somedict.update(somenewdict)
    return somedict

def dictdel(somedict):
    del somedict["Poland"]                            # Функція del використовуються для видалення окремого елементу з заданим ключем
    return somedict

def dictclear(somedict):                              # Функція clear використовуються для очистки словника
    somedict.clear()
    return somedict

def dictkey(somedict):                                # Функція keys використовуються для виділення ключей зі словника
    dictkeys = somedict.keys()
    return dictkeys

def dictvalues(somedict):                             # Функція values використовуються для виділення значень зі словника
    values = somedict.values()
    return values

def dictitem(somedict):                               # Функція items використовуються для виділення ключа разом з його значенням зі словника
    items = somedict.items()
    return items

somedict = {
    "Poland": 2,
    "Netherlands": 3,
    "Egypt": 4
}
func = input("Введіть операцію [u, d, c, k, v, i]: ")        # Ввід операції
print("Оригілнальний словник: ",somedict)

match func:                        # Конструкція match, яка використовується для виклику однієї окремої функції
    case "u":   
        sd = dictupdate(somedict)              
        print("Результат дії функції update:", sd)
    case "d":                    
        sd = dictdel(somedict)
        print("Результат дії функції del:", sd)
    case "c":                    
        sd = dictclear(somedict)
        print("Результат дії функції clear:", sd)
    case "k":                   
        sd = dictkey(somedict)
        print("Результат дії функції keys:", sd)
    case "v":                   
        sd = dictvalues(somedict)
        print("Результат дії функції values:", sd)
    case "i":                   
        sd = dictitem(somedict)
        print("Результат дії функції items:", sd)
    case _:                     
        print("Невірно вказані дані")