# Passing an Arbitrary number of arguments

def make_pizza(*toppings):
  """Print the list of toppings that have been requested."""
  print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
  """Summarize the pizza we are about to make."""
  print("\nMaking a pizza with the following toppings:")
  for topping in toppings:
    print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Making Positional and arbitrary arguments
def make_pizza(*toppings):
  """Summarize the pizza we are about to make."""
  print("\nMaking a {size}-inch pizza with the following toppings:")
  for topping in toppings:
    print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Storing your functions in modules
# Using Import to take from other files can help with the readibility of your program
# There are several ways to import a module

# Continued in seperate file making_pizzas.py
