
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "surname":"Evanson", "phone":"0631234567", "age":"30"},
    {"name":"Emma", "surname":"Millerovich", "phone":"0631234567", "age":"20"},
    {"name":"Jon", "surname":"Smith", "phone":"0631234567", "age":"18"},
    {"name":"Zak", "surname":"Bush", "phone":"0631234567", "age":"27"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Surname is " + elem["surname"] + ",  Phone is " + elem["phone"] + ",  Age is " + elem["age"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    surname = input("Please enter student surname: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter student age: ")
    newItem = {"name": name, "surname": surname, "phone": phone, "age": age}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    searchPosition = -1
    for item in list:
        if name == item["name"]:
            searchPosition = list.index(item)
            break
    if searchPosition == -1:
        print("Element was not found")
    else:
        prname = list[searchPosition]["name"]

        upname = input("Pease enter new student name or skip: ") or prname
        upsurname = input("Please enter new student surname or skip: ") or list[searchPosition]["surname"]
        upphone = input("Please enter new student phone or skip: ") or list[searchPosition]["phone"]
        upage = input("Please enter new student age or skip: ") or list[searchPosition]["age"]
        
        upitem = {"name": upname, "surname": upsurname, "phone": upphone, "age": upage}
        del list[searchPosition]
        if upname == prname:
            list.insert(searchPosition, upitem)
        else:
            updatePosition = 0
            for item in list:
                if upname > item["name"]:
                    updatePosition += 1
                else:
                    break
            list.insert(updatePosition, upitem)
        print("Element was updated")
        return
    # implementation required

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()