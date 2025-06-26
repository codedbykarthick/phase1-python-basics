# Day 3: Loops & Patterns 🇩🇪

# For loop - print numbers from 1 to 5
print("Counting with for loop:")
for i in range(1, 6):
    print(i)

print()  # Blank line for spacing

# While loop - print numbers from 1 to 5
print("Counting with while loop:")
i = 1
while i <= 5:
    print(i)
    i += 1

print()  # Blank line for spacing

# Pattern printing
print("Pattern: Right-angled triangle of stars")
rows = int(input("Enter the number of rows for the pattern: "))

for i in range(1, rows + 1):
    print("*" * i)
