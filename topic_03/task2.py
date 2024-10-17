def listextend(somelist):           # Функція extend використовуються для додавання елементів типу list,string,tuple та інші в кінець списку
    somenewlist = [18, 10, -1]
    somelist.extend(somenewlist)
    return somelist

def listappend(somelist):           # Функція append використовуються для додавання елементу в кінець списку 
    somelist.append("adc")
    return somelist

def listinsert(somelist):           # Функція insert використовуються для додавання елементу у визначене місце
    somelist.insert(2,"Amx")
    return somelist

def listremove(somelist):           # Функція remove використовуються для видалення першого зазначеного елементу
    somelist.remove(1)
    return somelist

def listclear(somelist):            # Функція clear використовуються для очищення списку
    somelist.clear()
    return somelist

def listsort(somelist):             # Функція sort використовуються для cортування списку
    somelist.sort()
    return somelist

def listreverse(somelist):          # Функція reverse використовуються для перевертання списку
    somelist.reverse()
    return somelist

def listcopy(somelist):             # Функція copy використовуються для копіювання списку
    copysomelist = somelist.copy()
    return copysomelist


somelist = [1, 14, 12, 1, 7]
func = input("Введіть операцію [e, a, i, rm, cl, s, rv, cp ]: ") # Ввід операції
print("Оригілнальний список: ",somelist)

match func:                        # Конструкція match, яка використовується для виклику однієї окремої функції
    case "e":   
        sl = listextend(somelist)              
        print("Результат дії функції extend:", sl)
    case "a":                    
        sl = listappend(somelist)
        print("Результат дії функції append:", sl)
    case "i":                    
        sl = listinsert(somelist)
        print("Результат дії функції insert:", sl)
    case "rm":                   
        sl = listremove(somelist)
        print("Результат дії функції remove:", sl)
    case "cl":                   
        sl = listclear(somelist)
        print("Результат дії функції clear:", sl)
    case "s":                   
        sl = listsort(somelist)
        print("Результат дії функції sort:", sl)
    case "rv":                   
        sl = listreverse(somelist)
        print("Результат дії функції reverse:", sl)
    case "cp":                   
        sl = listcopy(somelist)
        print("Результат дії функції copy:", sl)
    case _:                     
        print("Невірно вказані дані")