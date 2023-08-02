# Dictionary of similar objects
favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
}

# To look for this info you can use the below code
language = favorite_language['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# Looping Dictionaries cont.
for name, language in favorite_languages.items():
  print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping through all the keys in a Dictionary
# Using the keys() method
for name in favorite_languages.keys():
  print(name.title())

# Accessing specific values in a dictionary while looping through it
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
  print(f"Hi {name.title()}.")

  if name in friends:
    language = favorite_languages[name].title()
    print(f"\t{name.title()}, I see you love {language}!")

# Looping through a dictionary's keys in a particular order
for name in sorted(favorite_languages.keys()):
  print(f"{name.title()}, thank you for taking the poll.")

# Looping through all values in a dictionary
# Using the values() method
print("The following languages have been mentioned:")
for language in favorite_languages.values():
  print(language.title())
# You can use the set() method to pull out the items and not call any repetitive values


