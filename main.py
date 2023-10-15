class Student:
    """
    Defines a Student class
    """
    def __init__(self, name, surname, date_of_birth):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f'{self.surname.title()} {self.name[0].upper()}.'


class Group:
    def __init__(self, title: str, start_date: str):
        self.title = title
        self.start_date = start_date
        self.__students = []

    def add_student(self, student: Student):
        if isinstance(student, Student) and student not in self.__students:
            self.__students.append(student)

    def __str__(self):
        return f'{self.title} - {self.start_date}\nList of students:\n' + '\n'.join(map(str, self.__students))

    def __len__(self):
        return len(self.__students)


gr = Group('Python', '11.10.2023')
gr.add_student(Student('Ivan', 'Ivanov1', '12.02.2000'))
gr.add_student(Student('Ivan', 'Ivanov2', '12.02.2000'))
gr.add_student(Student('Ivan', 'Ivanov3', '12.02.2000'))
gr.add_student(Student('Ivan', 'Ivanov4', '12.02.2000'))
gr.add_student(Student('Ivan', 'Ivanov5', '12.02.2000'))
gr.add_student(Student('Ivan', 'Ivanov6', '12.02.2000'))
print(gr)

print(len(gr))