# Positional Arguments
def describe_pet(animal_type, pet_name):
  """Display information about a pet"""
  print(f"\nI have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

describe_pet('dog', 'willie')

# Order matters in a positional argument
# Passing the following will make the output unintelligile. 
describe_pet('harry', 'hamster')

# Keyword Arguments
#    name-value pair that you pass to a function
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster') # each will pass the same output, regardless of which key value is entered first

# Default Values
#    When describing a function default values can be set, therefore only one is needed when the function is called.
