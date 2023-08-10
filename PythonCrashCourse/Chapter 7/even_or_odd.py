# The Modulo Operator
# The modulo operator doesn't tell you how many times one number fits into another. It just tells you what the remainder is.
# When one number is divisible by another number, the remainder is 0.

# we will now use that rule to see if a number is even or odd

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
  print(f"\nThe number {number} is even.")
else:
  print(f"\nThe number {number} is odd.")
