class Student:
    def __init__(self, name, number, grade):
        self.name = name
        self.roll_no = number
        self.grade = grade

    def display_student_info(self):
        print(f"Имя: {self.name}")
        print(f"Номер: {self.roll_no}")
        print(f"Класс: {self.grade}")

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def display_teacher_info(self):
        print(f"Имя: {self.name}")
        print(f"Предмет: {self.subject}")

class School:
    def __init__(self):
        self.students = []
        self.teachers = []

    def add_student(self):
        name = input("Введите имя студента: ")
        number = int(input("Введите номер студента: "))
        grade = input("Введите класс студента: ")
        student = Student(name, number, grade)
        self.students.append(student)
        print("Студент добавлен успешно.")

    def add_teacher(self):
        name = input("Введите имя учителя: ")
        subject = input("Введите предмет учителя: ")
        teacher = Teacher(name, subject)
        self.teachers.append(teacher)
        print("Учитель добавлен успешно.")

    def display_students(self):
        if self.students:
            print("Список студентов:")
            for student in self.students:
                student.display_student_info()
                print("-" * 20)
        else:
            print("Список студентов пуст.")

    def display_teachers(self):
        if self.teachers:
            print("Список учителей:")
            for teacher in self.teachers:
                teacher.display_teacher_info()
                print("-" * 20)
        else:
            print("Список учителей пуст.")

school = School()

while True:
    print("\nШкольная система управления:")
    print("1. Добавить студента")
    print("2. Добавить учителя")
    print("3. Показать студентов")
    print("4. Показать учителей")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        school.add_student()
    elif choice == "2":
        school.add_teacher()
    elif choice == "3":
        school.display_students()
    elif choice == "4":
        school.display_teachers()
    elif choice == "5":
        break
    else:
        print("Неверный выбор.")