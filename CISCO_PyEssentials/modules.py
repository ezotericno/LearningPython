import mod1
import mod2, mod3, mod4
   
import mod2
import mod3
import mod4
  
import my_module
   
result = my_module.my_function(my_module.my_data)

from module import my_function, my_data
  
result = my_function(my_data)

from my_module import *
  
result = my_function(my_data)

from module import my_function as fun, my_data as dat
  
result = fun(dat)

