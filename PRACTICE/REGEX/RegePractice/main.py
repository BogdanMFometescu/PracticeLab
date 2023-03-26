import re

username = "bogdan"
password = "password"
email = "bogdan-fometescu@yahoo.com"


# Patter for password requirements
reg_pattern = re.search(r'(?=.*\d)(?=.*[a-z])(?=.*\W)', password)

# Check email format
match_email = re.search(r'[\w.-]+@[\w.-]{1,25}', email)  # max length, allow @ and -

if match_email:
    print(match_email.group())
else:
    print("Wrong email format")

# Check username length
match_username = re.search(r'\w{1,8}', username)

if match_username:
    print(match_username.group())
else:
    print("Username in wrong format")

# Check password
match_password = re.search(r'\w{8,15}',password)

if match_password:
    print(match_password.group())
else:
    print("Password in wrong format")

