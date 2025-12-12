import calendar

year = int(input("Enter the year: "))
month = input("Enter the month: ")
cal = calendar.month(year , month)
print(cal)