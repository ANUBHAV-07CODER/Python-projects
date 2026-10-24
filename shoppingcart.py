foods = []
prices = []
total_price = 0

while True:
    food = input("Enter food item (or 'q' to quit): ")

    if food.lower() == "q":
        break

    price = float(input("Enter price: "))

    foods.append(food)
    prices.append(price)

    total_price += price

print("\nYour shopping cart:")

for food, price in zip(foods, prices):
    print(f"{food}: ${price:.2f}")

print(f"\nYour Total Price: ${total_price:.2f}")
    

    