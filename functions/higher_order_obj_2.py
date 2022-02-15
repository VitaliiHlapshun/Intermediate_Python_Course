"""So far, we have focused on higher-order functions that take another
function as an argument. Remember, though, that a function that returns
another function is also a higher-order function.

Higher-order functions are possible because functions are first-class
objects in Python, meaning that a function can be stored as a variable,
passed as an argument to a function, returned by a function, and stored in
data structures (lists, dictionaries, etc.). """


def make_box_volume_function(height):
    # defines and returns a function that takes two numeric arguments,
    # length &  width, and returns the volume given the input height
    def volume(length, width):
        return length * width * height

    return volume


box_volume_height15 = make_box_volume_function(15)

print(box_volume_height15(3, 2))