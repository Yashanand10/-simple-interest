principal=float(input("enter the principal amount"))
rate=float(input("enter the rate if interest"))
time_period=float(input('enter the time to pay'))
simple_interest =principal*rate*time_period/100
amount=principal+simple_interest
print(simple_interest)
print(amount)
