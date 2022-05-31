def course_generator():
    yield ('Computer Science', 5)
    # Checkpoint 1
    yield ('Art', 10)
    yield ('Business', 15)


# Checkpoint 2
def add_five_students(courses):
    for course, num_students in courses:
        yield (course, num_students + 5)


# Checkpoint 3
increased_courses = add_five_students(course_generator())
for course in increased_courses:
    print(course)
