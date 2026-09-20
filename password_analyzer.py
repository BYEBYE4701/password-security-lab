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


# =================================
# FUNCTIONS
# =================================

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


def estimate_crack_time(entropy):
    guesses_per_second = 1_000_000_000

    possible_combinations = 2 ** entropy
    seconds = possible_combinations / guesses_per_second

    return possible_combinations, seconds


def check_common_password(password):
    return password.lower() in common_passwords


def check_common_password_pattern(password):
    password_lower = password.lower()

    for common_password in common_passwords:
        if password_lower.startswith(common_password):
            if password_lower != common_password:
                return common_password

    return None


def check_character_substitution(password):
    substitutions = {
        "@": "a",
        "4": "a",
        "3": "e",
        "1": "i",
        "0": "o",
        "$": "s",
        "5": "s",
        "7": "t"
    }

    normalized_password = password.lower()

    for character, replacement in substitutions.items():
        normalized_password = normalized_password.replace(character, replacement)

    for common_password in common_passwords:
        if normalized_password == common_password:
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

def main():

    # =================================
    # PASSWORD SECURITY LAB
    # =================================

    print()
    print("=" * 50)
    print("             PASSWORD SECURITY LAB")
    print("=" * 50)

    password = input("\nEnter a password: ")


    # =================================
    # CHARACTER ANALYSIS
    # =================================

    has_uppercase, has_lowercase, has_digit, has_special = check_character_types(password)

    print()
    print("[ CHARACTER ANALYSIS ]")
    print("-" * 50)

    print(f"{'Length:':25}", len(password))
    print(f"{'Uppercase:':25}", "✓" if has_uppercase else "✗")
    print(f"{'Lowercase:':25}", "✓" if has_lowercase else "✗")
    print(f"{'Digits:':25}", "✓" if has_digit else "✗")
    print(f"{'Special characters:':25}", "✓" if has_special else "✗")


    # =================================
    # SECURITY REQUIREMENTS
    # =================================

    print()
    print("[ SECURITY REQUIREMENTS ]")
    print("-" * 50)

    requirements_met = True

    if len(password) < 10:
        print("✗ Password must be at least 10 characters long.")
        requirements_met = False

    if not has_uppercase:
        print("✗ Password should contain an uppercase letter.")
        requirements_met = False

    if not has_lowercase:
        print("✗ Password should contain a lowercase letter.")
        requirements_met = False

    if not has_digit:
        print("✗ Password should contain a digit.")
        requirements_met = False

    if not has_special:
        print("✗ Password should contain a special character.")
        requirements_met = False

    if requirements_met:
        print("✓ Password meets all current security requirements.")


    # =================================
    # ENTROPY ANALYSIS
    # =================================

    character_pool, entropy = calculate_entropy(
        password,
        has_uppercase,
        has_lowercase,
        has_digit,
        has_special
    )

    print()
    print("[ ENTROPY ANALYSIS ]")
    print("-" * 50)

    print(f"{'Character pool:':25}", character_pool)
    print(f"{'Estimated entropy:':25}", f"{entropy:.2f} bits")


    # =================================
    # BRUTE-FORCE ESTIMATE
    # =================================

    possible_combinations, crack_time = estimate_crack_time(entropy)

    print()
    print("[ BRUTE-FORCE ESTIMATE ]")
    print("-" * 50)

    print(f"{'Possible combinations:':25}", f"{possible_combinations:,.0f}")

    if crack_time < 60:
        print(
            f"{'Estimated crack time:':25}",
            f"{crack_time:.2f} seconds"
        )

    elif crack_time < 3600:
        print(
            f"{'Estimated crack time:':25}",
            f"{crack_time / 60:.2f} minutes"
        )

    elif crack_time < 86400:
        print(
            f"{'Estimated crack time:':25}",
            f"{crack_time / 3600:.2f} hours"
        )

    elif crack_time < 31536000:
        print(
            f"{'Estimated crack time:':25}",
            f"{crack_time / 86400:.2f} days"
        )

    else:
        print(
            f"{'Estimated crack time:':25}",
            f"{crack_time / 31536000:,.2f} years"
        )


    # =================================
    # PREDICTABILITY ANALYSIS
    # =================================

    is_common_password = check_common_password(password)
    common_password_pattern = check_common_password_pattern(password)
    substitution_pattern = check_character_substitution(password)
    has_repeated_characters = check_repeated_characters(password)
    has_sequence = check_sequences(password)

    print()
    print("[ PREDICTABILITY ANALYSIS ]")
    print("-" * 50)

    warnings_found = False

    if is_common_password:
        print("✗ Common password detected.")
        warnings_found = True

    if common_password_pattern:
        print(
            "✗ Password is based on the common password:",
            common_password_pattern
        )
        warnings_found = True

    if substitution_pattern:
        print(
            "✗ Predictable character substitutions detected.",
            "Based on:",
            substitution_pattern
        )
        warnings_found = True

    if has_repeated_characters:
        print("✗ Repeated characters detected.")
        warnings_found = True

    if has_sequence:
        print("✗ Sequential characters detected.")
        warnings_found = True

    if not warnings_found:
        print("✓ No common predictable patterns detected.")


    # =================================
    # SECURITY SCORE
    # =================================

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

    rating = get_security_rating(security_score)

    print()
    print("[ FINAL RESULT ]")
    print("-" * 50)

    print(f"{'Security score:':25}", f"{security_score} / 10")
    print(f"{'Security rating:':25}", rating)

    print()
    print("=" * 50)
    print("              ANALYSIS COMPLETE")
    print("=" * 50)

if __name__ == "__main__":
    main()