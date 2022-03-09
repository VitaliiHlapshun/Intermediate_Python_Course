import contextlib

staff = {
    'Austin': {
        'floor managers': 1,
        'sales associates': 5
    },
    'Melbourne': {
        'floor managers': 0,
        'sales associates': 8
    },
    'Beijing': {
        'floor managers': 2,
        'sales associates': 5
    },
}


def print_staff_report(_location, staff_dict):
    managers = staff_dict['floor managers']
    sales_people = staff_dict['sales associates']
    ratio = sales_people / managers
    print('Instrument World ' + location + ' has:')
    print(str(sales_people) + ' sales employees')
    print(str(managers) + ' floor managers')
    print('The ratio of sales people to managers is ' + str(ratio))


for location, staff in staff.items():
    # print_staff_report(location, staff)

    #1
    # try:
    #     print_staff_report(location, staff)
    # except:
    #     print('Could not print sales report for ' + location)

    #2
    with contextlib.suppress(ZeroDivisionError):
        print_staff_report(location, staff)



