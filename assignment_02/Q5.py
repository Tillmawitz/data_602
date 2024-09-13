# Write a program that keeps names and email addresses in a dictionary as
# key-value pairs. The program should then demonstrate the four options:
# ● look up a person’s email address,
# ● add a new name and email address,
# ● change an existing email address, and
# ● delete an existing name and email address.

emails = {'tim': 'tim@gmail.com', 'dan': 'dan@hotmail.com', 'tina': 'tina@hotmail.com', 'lisa': 'lisa@gmail.com'}
print(emails)
print(emails['dan'])
emails['erica'] = 'erica@spsmail.cuny.com'
print(emails)
emails['erica'] = 'erica@spsmail.cuny.edu'
print(emails)
del(emails['tim'])
print(emails)