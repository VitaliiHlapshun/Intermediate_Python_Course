guests = {}


def read_guestlist(file_name):
    text_file = open(file_name, 'r')
    while True:
        line_data = text_file.readline().strip().split(",")
        if len(line_data) < 2:
            # If no more lines, close file
            text_file.close()
            break
        name = line_data[0]
        age = int(line_data[1])
        guests[name] = age
        val = yield name, age
        if val is not None:
            val = val.split(",")
            name = val[0]
            age = int(val[1])
            guests[name] = age
            yield name, age


guestlist = read_guestlist("guest_list.txt")
for i in range(10):
    print(next(guestlist))

guestlist.send('Jane, 35')
for guest in guestlist:
    print(guest)
