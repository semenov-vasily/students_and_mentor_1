class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_student = {}
        self.student = []


    def rate_hw_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def grades_average(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades_student:
            grades_count += len(self.grades_student[grade])
            grades_sum += sum(self.grades_student[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0


    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.grades_average() > other.grades_average()
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.grades_average() < other.grades_average()
    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.grades_average() == other.grades_average()






    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.grades_average()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}\n")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades_lecturer = {}


    def grades_average(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades_lecturer:
            grades_count += len(self.grades_lecturer[grade])
            grades_sum += sum(self.grades_lecturer[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.grades_average() > other.grades_average()
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.grades_average() < other.grades_average()
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.grades_average() == other.grades_average()

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.grades_average()}\n")


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


    def rate_hw_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_student:
                student.grades_student[course] += [grade]
            else:
                student.grades_student[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")



student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.courses_in_progress += ['Django']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Tom', 'Cruise', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.courses_in_progress += ['Django']
student_2.finished_courses += ['Введение в программирование']

mentor_reviewer_1 = Reviewer('Some', 'Buddy')
mentor_reviewer_1.courses_attached += ['Python']
mentor_reviewer_1.courses_attached += ['Git']
mentor_reviewer_1.courses_attached += ['Django']

mentor_lecturer_1 = Lecturer('Lom', 'Pud')
mentor_lecturer_1.courses_attached += ['Python']
mentor_lecturer_1.courses_attached += ['Git']
mentor_lecturer_1.courses_attached += ['Django']

mentor_lecturer_2 = Lecturer('Katie', 'Holmes')
mentor_lecturer_2.courses_attached += ['Python']
mentor_lecturer_2.courses_attached += ['Git']
mentor_lecturer_2.courses_attached += ['Django']

mentor_reviewer_1.rate_hw_student(student_1, 'Python', 10)
mentor_reviewer_1.rate_hw_student(student_1, 'Python', 10)
mentor_reviewer_1.rate_hw_student(student_1, 'Python', 8)
mentor_reviewer_1.rate_hw_student(student_1, 'Git', 10)
mentor_reviewer_1.rate_hw_student(student_1, 'Django', 8)

mentor_reviewer_1.rate_hw_student(student_2, 'Python', 10)
mentor_reviewer_1.rate_hw_student(student_2, 'Python', 10)
mentor_reviewer_1.rate_hw_student(student_2, 'Python', 8)
mentor_reviewer_1.rate_hw_student(student_2, 'Git', 10)
mentor_reviewer_1.rate_hw_student(student_2, 'Django', 8)

student_1.rate_hw_lecturer(mentor_lecturer_1, 'Python', 10)
student_1.rate_hw_lecturer(mentor_lecturer_1, 'Python', 10)
student_1.rate_hw_lecturer(mentor_lecturer_1, 'Python', 7)
student_1.rate_hw_lecturer(mentor_lecturer_1, 'Git', 8)

student_2.rate_hw_lecturer(mentor_lecturer_2, 'Python', 10)
student_2.rate_hw_lecturer(mentor_lecturer_2, 'Python', 10)
student_2.rate_hw_lecturer(mentor_lecturer_2, 'Python', 7)
student_2.rate_hw_lecturer(mentor_lecturer_2, 'Git', 8)

print(f'Оценки студента {student_1.name} {student_1.surname}: ', student_1.grades_student)
print(f'Оценки студента {student_2.name} {student_2.surname}: ',student_2.grades_student)
print(f'Курсы студента {student_1.name} {student_1.surname}: ',student_1.courses_in_progress)
print(f'Курсы студента {student_2.name} {student_2.surname}: ',student_2.courses_in_progress)

print(f'Оценки лектора {mentor_lecturer_1.name} {mentor_lecturer_1.surname}: ',mentor_lecturer_1.grades_lecturer)
print(f'Оценки лектора {mentor_lecturer_2.name} {mentor_lecturer_2.surname}: ',mentor_lecturer_2.grades_lecturer)

print(mentor_reviewer_1)
print(mentor_lecturer_1)
print(mentor_lecturer_2)
print(student_1)
print(student_2)

if student_1 > student_2:
    print(f'Средняя оценка {student_1.name} {student_1.surname} больше, чем средняя оценка {student_2.name} {student_2.surname}')
elif student_1 < student_2:
    print(f'Средняя оценка {student_1.name} {student_1.surname} меньше, чем средняя оценка {student_2.name} {student_2.surname}')
else:
    print(f'Средняя оценка {student_1.name} {student_1.surname}  равна средней оценке {student_2.name} {student_2.surname}')


if mentor_lecturer_1 > mentor_lecturer_2:
    print(f'Средняя оценка {mentor_lecturer_1.name} {mentor_lecturer_1.surname} больше, чем средняя оценка {mentor_lecturer_2.name} {mentor_lecturer_2.surname}')
elif student_1 < student_2:
    print(f'Средняя оценка {mentor_lecturer_1.name} {mentor_lecturer_1.surname} меньше, чем средняя оценка {mentor_lecturer_2.name} {mentor_lecturer_2.surname}')
else:
    print(f'Средняя оценка {mentor_lecturer_1.name} {mentor_lecturer_1.surname}  равна средней оценке {mentor_lecturer_2.name} {mentor_lecturer_2.surname}')



print('ok')
