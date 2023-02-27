# weekday.py
# Author: Norbert Antal
# Program checks if current date falls on a weekday or not
# ref: datetime module - https://docs.python.org/3/library/datetime.html
from datetime import date #imports datetime module
today = date.today() # get today's date
day = today.weekday() # convert to weekday number
if day>4: #check if day value is more than 4 (Saturday would be 5 and Sunday 6) and set text variable accordingly.
    mytext = "It is the weekend, yay!" 
else:
    mytext = "Yes, unfortunately today is a weekday."
# arrange and print all information.
print("Today's date is:") 
print(today.strftime("%A, %d. %B %Y"))
print(mytext)