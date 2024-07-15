from models import *

session = get_session()

# Creating a new student and course
student = create_student("Wisdom Okposin", regNo="AK17/ENG/EEE/058")
course = create_course(name="Mathematics")

# Query and print the Student class
print("The students in the class are:")
for student in session.query(Student).all():
    print(student.name, student.regNo)

# Query and print the courses available
print("\nThe available courses are:")
for course in session.query(Course).all():
    print(course.name)

# Enroll a student in a course
if enroll_student(student.studentId, course.courseId):
    print(f"\n{student.name} successfully enrolled for {course.name}")
else:
    print(f"Enrollment of {student.name} in {course.name} failed.")

