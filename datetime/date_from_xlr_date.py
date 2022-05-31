import xlrd

xl_date = 44660.0

datetime_date = xlrd.xldate_as_datetime(xl_date, 0)
date_object = datetime_date.date()
string_date = date_object.isoformat()

print(string_date)
