class Student: 
    def __init__(self, name, age):
        self.name = name
        self.age=age
    def show_info(self):
        print("Name:",self.name)
        print("Age:",self.age)
s1=Student("shiba",20)
s1.show_info()