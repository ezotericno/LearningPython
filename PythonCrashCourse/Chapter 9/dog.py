# Creating and using a class

# Class names are usually capital in Python
# creating a dog class
class Dog:
  """A simple attempt to model a dog."""

  def __init__(self, name, age):
    """Initializw name and age attributes."""
    self.name = name
    self.age = age
# Variables that are accessible through instances like this are called attributes.
  def sit(self):
    """Simulate a dog sitting in response to a command."""
    print(f"{self.name} is now sitting.")

  def roll_over(self):
    """Simulate rolling over in response to a command."""
    print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3) # Creating multiple instances
# To access the attributes of an instance, you use . notation

print(f"\nYour dog's name is {your_dog.name}.")
print(f"\nYour dog is {your_dog.age} years old.")
my_dog.sit()

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
your_dog.sit()

# Calling Methods
my_dog.sit()
my_dog.roll_over()
