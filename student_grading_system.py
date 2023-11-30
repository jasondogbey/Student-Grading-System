class Grade:
    def __init__(self, course_name, grade):
        self.course_name = course_name
        self.grade = grade
    
    def get_grade(self):
        return self.grade

    def get_course_name(self):
        return self.course_name

class Course:
    def __init__(self, course_name, max_students):
        self.course_name = course_name
        self.max_students = max_students
        self.students = []

    def get_course_name(self):
        return self.course_name
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def get_average_grade(self):
        total_grade = 0
        count_students = 0
        if self.students:
            for student in self.students:
                student_grades = student.get_grades_by_course_name(self.course_name)
                if student_grades:
                    for grade in student_grades:
                        total_grade += grade.get_grade()
                        count_students +=1
            if count_students > 0:
                return total_grade / count_students
        return 0

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if self.grades:
            total_grade = sum(grade.get_grade() for grade in self.grades)
            return total_grade / len(self.grades)
        else:
            return 0

    def get_grades_by_course_name(self, course_name):
        course_grades = []
        for grade in self.grades:
            if grade.get_course_name() == course_name:
                course_grades.append(grade)
        return course_grades


# Example Usage:

# Creating students
student1 = Student("Alice")
student2 = Student("Bob")

# Creating courses
math_course = Course("Math", 2)
science_course = Course("Science", 2)

# Adding students to courses
math_course.add_student(student1)
math_course.add_student(student2)
science_course.add_student(student1)
science_course.add_student(student2)

# Adding grades for students
grade1_student1 = Grade("Math", 85)
grade2_student1 = Grade("Science", 90)
grade1_student2 = Grade("Math", 78)
grade2_student2 = Grade("Science", 92)

student1.add_grade(grade1_student1)
student1.add_grade(grade2_student1)
student2.add_grade(grade1_student2)
student2.add_grade(grade2_student2)

print(grade1_student1.get_grade())

# Get average grades for students
print(f"{student1.name}'s average grade: {student1.get_average_grade()}")
print(f"{student2.name}'s average grade: {student2.get_average_grade()}")

# Get average grade for the course
print(f"{math_course.course_name}'s average grade: {math_course.get_average_grade()}")
