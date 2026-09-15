import math
common_passwords = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "abc123",
    "password123",
    "admin",
    "letmein",
    "welcome",
    "monkey"
]
print("================================")
print("     PASSWORD SECURITY LAB")
print("================================")

password = input("Enter a password: ")

print("Password length:", len(password))

has_uppercase = False

for character in password:
    if character.isupper():
        has_uppercase = True

print("Contains uppercase:", has_uppercase)

has_lowercase = False
for character in password:
    if character.islower():
        has_lowercase = True
print("Contains lowercase:", has_lowercase)

has_digit = False
for character in password:
    if character.isdigit():
        has_digit = True
print("Contains digit:", has_digit)

has_special = False
special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
for character in password:
    if character in special_characters:
        has_special = True
print("Contains special character:", has_special)

if len(password) < 10:
    print("Password is too short. It should be at least 10 characters long.")

if not has_uppercase:
    print("Password should contain at least one uppercase letter.")

if not has_lowercase:
    print("Password should contain at least one lowercase letter.")

if not has_digit:
    print("Password should contain at least one digit.")

if not has_special:
    print("Password should contain at least one special character.")

if len(password) >= 10 and has_uppercase and has_lowercase and has_digit and has_special:
    print("Password meets all current security requirements.")

character_pool = 0
if has_uppercase:
    character_pool += 26
if has_lowercase:
    character_pool += 26
if has_digit:
    character_pool += 10
if has_special:
    character_pool += len(special_characters) 

print("Character pool size:", character_pool)
print("Estimated entropy:", math.log2(character_pool) * len(password))

if password.lower() in common_passwords:
    print("Warning: Password is a common password and is easily guessable. Please choose a more secure password.")

if "1234" in password:
    print("Warning: Password contains a predictable number sequence.")