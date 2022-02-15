"""
In Python, all functions, including the ones we’ve written, are classified as
first-class objects (sometimes also called first-class citizens or first-class
 functions). This means they have four important characteristics:

First-class objects can be stored as variables. First-class objects can be
passed as arguments to a function. First-class objects can be returned by a
function. First-class objects can be stored in data structures (e.g.,
lists, dictionaries, etc.). """

from datetime import datetime

# Here, we assign a function to a variable
uppercase = str.upper

# And then call it
big_pie = uppercase("pumpkinpie")
print(big_pie)


# string_manipulation_functions = [str.upper, str.lower]
# for i in string_manipulation_functions:
#     print(i('lkjsdflkjsdfFFLKJSFKLSJDFLKJSD'))


def add_tax(total):
    tax = total * 0.06
    new_total = total + tax
    return new_total


def total_bills(func, l):
    # This list will store all the new bill values

    time_before = datetime.now()
    total = func(l)
    time_after = datetime.now()
    print(f'functions has been executed in {time_after - time_before}')
    return l


def ranger(iterrrrr):
    return [len(str(i))for i in iterrrrr]


sequence = ['asd', 'sdfkjhgsjdfhdvj,zdfh,zjdhvzdfk']

bills = total_bills(ranger, sequence)

print(bills)

lis = ['asd', 'et']
print(list(map(len, lis)))
