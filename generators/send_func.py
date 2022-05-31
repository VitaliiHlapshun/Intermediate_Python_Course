"""The .send() method allows us to send a value to a generator using the
yield expression. If you assign yield to a variable the argument passed to
the .send() method will be assigned to that variable. Calling .send() will
also cause the generator to perform an iteration. """

MAX_STUDENTS = 50


def get_student_ids():
    student_id = 1
    while student_id < MAX_STUDENTS:
        # Write your code below
        n = yield student_id
        print(n)
        if n is not None:
            student_id = n
            continue
        student_id += 1

def generator_func(n):
    student_id_generator = get_student_ids()
    for i in student_id_generator:
        # Write your code below
        if i == 10:
            i = student_id_generator.send(n)

        print(i)

generator_func(30)

# def generator():
#     count = 0
#     while True:
#         n = yield count
#         if n is not None:
#             count = n
#         count += 1
#
#
# my_generator = generator()
# print(next(my_generator))  # Output: 0
# print(next(my_generator))  # Output: 1
# print(my_generator.send(3))  # Output: 4
# print(next(my_generator))  # Output: 5