# def cs_generator():
#   for i in range(1,5):
#     yield "Computer Science " + str(i)
#
# # Write your code below:
# cs_courses = cs_generator()
# for i in cs_courses:
#   print(next(cs_courses))
#   print(next(cs_courses))
#   print(next(cs_courses))

cs_generator_exp = ("Computer Science " + str(i) for i in range(1, 5))
for i in cs_generator_exp:
    print(next(cs_generator_exp))
    print(next(cs_generator_exp))
    print(next(cs_generator_exp))
