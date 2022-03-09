colors = {
    'red': '#FF0000',
    'blue': '#0000FF',
    'yellow': '#FFFF00',
}

for color in ('red', 'green', 'yellow'):
    try:
        print('The hex value of ' + color + ' is ' + colors[color])
    except:
        # raise KeyError('Hui vam')
        print('An exception occurred! Color does not exist.')
    print('Loop continues...')
