import datetime
today=datetime.datetime.now()
print("today datetime:",today)
print("current year is:",today.year)
print("month of year:",today.month)
print("week of year:",today.strftime("%U"))
print("weekday of the week:",today.strftime("%A"))
print("day no of the year:",today.strftime("%j"))
print("day no of the month:",today.strftime("%d"))
print("day no of the week:",today.strftime("%w"))
