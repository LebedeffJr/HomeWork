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

    def average_grade(self):
        sum_grades = 0
        for avrg in self.grades.values():
            for gr in avrg:
                sum_grades += gr
        m = sum_grades / len(avrg)
        return m

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\
            \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: \
            {", ".join(self.finished_courses)}'


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
        sum_grades = 0
        for avrg in self.grades.values():
            for gr in avrg:
                sum_grades += gr
        m = sum_grades / len(avrg)
        return m
    def __lt__(self, other):
        if not isinstance(other, Mentor):
            print('Not a Mentor!')
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

Tony = Lecturer('Tony', 'Stark')
Deadpool = Lecturer('Wade', 'Wilson')
Barry = Student('Barry','Alen','man')
Peter = Student('Peter', 'Parker', 'man')
Banner = Reviewer('Bruce', 'Banner')
Logan = Reviewer('James', 'Howlett')

Logan.courses_attached += ['Python']
Deadpool.courses_attached += ['Python']
Banner.courses_attached += ['Python']
Tony.courses_attached += ['Python']
Barry.finished_courses += ['Git']
Barry.courses_in_progress += ['Python']
Peter.finished_courses += ['Git']
Peter.courses_in_progress += ['Python']

Banner.rate_hw(Barry, 'Python', 10)
Banner.rate_hw(Barry, 'Python', 8)
Banner.rate_hw(Barry, 'Python', 9)
Logan.rate_hw(Peter,'Python', 10)
Logan.rate_hw(Peter,'Python', 5)
Logan.rate_hw(Peter,'Python', 7)

Peter.rate_lecturer(Deadpool, 'Python', 10)
Peter.rate_lecturer(Deadpool, 'Python', 10)
Peter.rate_lecturer(Deadpool, 'Python', 10)
Barry.rate_lecturer(Tony, 'Python', 10)
Barry.rate_lecturer(Tony, 'Python', 7)
Barry.rate_lecturer(Tony, 'Python', 9)


print(Barry < Peter)
