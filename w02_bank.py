# bank.py
# Author: Norbert Antal
# weekly task: week02:
# Prompt the user and read in two money amounts (in cent)
# Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 

# Prompt user for two money amounts (in cent)
amount1 = int(input("Enter the first amount (in cents):\t "))
amount2 = int(input("Enter the second amount (in cents):\t "))

'''# Add the two amounts and divide sum by 100 to convert cents to euros
eur = (amount1+amount2)/100
print(f"The sum of these is: \t\t\t€{eur}")'''

# ☝️AFTER FEEDBACK
# without floats
add = amount1+amount2 # Add the two amounts and store sum in 'add'
euro = add // 100 #Floor division - returns the closest whole number after division -> in this case the largest number divisible with 100 (100 cent = 1 euro) - store value in 'euro'
cent = add % 100 #modulus operator - returns the remainder of above division. (cents) - store value in 'cents'
# Integer and float division ref: https://www.educative.io/answers/what-is-integer-and-float-division-in-python

# Display result in human readable format using the variables for formatting
print(f'''
You entered {amount1}c and {amount2}c, 
{add} cents in total,
which is {euro} Euros and {cent} cents.''')

