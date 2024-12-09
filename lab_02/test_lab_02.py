import pytest
from lab_02 import addNewElement, deleteElement, updateElement, loadCSV, saveCSV, studlist

def test_addNewElement():
    studlist.clear()
    Stud1 = {"name": "Bob", "surname": "Etica", "phone": "0900909090", "age": "21"}
    Stud2 = {"name": "Ariya", "surname": "Ericson", "phone": "0900909090", "age": "17"}
    addNewElement(Stud1)
    addNewElement(Stud2)
    assert studlist[0]["name"] == "Ariya"
    assert len(studlist) == 2

def test_deleteElement():
    studlist.clear()
    Stud1 = {"name": "Bob", "surname": "Etica", "phone": "0900909090", "age": "21"}
    addNewElement(Stud1)
    deleteElement("Bob")
    assert len(studlist) == 0
    addNewElement(Stud1)
    deleteElement("Bib")
    assert len(studlist) == 1

def test_updateElement():
    studlist.clear()
    Stud1 = {"name": "Bob", "surname": "Etica", "phone": "0900909090", "age": "21"}
    Stud2 = {"name": "Ariya", "surname": "Ericson", "phone": "0900909090", "age": "17"}
    addNewElement(Stud1)
    addNewElement(Stud2)
    updateElement("Bob")
    assert studlist[1]["surname"] == "Vilich"
    updateElement("Ariya")
    assert studlist[0]["name"] == "Bob"
    assert studlist[1]["name"] == "Zina"

def test_loadCSV():
    studlist.clear()
    testcsv = "test_lab_02.csv"
    with open(testcsv, "w") as file:
            file.write("name,surname,phone,age\n")
            file.write("Bob,Etica,0900909090,21\n")
    loadCSV(testcsv)
    assert len(studlist) == 1
    assert studlist[0]["name"] == "Bob"

def test_saveCSV():
    studlist.clear()
    testcsv = "test_lab_02.csv"
    Stud2 = {"name": "Ariya", "surname": "Ericson", "phone": "0900909090", "age": "17"}
    addNewElement(Stud2)
    saveCSV(testcsv)
    with open(testcsv, "r") as file:
         lines = file.readlines()
    assert len(lines) == 2
