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

if len(password) < 8:
    print("Password is too short. It should be at least 8 characters long.")

if not has_uppercase:
    print("Password should contain at least one uppercase letter.")

if not has_lowercase:
    print("Password should contain at least one lowercase letter.")

if not has_digit:
    print("Password should contain at least one digit.")

if not has_special:
    print("Password should contain at least one special character.")

if len(password) >= 8 and has_uppercase and has_lowercase and has_digit and has_special:
    print("Password meets all current security requirements.")