class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

class Student(Person):
    def say_name(self):
        print("Меня зовут:", self.name, self.last_name)

class Teacher(Person):
    def __init__(self, name, last_name, lesson):
        Person.__init__(self, name, last_name)
        self.lesson = lesson
    def teach(self):
        print("Я учу")

class Director(Student, Teacher):
    def __init__(self, name, last_name, lesson, school):
        Teacher.__init__(self, name, last_name, lesson)
        self.school = school
    def manage(self):
        print("Я управляю")

p = Person("Человек", "Разумный")
print(p.name, p.last_name)
print()

s = Student("Студент", "Хороший")
print(s.name, s.last_name)
s.say_name()
print()

t = Teacher("Учитель", "Заслуженный", "Программирование")
print(t.name, t.last_name, t.lesson)
t.teach()
print()

d = Director("Директор", "Школьный", "Математика", "Лучшая")
print(d.name, d.last_name, d.lesson, d.school)
d.say_name()
d.teach()
d.manage()
print()