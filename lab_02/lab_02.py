import csv
from sys import argv

studlist = []

def printAllList():
    for elem in studlist:
        strForPrint = "Student name is " + elem["name"] + ",  Surname is " + elem["surname"] + ",  Phone is " + elem["phone"] + ",  Age is " + elem["age"]
        print(strForPrint)
    return

def addingNew():
    name = input("Pease enter student name: ")
    surname = input("Please enter student surname: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter student age: ")
    return {"name": name, "surname": surname, "phone": phone, "age": age}

def addNewElement(newItem):
    insertPosition = 0
    for item in studlist:
        if newItem["name"] > item["name"]:
            insertPosition += 1
        else:
            break
    studlist.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement(name):
    deletePosition = -1
    for item in studlist:
        if name == item["name"]:
            deletePosition = studlist.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        del studlist[deletePosition]
    return

def updatingNew(searchPosition, prname):
    upname = input("Pease enter new student name or skip: ") or prname
    upsurname = input("Please enter new student surname or skip: ") or studlist[searchPosition]["surname"]
    upphone = input("Please enter new student phone or skip: ") or studlist[searchPosition]["phone"]
    upage = input("Please enter new student age or skip: ") or studlist[searchPosition]["age"]    
    upitem = {"name": upname, "surname": upsurname, "phone": upphone, "age": upage}
    return upitem

def updateElement(name):
    searchPosition = -1
    for item in studlist:
        if name == item["name"]:
            searchPosition = studlist.index(item)
            break
    if searchPosition == -1:
        print("Element was not found")
    else:
        prname = studlist[searchPosition]["name"]
        upitem = updatingNew(searchPosition, prname)
        del studlist[searchPosition]
        if upitem["name"] == prname:
            studlist.insert(searchPosition, upitem)
        else:
            updatePosition = 0
            for item in studlist:
                if upitem["name"] > item["name"]:
                    updatePosition += 1
                else:
                    break
            studlist.insert(updatePosition, upitem)
        print("Element was updated")
        return

def loadCSV(file_name):
    try:
        with open(file_name, "r", newline ='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                studlist.append({"name":row["name"], "surname":row["surname"], "phone":row["phone"], "age":row["age"]})
            print(f"Data loaded ")
    except FileNotFoundError:
         print(f"You don't have csvfile - {file_name}, it will be created, when you exit")

def saveCSV(file_name):
    with open(file_name, "w", newline ='') as csvfile:
        fieldnames = ['name', 'surname', 'phone', 'age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in studlist:
            writer.writerow(student)
        print(f"Data in file was updated ")


def main():
    file_name = argv[1]
    loadCSV(file_name)
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement(addingNew())
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement(input("Please enter name to be updated: "))
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement(input("Please enter name to be delated: "))
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                saveCSV(file_name)
                print("Exit()")
                break
            case _:
                print("Wrong chouse")

if __name__ == "__main__":
    main()
