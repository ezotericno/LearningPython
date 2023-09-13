# Writing to a file

# Writing to an empty file
filename = 'programming.txt'

with open(filename, 'w') as file_object:
  file_object.write("I love programming.")
# The first argument is the filename, the second 'w' tells Python that we want to open the file in write mode.
# There is read mode 'r', write mode 'w', append mode 'a', read and write mode 'r+'
# If no second argument is given Python assumes read only mode

# Writing multiple lines
file_object.write("I love programming.\n")
file_object.write("I love creating new games.\n")
# This will split the writing to two separate lines

# Appending to a file
# Writes to the end of the file instead of overwriting the current contents
# If the file does not exist Python will create a file for you

