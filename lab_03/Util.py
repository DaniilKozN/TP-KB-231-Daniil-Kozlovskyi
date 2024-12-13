import csv
import sys
from StudList import StudList

class CSVop:
    def __init__(self, studn_list:StudList):
        self.studn_list = studn_list
        self.file = sys.argv[1]
    
    def loadCSV(self):
        self.studn_list.studlist = []
        try:
            with open(self.file, "r", newline ='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.studn_list.addNewElement(row)
                print(f"Data loaded ")
        except FileNotFoundError:
            print(f"You don't have csvfile - {self.file}, it will be created, when you exit")

    def saveCSV(self):
        with open(self.file, "w", newline ='') as csvfile:
            fieldnames = ['name', 'surname', 'phone', 'age']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for student in self.studn_list.studlist:
                writer.writerow({
                    "name": student.name,
                    "surname": student.surname,
                    "phone": student.phone,
                    "age": student.age
                })
            print(f"Data in file was updated ")