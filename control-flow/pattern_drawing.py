# pattern_drawing.py

# Prompt user for input
sizeOfSquare = int(input("Enter the size of the pattern: "))

# Draw the pattern
row = 1
while row <= sizeOfSquare:
    col = 1
    while col <= sizeOfSquare:
        print("*", end="")
        col += 1
    print()  # Move to the next line after printing each row
    row += 1

