import re

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Length >= 8 characters": not length_error,
        "At least one lowercase letter": not lowercase_error,
        "At least one uppercase letter": not uppercase_error,
        "At least one digit": not digit_error,
        "At least one special character": not special_char_error
    }

    score = sum(errors.values())

    if score == 5:
        strength = "Strong"
    elif 3 <= score < 5:
        strength = "Medium"
    else:
        strength = "Weak"

    print(f"\nPassword Strength: {strength}\n")
    print("Criteria Check:")
    for criteria, passed in errors.items():
        print(f" - {criteria}: {'✔' if passed else '✘'}")

# Password input in Replit safely
pwd = input("Enter your password: ")
check_password_strength(pwd)
