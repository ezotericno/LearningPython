# A simple dictionary
alien_0 = {color: 'green', points: 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Adding new key value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25

# Starting with an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

# Modifiying values in a Dictionary
alien_0['color2'] = 'yellow'
# Give the name of the dictionary with the new value or the value
# that is to be modified

# Example of tracking the position of an alien
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

# move the alien to the right
# detemine how far to move the alien based on its speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3