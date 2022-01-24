"""This is the main definition of what is GOTCHA in Python"""


def createStudent(name, age, grades=[]):
    """how NOT to do"""
    return {
        'name': name,
        'age': age,
        'grades': grades
    }


chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)


def addGrade(student, grade):
    student['grades'].append(grade)
    # To help visualize the grades we have added a print statement
    print(student['grades'])


addGrade(chrisley, 90)
addGrade(dallas, 100)

"""This is correct solution"""
