from teacher import Teacher
from course import Course
from customer import Customer

class Web_Management:
    def __init__(self):
        self.teachers = []
        self.courses = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def display_available_courses(self):
        return self.courses
