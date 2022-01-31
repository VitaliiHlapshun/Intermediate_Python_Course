walls = [(20, 9), (25, 9), (20, 9), (25, 9)]


def calc_paint_amount(wall_measurements):
    square_feet = 0

    def calc_square_feet():
        for width, height in wall_measurements:
            nonlocal square_feet
            square_feet += width * height

    def calc_gallons():
        return square_feet / 400

    calc_square_feet()
    print(square_feet)
    return calc_gallons(), square_feet


print('Number of paint gallons needed: ')
print(str(calc_paint_amount(walls)))
