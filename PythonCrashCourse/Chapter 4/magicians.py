magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: # Prints each name on a new line using a for loop
  print(magician) 

for magician in magicians:
  print(f"{magician.title()}, that was a great trick!") # Prints a message to each magician on a new line

print("Thank you, everyone. That was a great magic show!") # since this line is not indented it runs after the for loops have completed



