prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}

py_and_dry = frozenset(
    {'classic', 'rock', 'electric guitar', 'rock and roll'})

# Find the intersection between them while providing the `frozenset` first.
frozen_intersected_tags = py_and_dry.intersection(prepare_to_py)
print(frozen_intersected_tags)

"""===================================================================
========================VICE VERSA================================="""


prepare_to_py_2 = {'rock', 'heavy metal', 'electric guitar', 'synth'}

py_and_dry_2 = frozenset(
    {'classic', 'rock', 'electric guitar', 'rock and roll'})

# Find the intersection between them while providing the `frozenset` first.
frozen_intersected_tags_2 = prepare_to_py_2.intersection(py_and_dry_2)
print(frozen_intersected_tags_2)
