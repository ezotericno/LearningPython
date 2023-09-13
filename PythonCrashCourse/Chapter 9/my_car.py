# Importing Classes
# Import a single class
from car import Car

# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
