"""Lambda functions are the preferred way of creating one-line functions.
The reduced syntax assists code readability and the functions can be
implemented where code reuse is not the primary objective. If we wanted our
function complexity to extend beyond one line, we would opt for a regular
function since making our function longer would impair readability. """

add_two = lambda my_input: my_input + 2

print(add_two(2))

grade_func = lambda grade: 'Got' if grade <= 90 else 'Did not get'

print(grade_func(87))
print(grade_func(91))
