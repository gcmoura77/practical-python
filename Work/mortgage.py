# mortgage.py
#
# Exercise 1.7
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. 
# The interest rate is 5% and the monthly payment is $2684.11.


principal = 500000.0
rate = 0.05
total_paid = 0.0
month = 1

extra_payment_start_month = int(input("Enter the month you will start making extra payments: "))
extra_payment_end_month = int(input("Enter the month you will stop making extra payments: "))
extra_payment = int(input("Enter the amount of extra payment: "))

while principal > 0:
    payment = 2684.11
    if (month >= extra_payment_start_month) & (month <= extra_payment_end_month):
        payment = payment + extra_payment

    if (principal + principal*rate/12) < payment:
        total_paid = total_paid + (payment-(principal + principal*rate/12))
        principal = 0
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    print(month, round(total_paid,2), round(principal,2))
    month += 1

print('Total paid', round(total_paid,2), month-1)