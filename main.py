class Student:
    def __init__(self, name, surname, date_of_birth):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth


x = Student("Nikita", "Nikatov", "01.02.2000")
y = Student("vanya", "vaninov", "12.12.1996")

print(x)
print(y)
