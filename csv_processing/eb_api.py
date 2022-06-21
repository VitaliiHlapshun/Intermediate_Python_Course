import csv

with open('fabrics.csv', newline='') as csvfile:
    spamreader = list(csv.reader(csvfile, delimiter=','))
    for row in spamreader:
        print(f'<record id="button_style_{row[0]}" '
              f'model="button.style">'
              f'<field name="name">{row[1]}</field>'
              f'<field name="ebapi_id">{row[0]}</field>'
              '</record>')
