import random

symbols = ["🍒", "🍋", "⭐", "🔔", "7️⃣"]

while True:
    print("\n--- SLOT MACHINE ---")
    input("Press Enter to spin...")

    slot1 = random.choice(symbols)
    slot2 = random.choice(symbols)
    slot3 = random.choice(symbols)

    print(f"\n| {slot1} | {slot2} | {slot3} |")

    if slot1 == slot2 == slot3:
        print("🎉 JACKPOT! You won!")
    elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
        print(" Two symbols matched! Small win!")
    else:
        print("You lost!")

    play_again = input("\nPlay again? (yes/no): ")

    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break