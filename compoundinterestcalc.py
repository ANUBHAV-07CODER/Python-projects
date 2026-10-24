principle = float(input("Enter the principle amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("principle amount cannot be negative")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest: "))
    if rate < 0:
        print("rate of interest cannot be negative")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("time cannot be negative")
    else:
        break

total = round(principle * pow(1 + rate/100,time), 2)
print(f"The total amount is: ${total}")