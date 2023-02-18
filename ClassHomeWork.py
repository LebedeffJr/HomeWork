class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
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
        self.grades = {}

    def average_grade(self):
        for avrg in self.grades.values():
            all_grades = None
            all_grades += avrg
        all_grades / len(self.grades.values)
        return


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

Tony = Lecturer('Tony', 'Stark')
Barry = Student('Barry','Alen','man')
Banner = Reviewer('Bruce', 'Banner')

Banner.courses_attached += ['Python']
Tony.courses_attached += ['Python']
Barry.finished_courses += ['Git']
Barry.courses_in_progress += ['Python']

Banner.rate_hw(Barry, 'Python', 10)
Banner.rate_hw(Barry, 'Python', 8)
Banner.rate_hw(Barry, 'Python', 9)

Barry.rate_lecturer(Tony, 'Python', 10)
Barry.rate_lecturer(Tony, 'Python', 7)
Barry.rate_lecturer(Tony, 'Python', 9)



print(Barry.grades)
print(Tony.grades)
