# Cont. from pizza.py

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# use this template to import entire modules: module_name.function_name()

# Importing specific functions
from module_name import function_name

# Using "as" to Give a function an alias
# from module_name import function_name as fn
from pizza imprt make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
# you can also do the same with modules
# import pizza as p

# you can also tell python to import every function from a module
# from pizza import *
