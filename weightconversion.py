weight = float(input("Enter the weight:"))
unit = input("Enter kilograms or pounds (k/l): ")

if unit== "k":
    weight = weight*2.205
    unit = "lbs."
    print(f"The weight in {unit} is: {round(weight, 3)}")
elif unit == "l":
    weight = weight/2.205
    unit = "kg."
    print(f"The weight in {unit} is: {round(weight, 3)}")
else:
    print(f"Invalid {unit} unit")

