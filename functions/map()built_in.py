# res = filter(lambda x: x > 3, [100, 2, 3])
# print(list(res))
#
# res = map(lambda x: x > 3, [100, 2, 3])
# print(list(res))


books = [["Burgess", 1985], ["Orwell", "Nineteen Eighty-four"], ["Murakami", "1Q85"], ["Orwell", 1984], ["Burgess", "Nineteen Eighty-five"], ["Murakami", 1985]]

# Your code below:

# assign the result of your filter function to the variable  string_titles

string_titles = filter(lambda value: isinstance(value[1], str), books)

# convert your filter object to a list stored in the variable string_titles_list

string_titles_list = list(string_titles)

# print the list string_titles_list

print(string_titles_list)
