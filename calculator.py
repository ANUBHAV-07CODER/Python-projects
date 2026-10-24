operator = input("Enter a operator (+,-,*,/,**,%):")
num1 = float(input("Enter num1:"))
num2 = float(input("Enter num2:"))

if operator == "+":
    result = num1 + num2
    print(round(result,3))
elif operator == "-":
    result = num1 - num2
    print(round(result,3))
elif operator == "*":
    result = num1 * num2
    print(round(result,3))
elif operator == "/":
    result = num1 / num2
    print(round(result,3))
elif operator == "**":
    result = num1 ** num2
    print(round(result,3))
elif operator == "%":
    result = num1 % num2
    print(round(result,3))
else:
    print("invalid operator")