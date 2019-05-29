"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
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
"""

import sys
import calendar
from datetime import datetime

"""
Brady used the sys arguments which makes sense seeing as the sys module was imported
"""

def render_calendar(month, year):
    c = calendar.TextCalendar(calendar.SUNDAY) 
    str = c.formatmonth(year, month)
    print(str)

# Accept user input
date = input("Enter month & year, example 5/2005: ").split('/')

# If user input is empty, print the calendar for the current month.
if len(date) <= 1 and len(date[0]) < 1:
    month = datetime.now().month
    year = datetime.now().year
    render_calendar(month, year)
elif len(date) == 1:
    month = int(date[0])
    year = datetime.now().year
    render_calendar(month, year)
elif len(date) == 2:
    month = int(date[0])
    year = int(date[1])
    render_calendar(month, year)
else:
    print("Enter month & year, example 5/2005")