age = tuple((28,))
print(type(age))

# should be double brackets, otherwise error TypeError: list() takes at most 1 argument (7 given) will occur
my_information = list(("Dionysia", 27, True, "Lemonaki", 7, "Python", False))


# В Python и кортежи, и списки поддерживают распаковку
# Эти значения можно «распаковать» и присвоить отдельным переменным.

front_end = ("html", "css", "javascript")
content, styling, interactivity = front_end

print(content)
