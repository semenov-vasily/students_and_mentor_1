class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_student = {}

    def rate_hw_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'
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


student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']

mentor_reviewer_1 = Reviewer('Some', 'Buddy')
mentor_reviewer_1.courses_attached += ['Python']

mentor_lecturer_2 = Reviewer('Lom', 'Pud')
mentor_lecturer_2.courses_attached += ['Python']

mentor_reviewer_1.rate_hw_student(student_1, 'Python', 10)
mentor_reviewer_1.rate_hw_student(student_1, 'Python', 10)
mentor_reviewer_1.rate_hw_student(student_1, 'Python', 10)

student_1.rate_hw_lecturer(mentor_lecturer_2, 'Python', 10)
student_1.rate_hw_lecturer(mentor_lecturer_2, 'Python', 10)
student_1.rate_hw_lecturer(mentor_lecturer_2, 'Python', 10)

print(student_1.grades_student)
print(mentor_lecturer_2.grades_lecturer)
print('ok')
