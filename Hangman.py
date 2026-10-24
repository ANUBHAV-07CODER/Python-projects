import random

words = ["python", "computer", "programming", "network"]
word = random.choice(words)
display = ["_"] * len(word)
 
print("Welcome to Hangman!")
print(" ".join(display))

while "_" in display:
    guess = input("Guess a letter: ").lower()
    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        print("Wrong guess!")
    print(" ".join(display))

print("🎉 You won!")
print("The word was:", word)