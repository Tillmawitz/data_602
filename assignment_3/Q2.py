hours = int(input("Please enter the number of hours worked: "))
pay = int(input("Please enter your hourly pay rate: "))
total_pay = 0
 

if (hours <= 20):
    total_pay = hours * pay
else:
    overtime = (hours - 20) * pay * 1.5
    regular_pay = 20 * pay
    total_pay = regular_pay + overtime

print(f"Your total pay was ${total_pay}")