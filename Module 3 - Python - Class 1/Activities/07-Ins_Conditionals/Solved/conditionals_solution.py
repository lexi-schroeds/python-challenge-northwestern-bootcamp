x = 1
y = 10

# Checks if one value is equal to another
if x == 1:
    print("x is equal to 1")

# Checks if one value is NOT equal to another
if y != 1:
    print("y is not equal to 1")

# Checks if one value is less than another
if x < y:
    print("x is less than y")

# Checks if one value is greater than another
if y > x:
    print("y is greater than x")

# Checks if a value is greater than or equal to another
if x >= 1:
    print("x is greater than or equal to 1")

# Checks for two conditions to be met using "and"
if x == 1 and y == 10:
    print("Both values returned true")

# Checks if either of two conditions is met
if x < 45 or y < 5:
    print("One or more of the statements were true")

if 50 < 2**5:
    print("50 < 2**5")
else:
    print("50 is not < 2**5")

g = 87
letter = 'unknown'
if g >= 90:
    letter = 'A'
elif g >= 80:
    letter = 'B'
elif g >= 70:
    # whatever you need to do
    letter = 'C'
else:
    letter = 'F'

print(f"grade is {letter}")


# Nested if statements
if x < 10:
    if y < 5:
        print("x is less than 10 and y is less than 5")
    elif y == 5:
        print("x is less than 10 and y is equal to 5")
    else:
        print("x is less than 10 and y is greater than 5")
else:
    print("x is not less than 10")