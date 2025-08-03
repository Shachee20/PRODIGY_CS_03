import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    errors = {
        "Too short (minimum 8 characters)": length_error,
        "Missing uppercase letter": uppercase_error,
        "Missing lowercase letter": lowercase_error,
        "Missing digit": digit_error,
        "Missing special character": special_char_error
    }

    failed_criteria = [msg for msg, failed in errors.items() if failed]

    if not failed_criteria:
        strength = "Strong"
    elif len(failed_criteria) <= 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, failed_criteria

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter a password to check: ")

    strength, issues = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if issues:
        print("Issues:")
        for issue in issues:
            print(f" - {issue}")
    else:
        print("Your password meets all recommended criteria.")

if __name__ == "__main__":
    main()
