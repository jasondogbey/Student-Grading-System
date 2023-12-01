class Grade:
    def __init__(self, course_name, grade):
        self.__course_name = course_name
        self.__grade = self.__validate_grade(grade)
    
    def get_grade(self):
        return self.__grade

    def get_course_name(self):
        return self.__course_name
    
    def __validate_grade(self, grade):
        if not isinstance(grade, int) or not (0 <= grade <= 100):
            raise ValueError('Grade must be an integer between 0 and 100')
        return grade

class Course:
    def __init__(self, course_name, max_students):
        self.__course_name = course_name
        self.__max_students = self.__validate_max_students(max_students)
        self.__students = []

    def get_course_name(self):
        return self.__course_name
    
    def add_student(self, student):
        if len(self.__students) < self.__max_students:
            self.__students.append(student)
            return True
        else:
            return False

    def get_average_grade(self):
        total_grade = 0
        count_students = 0
        if self.__students:
            for student in self.__students:
                student_grades = student.get_grades_by_course_name(self.__course_name)
                if student_grades:
                    for grade in student_grades:
                        total_grade += grade.get_grade()
                        count_students +=1
            if count_students > 0:
                return total_grade / count_students
        return 0

    def __validate_max_students(self, max_students):
        if not isinstance(max_students, int) or not (0 < max_students):
            raise ValueError('Max student must be an integer greater than 0')
        return max_students
    
class Student:
    def __init__(self, name):
        self.__name = name
        self.__grades = []
    
    def add_grade(self, grade):
        if isinstance(grade, Grade):
            self.__grades.append(grade)
        else:
            raise ValueError('Invalid grade.')
    
    def get_name(self):
        return self.__name

    def get_average_grade(self):
        if self.__grades:
            total_grade = sum(grade.get_grade() for grade in self.__grades)
            return total_grade / len(self.__grades)
        else:
            return 0

    def get_grades_by_course_name(self, course_name):
        course_grades = []
        for grade in self.__grades:
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

# print(grade1_student1.grade)
# print(student1.name)

# Get average grades for students
print(f"{student1.get_name()}'s average grade: {student1.get_average_grade()}")
print(f"{student2.get_name()}'s average grade: {student2.get_average_grade()}")

# Get average grade for the course
print(f"{math_course.get_course_name()}'s average grade: {math_course.get_average_grade()}")
