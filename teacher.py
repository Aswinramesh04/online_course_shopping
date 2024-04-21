class Teacher:
    def __init__(self, teacher_id, name):
        self.name = name
        self.teacher_id = teacher_id
        self.created_courses = []

    def create_course(self, course):
        self.created_courses.append(course)

    def view_created_course(self):
        return self.created_courses

