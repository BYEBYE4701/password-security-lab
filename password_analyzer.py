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

special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/"


def check_character_types(password):
    has_uppercase = any(character.isupper() for character in password)
    has_lowercase = any(character.islower() for character in password)
    has_digit = any(character.isdigit() for character in password)
    has_special = any(character in special_characters for character in password)

    return has_uppercase, has_lowercase, has_digit, has_special


def calculate_entropy(password, has_uppercase, has_lowercase, has_digit, has_special):
    character_pool = 0

    if has_uppercase:
        character_pool += 26

    if has_lowercase:
        character_pool += 26

    if has_digit:
        character_pool += 10

    if has_special:
        character_pool += len(special_characters)

    entropy = math.log2(character_pool) * len(password)

    return character_pool, entropy


def check_common_password(password):
    
    return password.lower() in common_passwords
def check_common_password_pattern(password):
    password_lower = password.lower()

    for common_password in common_passwords:
        if password_lower.startswith(common_password):
            if password_lower != common_password:
                return common_password

    return None

def check_repeated_characters(password):
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            return True

    return False


def check_sequences(password):
    sequence_length = 1

    for i in range(len(password) - 1):
        difference = ord(password[i + 1]) - ord(password[i])

        if difference == 1 or difference == -1:
            sequence_length += 1

            if sequence_length >= 3:
                return True
        else:
            sequence_length = 1

    return False


def calculate_security_score(
    password,
    has_uppercase,
    has_lowercase,
    has_digit,
    has_special,
    entropy,
    is_common_password,
    has_repeated_characters,
    has_sequence
):
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

    # Not a common password
    if not is_common_password:
        security_score += 1

    # No predictable patterns
    if not has_repeated_characters and not has_sequence:
        security_score += 1

    return security_score


def get_security_rating(security_score):
    if security_score <= 2:
        return "Very Weak"
    elif security_score <= 4:
        return "Weak"
    elif security_score <= 6:
        return "Moderate"
    elif security_score <= 8:
        return "Strong"
    else:
        return "Very Strong"


# =================================
# PASSWORD SECURITY LAB
# =================================

print("================================")
print("     PASSWORD SECURITY LAB")
print("================================")

password = input("Enter a password: ")

# Character checks
has_uppercase, has_lowercase, has_digit, has_special = check_character_types(password)

print("Password length:", len(password))
print("Contains uppercase:", has_uppercase)
print("Contains lowercase:", has_lowercase)
print("Contains digit:", has_digit)
print("Contains special character:", has_special)


# Security requirements
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


# Entropy
character_pool, entropy = calculate_entropy(
    password,
    has_uppercase,
    has_lowercase,
    has_digit,
    has_special
)
def estimate_crack_time(entropy):
    guesses_per_second = 1_000_000_000

    possible_combinations = 2 ** entropy
    seconds = possible_combinations / guesses_per_second

    return possible_combinations, seconds
print("Character pool size:", character_pool)
print("Estimated entropy:", entropy)

possible_combinations, crack_time = estimate_crack_time(entropy)

print("Possible combinations:", f"{possible_combinations:,.0f}")

if crack_time < 60:
    print("Estimated brute-force crack time:", f"{crack_time:.2f}", "seconds")
elif crack_time < 3600:
    print("Estimated brute-force crack time:", f"{crack_time / 60:.2f}", "minutes")
elif crack_time < 86400:
    print("Estimated brute-force crack time:", f"{crack_time / 3600:.2f}", "hours")
elif crack_time < 31536000:
    print("Estimated brute-force crack time:", f"{crack_time / 86400:.2f}", "days")
else:
    print("Estimated brute-force crack time:", f"{crack_time / 31536000:,.2f}", "years")

# Password analysis
is_common_password = check_common_password(password)
has_repeated_characters = check_repeated_characters(password)
has_sequence = check_sequences(password)
common_password_pattern = check_common_password_pattern(password)


if is_common_password:
    print("Warning: Password is a common password and is easily guessable. Please choose a more secure password.")
if common_password_pattern:
    print("Warning: Password is based on the common password:", common_password_pattern)

if has_repeated_characters:
    print("Warning: Password contains repeated characters.")

if has_sequence:
    print("Warning: Password contains sequential characters.")


# Security score
security_score = calculate_security_score(
    password,
    has_uppercase,
    has_lowercase,
    has_digit,
    has_special,
    entropy,
    is_common_password,
    has_repeated_characters,
    has_sequence
)

print("Security score:", security_score, "/ 10")


# Security rating
rating = get_security_rating(security_score)

print("Security rating:", rating)