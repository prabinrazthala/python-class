#Create a class Person with instance attributes name and age. Create a method get_details in this class to print name and age.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_details(self):
        return f'My name is {self.name} and age is {self.age}'

result = Person("Prabin",31)
print(result.get_details())