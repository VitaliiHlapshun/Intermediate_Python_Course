def print_available(color):
  global paint_gallons_available
  paint_gallons_available = {
    'red': 50,
    'blue': 72,
    'green': 99,
    'yellow': 33
  }
  print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')


print_available('red')

def func():
  for keys, values in paint_gallons_available.items():
    print(values)
func()