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

# without floats
add = str(amount1+amount2)
eur = add[:-2]
cnt = add[-2]
# Display result in requested format
print(f"The sum of these is: {add}\t\t\t{eur} Euros and {cnt} cents")
#this is only working if the sum is min 100 cents unless I add an if statement

