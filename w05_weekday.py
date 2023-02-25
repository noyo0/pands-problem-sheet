# weekday.py
# Author: Norbert Antal
# Program checks if current date falls on a weekday or not
# ref: datetime module - https://docs.python.org/3/library/datetime.html
from datetime import date
today = date.today()
day = today.weekday()
if day>4:
    mytext = "It is the weekend, yay!"
else:
    mytext = "Yes, unfortunately today is a weekday."
print("Today's date is:")
print(today.strftime("%A, %d. %B %Y"))
print(mytext)