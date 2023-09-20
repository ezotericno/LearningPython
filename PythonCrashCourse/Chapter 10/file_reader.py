with open('pi_digits.txt') as file_object:
  contents = file_object.read()
print(contents)

# Using a for loop to read line by line
filename = 'pi_digits.txt'

with open(filename) as file_object:
  for line in file_object:
    print(line)
# Use .rstrip() to eliminate blank spaces in between lines printed
