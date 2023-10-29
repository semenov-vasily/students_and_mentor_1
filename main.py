class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_student = {}
        self.grades_average_homework = []

    def rate_hw_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'



    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {', '.join(self.grades_average_homework)}\n"
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
        self.grades_average_lecture = []
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {', '.join(self.grades_average_lecture)}\n")


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
student_1.finished_courses += ['Введение в программирование']


mentor_reviewer_1 = Reviewer('Some', 'Buddy')
mentor_reviewer_1.courses_attached += ['Python']
mentor_reviewer_1.courses_attached += ['Git']

mentor_lecturer_2 = Lecturer('Lom', 'Pud')
mentor_lecturer_2.courses_attached += ['Python']

mentor_reviewer_1.rate_hw_student(student_1, 'Python', 10)
mentor_reviewer_1.rate_hw_student(student_1, 'Python', 10)
mentor_reviewer_1.rate_hw_student(student_1, 'Python', 10)
mentor_reviewer_1.rate_hw_student(student_1, 'Git', 10)

student_1.rate_hw_lecturer(mentor_lecturer_2, 'Python', 10)
student_1.rate_hw_lecturer(mentor_lecturer_2, 'Python', 10)
student_1.rate_hw_lecturer(mentor_lecturer_2, 'Python', 10)

print(student_1.grades_student)
print(student_1.courses_in_progress)

print(mentor_lecturer_2.grades_lecturer)

print(mentor_reviewer_1)
print(mentor_lecturer_2)
print(student_1)

print('ok')
