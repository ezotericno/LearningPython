# Creating and using a class

# Class names are usually capital in Python
# creating a dog class
class Dog:
  """A simple attempt to model a dog."""

  def __init__(self, name, age):
    """Initializw name and age attributes."""
    self.name = name
    self.age = age

  def sit(self):
    """Simulate a dog sitting in response to a command."""
    print(f"{self.name} is now sitting.")

  def roll_over(self):
    """Simulate rolling over in response to a command."""
    print(f"{self.name} rolled over!")
