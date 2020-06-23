import random
import string

print('Password Generator')
print('Your new password is: ')

letters = string.ascii_letters
letters = ( ''.join(random.choice(letters) for i in range(10)))

digits = string.digits
digits = ( ''.join(random.choice(digits) for i in range(10)))

special_characters = "!,§,$,%,&,/,=,?"
special_characters= ( ''.join(random.choice(special_characters) for i in range(3)))

password = letters + digits + special_characters
print(password)
