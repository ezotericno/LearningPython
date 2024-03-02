import module as alias
from module import name as alias

import my_module
result = my_module.my_function(my_module.my_data)

import math as m
    
print(m.sin(m.pi/2))

import math
from math import pi
from math import sin, pi

print(sin(pi/2))


print(math.sin(math.pi/2))
