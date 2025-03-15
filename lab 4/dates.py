# Python Dates
# Explanation:
# Python's datetime module is used to work with dates and times.

# Examples of Working with Dates
# Get Current Date and Time

import datetime
now = datetime.datetime.now()
print(now)
# Formatting Dates

today = datetime.date.today()
print(today.strftime("%Y-%m-%d"))  # Output: 2025-03-01
# Parsing a Date String

date_string = "2024-12-04"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print(parsed_date)
# Calculating Time Difference

date1 = datetime.date(2024, 12, 4)
date2 = datetime.date(2025, 1, 1)
delta = date2 - date1
print(delta.days)  # Output: 28
