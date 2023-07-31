squares =[]
for value in range(1, 11):
  square = value ** 2 # more concise code would look like: squares.append(value **2)
  squares.append(square)

print(squares)

#Example of list comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)


