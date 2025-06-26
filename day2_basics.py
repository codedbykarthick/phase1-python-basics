# Day 2: Inputs, Conditionals, and Logic 🇩🇪

# Asking for user input
name = input("What's your name? ")
age = int(input("How old are you? "))

# Simple logic
if age >= 18:
    print(f"Welcome, {name}! You're eligible to apply for a German job 🇩🇪.")
else:
    print(f"Sorry, {name}. You're too young for Germany job hunting, but keep learning! 💻")

# Nested if
language = input("Do you know Python? (yes/no): ").lower()

if language == "yes":
    print("Nice! You're on the right track 🐍")
else:
    print("No worries. Start today and stay consistent! 🚀")
