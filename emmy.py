from test import student

no_of_students = 0
while no_of_students < 5:
    name_1 = input("Enter your name: ")
    age_1 = input("Enter your age: ")
    gpa_1 = input("Enter your gpa: ")
    gender_1 = input("Enter your gender: ")
    faculty_1 = input("Enter your faculty: ") 
    department_1 = input("Enter your department: ")
    year_1 = input("Enter your year: ")

    name = name_1.lower()
    age = int(age_1)
    gpa = float(gpa_1)
    gender = gender_1.lower()
    faculty = faculty_1.lower()
    department = department_1.lower()
    year = int(year_1)

    student_one = student(name, age, gpa, gender, faculty, department, year)
    print(student_one.matric_no())
    no_of_students += 1