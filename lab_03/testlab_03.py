import pytest
from StudList import StudList
from Util import CSVop

def test_addNewElement():
    stud_list = StudList()
    Stud1 = {"name": "Bob", "surname": "Etica", "phone": "0900909090", "age": "21"}
    Stud2 = {"name": "Ariya", "surname": "Ericson", "phone": "0900909090", "age": "17"}
    stud_list.addNewElement(Stud1)
    stud_list.addNewElement(Stud2)
    assert stud_list.studlist[0].name == "Ariya"
    assert stud_list.studlist[1].name == "Bob"
    assert len(stud_list.studlist) == 2

def test_deleteElement():
    stud_list = StudList()
    Stud1 = {"name": "Bob", "surname": "Etica", "phone": "0900909090", "age": "21"}
    stud_list.addNewElement(Stud1)
    stud_list.deleteElement("Bob")
    assert len(stud_list.studlist) == 0
    stud_list.addNewElement(Stud1)
    stud_list.deleteElement("Bib")
    assert len(stud_list.studlist) == 1

def test_updateElement():
    stud_list = StudList()
    Stud1 = {"name": "Bob", "surname": "Etica", "phone": "0900909090", "age": "21"}
    Stud2 = {"name": "Ariya", "surname": "Ericson", "phone": "0900909090", "age": "17"}
    stud_list.addNewElement(Stud1)
    stud_list.addNewElement(Stud2)
    stud_list.updateElement("Bob")
    assert stud_list.studlist[1].surname == "Vilich"
    stud_list.updateElement("Ariya")
    assert stud_list.studlist[0].name == "Bob"
    assert stud_list.studlist[1].name == "Zina"

def test_saveloadCSV():
    stud_list = StudList()
    file = CSVop(stud_list)
    Stud2 = {"name": "Ariya", "surname": "Ericson", "phone": "0900909090", "age": "17"}
    stud_list.addNewElement(Stud2)
    file.saveCSV()
    file.loadCSV()
    assert len(stud_list.studlist) == 1
    assert stud_list.studlist[0].name == "Ariya"