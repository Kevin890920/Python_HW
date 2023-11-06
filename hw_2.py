class Student:
    def __init__(self, name, student_id, age, gender):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.gender = gender
    def set_grade(self, grade):
        self.grade = grade
    def get_grade(self):
        print("Usage : <Grade>")
        self.grade = float(input("Please enter your grade : "))
    def display_student_info(self):
        print("Name :", self.name)
        print("Student_ID :", self.student_id)
        print("Age :", self.age)
        print("Gender :", self.gender)
        print("Grade :", self.grade)

student = Student("Kevin", "R12942121", "22", "male")
student.get_grade()
student_info = student.display_student_info()
print("123")