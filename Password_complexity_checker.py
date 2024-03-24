import re

def assess_password_strength(password):
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_special_char = bool(re.search(r'[!@#$%^&*()\-_=+{};:,<.>]', password))

    strength = 0
    if length >= 8:
        strength += 1
    if has_uppercase:
        strength += 1
    if has_lowercase:
        strength += 1
    if has_number:
        strength += 1
    if has_special_char:
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength <= 3:
        return "Moderate"
    elif strength <= 4:
        return "Strong"
    else:
        return "Very Strong"

# Example usage:
password = input("Enter your password: ")
strength = assess_password_strength(password)
print("Password strength:", strength)


