class Student:
    def __init__(self,name,surname,phone,age):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.age = age
    def __str__(self):
        return f"Name: '{self.name}', surname: '{self.surname}', phone: '{self.phone}', age: '{self.age}' "