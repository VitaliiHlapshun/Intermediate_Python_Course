def prize_generators():
    student_info = {
            "Joan Stark": 355,
            "Billy Mars": 45,
            "Tori Rivers": 18,
            "Kyle Newman": 25
        }

    for student in student_info:
        name = student
        id = student_info[name]
        if id % 3 == 0 and id % 5 == 0:
            yield student + " gets prize C"
        elif id % 3 == 0:
            yield student + " gets prize A"
        elif id % 5 == 0:
            yield student + " gets prize B"


prizes = prize_generators()
print(next(prizes))
print(next(prizes))
print(next(prizes))
print(next(prizes))
