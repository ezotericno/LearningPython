# Using while loop with lists and dictionaries

# Moving items from one list to another
  # Start with users that need to be verified
  # add an empty list to hold confimed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
#    Move each verified user into the list of confirmed users.
while unconfirmed_users:
  current_user = unconfirmed_user.pop()

  print(f"Verifying user: {current_user.title()}")
  confirmed_users.append(current_user)
  # Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
  print(confirmed_user.title())

