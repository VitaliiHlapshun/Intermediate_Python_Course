numbers = [1, 10, 20, 70, 5]

def binary(target):
    found = False
    buttom = 0
    top = len(numbers) - 1
    while (buttom <= top and not found):
        middle = (buttom + top) // 2
        if numbers[middle] == target:
            return True
        elif numbers[middle] > buttom:
            buttom = middle + 1
        else:
            top = middle - 1
    return False

print(binary(67))
