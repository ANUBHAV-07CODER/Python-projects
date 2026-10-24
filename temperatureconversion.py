unit = input("Enter the unit Celcius or Fahrenheit (C/F): ")
temp = float(input("enter the temperature:"))

if unit == "C":
    temp = round((temp *9)/5 +32,1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round(((temp - 32) * 5)/9,1)
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print(f"Invalid {unit} unit")
