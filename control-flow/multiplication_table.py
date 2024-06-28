# multiplication_table.py

# Prompt user for input from 1 -10
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table
for num in range(1, 11):
    multi = number * num
    print(f"{number} * {num} = {multi}")

