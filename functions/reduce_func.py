from functools import reduce

letters = ['r', 'e', 'd', 'u', 'c', 'e']

# your code below:
word = reduce(lambda x, y: 2*x + y, letters)
# remember to import the reduce function

# store the result of your reduce function in the variable word

print(word)
# print word
