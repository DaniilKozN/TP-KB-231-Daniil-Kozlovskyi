from Stud import Student

class StudList:

    def __init__(self):

        self.studlist=[]

    def printAllList(self):
        for student in self.studlist:
            print(student)
    
    def addingNew(self):
        name = input("Pease enter student name: ")
        surname = input("Please enter student surname: ")
        phone = input("Please enter student phone: ")
        age = input("Please enter student age: ")
        newItem = {"name": name, "surname": surname, "phone": phone, "age": age}
        return newItem

    def addNewElement(self,newItem):
        student = Student(newItem["name"], newItem["surname"], newItem["phone"], newItem["age"])

        insertPosition = 0
        for item in self.studlist:
            if newItem["name"] > item.name:
                insertPosition += 1
            else:
                break
        self.studlist.insert(insertPosition, student)
        return

    def deleteElement(self,name):
        deletePosition = -1
        for item in self.studlist:
            if name == item.name:
                deletePosition = self.studlist.index(item)
                break
        if deletePosition == -1:
            print("Element was not found")
        else:
            print("Dele position " + str(deletePosition))
            del self.studlist[deletePosition]
        return

    def updatingNew(self, searchPosition, previousstud):
        upname = input("Pease enter new student name or skip: ") or previousstud.name
        upsurname = input("Please enter new student surname or skip: ") or previousstud.surname
        upphone = input("Please enter new student phone or skip: ") or previousstud.phone
        upage = input("Please enter new student age or skip: ") or previousstud.age    
        upitem = {"name": upname, "surname": upsurname, "phone": upphone, "age": upage}
        return upitem

    def updateElement(self,name):
        searchPosition = -1
        for item in self.studlist:
            if name == item.name:
                searchPosition = self.studlist.index(item)
                break
        if searchPosition == -1:
            print("Element was not found")
        else:
            previousstud = self.studlist[searchPosition]
            upitem = self.updatingNew(searchPosition, previousstud)
            student = Student(upitem["name"], upitem["surname"], upitem["phone"], upitem["age"])
            del self.studlist[searchPosition]
            if upitem["name"] == previousstud.name:
                self.studlist.insert(searchPosition, student)
            else:
                updatePosition = 0
                for item in self.studlist:
                    if upitem["name"] > item.name:
                        updatePosition += 1
                    else:
                        break
                self.studlist.insert(updatePosition, student)
            print("Element was updated")
            return