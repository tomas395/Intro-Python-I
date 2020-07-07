"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

now = datetime.now()

print("now =", now)

user_input = input(
    "Please enter desired month and day. It needs to seperated by a comma:")


def fetch_cal(dt):
    if dt == "":
        today = datetime.today()
        ty = today.year
        tm = today.month
        print(calendar.month(ty, tm))
    # This hits the first requirement. If the string is empty, it will just print todays date in the terminal.

    elif "," in dt:
        result = [x.strip() for x in dt.split(',')]
        m = int(result[0])
        y = int(result[1])

    # If the user puts a comma in the field and the numbers are in the range, it's going to give the month and year requested.
    # The .split is to make sure the leading and trailing characters are removed so it doesn't throw an error.

        print(calendar.month(y, m))
    else:
        mo = int(dt)
        yr = 2020
        print(calendar.month(yr, mo))


fetch_cal(user_input)
