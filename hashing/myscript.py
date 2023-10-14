# from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt()

# my_pass = 'supersecretpassword'

# hashed_pass = bcrypt.generate_password_hash(my_pass)

# print(hashed_pass)

# check_1 = bcrypt.check_password_hash(hashed_pass, 'wrongpassword') 
# print(check_1)

# check_2 = bcrypt.check_password_hash(hashed_pass, 'supersecretpassword')
# print(check_2)

from werkzeug.security import generate_password_hash, check_password_hash

my_pass = 'supersecretpassword'

hashed_pass = generate_password_hash(my_pass)
print(hashed_pass)

check_1 = check_password_hash(hashed_pass, 'wrongpassword') 
print(check_1)

check_2 = check_password_hash(hashed_pass, 'supersecretpassword')
print(check_2)
