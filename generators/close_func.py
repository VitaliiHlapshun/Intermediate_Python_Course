"""
The generator method .close() is used to terminate a generator early.
Once the .close() method is called the generator is finished just like the
end of a for loop.
"""


def generator():
    i = 0
    while True:
        n = yield i
        # print(f'n -----> {n}')
        if n is not None:
            i = n
            # continue
        i += 1


my_generator = generator()
for el in my_generator:
    if el == 5:
        el = my_generator.send(7)
    elif el == 15:
        my_generator.close()
    print(el)
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# # next(my_generator)
# my_generator.close()
# next(my_generator)  # raises StopGenerator exception
