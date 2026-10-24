year = int(input("Enter a year:"))

print(f"🚀 Mad Libs: The Year {year} 🚀\n")

name = input("Name: ")
place = input("Place: ")
animal = input("Animal: ")
adjective = input("Adjective: ")
verb = input("Verb: ")
object = input("Object: ")
food = input("Food: ")

story = f"""
It was the year {year}. {name} was walking through {place}
when a {adjective} {animal} suddenly appeared! 
The animal asked {name} to {verb} using a {object}.
Surprised but excited, {name} agreed and celebrated
by eating {food}. From that day, {name} became known
as the hero of {year}! 🚀
"""

print(story)