# Q2. Design a program that asks the user to enter a store’s sales for each day of the
# week. The amounts should be stored in a list. Use a loop to calculate the total sales for
# the week and display the result.
import sys

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
weekly_sales = []

for day in days:
    try :
        weekly_sales.append(int(input("Please enter the sales for " + day + ": ")))
    except ValueError:
        print("Invalid input program terminating")
        sys.exit()

total_sales = 0
for sale in weekly_sales:
    total_sales += sale

print("Total sales this week were: " + str(total_sales))