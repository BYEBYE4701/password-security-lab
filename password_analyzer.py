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
entropy = math.log2(character_pool) * len(password)
print("Estimated entropy:", entropy)

if password.lower() in common_passwords:
    print("Warning: Password is a common password and is easily guessable. Please choose a more secure password.")

if "1234" in password:
    print("Warning: Password contains a predictable number sequence.")

has_repeated_characters = False
for i in range(len(password) - 1):
    if password[i] == password[i + 1]:
        has_repeated_characters = True

if has_repeated_characters:
    print("Warning: Password contains repeated characters.")

has_sequence = False
sequence_length = 1

for i in range(len(password) - 1):
    difference = ord(password[i + 1]) - ord(password[i])

    if difference == 1 or difference == -1:
        sequence_length += 1

        if sequence_length >= 3:
            has_sequence = True
    else:
        sequence_length = 1

if has_sequence:
    print("Warning: Password contains sequential characters.")

security_score = 0

# Length
if len(password) >= 20:
    security_score += 3
elif len(password) >= 14:
    security_score += 2
elif len(password) >= 10:
    security_score += 1

# Character diversity
if has_lowercase:
    security_score += 1

if has_uppercase:
    security_score += 1

if has_digit:
    security_score += 1

if has_special:
    security_score += 1

# Entropy
if entropy >= 60:
    security_score += 1

# Predictability penalties
if password.lower() in common_passwords:
    security_score -= 5

if has_repeated_characters:
    security_score -= 1

if has_sequence:
    security_score -= 1
if security_score < 0:
    security_score = 0

print("Security score:", security_score)