# Write your code below:
import itertools

max_capacity = 1000
num_bags = 0
for num in itertools.count(13.5, 13.5):
    if num > max_capacity:
        break
    num_bags += 1
print(num_bags)
