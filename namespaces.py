"""Python uses the system of names so that it can differentiate between each distinct object (such as a string or a
function) that we define. In most programs, Python has to keep track of the hundreds and sometimes even thousands of
names. So, how exactly does Python store all of this information? Well, it creates what is called a namespace.

A namespace is a collection of names and the objects that they reference. Python will host a dictionary where the
keys are the names that have been defined and the mapped values are the objects that they reference.

Built-In
Global
Local
Enclosing
"""


def get_color(position):
    color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    print(color_list[position])


get_color(2)
