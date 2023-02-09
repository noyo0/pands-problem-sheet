# bank.py
# weekly tasks: week02
# Author: Norbert Antal
# Program functions:
# Prompt the user and read in two money amounts (in cent)
# Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 

# Prompt user for two money amounts (in cent)
amount1 = int(input("Enter the first amount (in cents):\t "))
amount2 = int(input("Enter the second amount (in cents):\t "))
# Add the two amounts and divide sum by 100 to convert cents to euros
eur = (amount1+amount2)/100
# Display result in requested format
print(f"The sum of these is: \t\t\t€{eur}")