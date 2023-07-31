# List slicing

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # leaving the second item blank will print list from first number specified
# using a negative index number like players[-3:] would only slice the last 3 of the list

print("Here are the first three players on my team: ")
for player in players[:3]: # This would print the first three items of the list
  print(player.title())

