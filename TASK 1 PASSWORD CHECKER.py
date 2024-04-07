import re

def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return any(char.isupper() for char in password)

def check_lowercase(password):
    return any(char.islower() for char in password)

def check_digit(password):
    return any(char.isdigit() for char in password)

def check_special_char(password):
    special_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    return special_chars.search(password) is not None

def assess_strength(password):
    criteria_checks = [
        ("Length >= 8 characters", check_length(password)),
        ("Uppercase character", check_uppercase(password)),
        ("Lowercase character", check_lowercase(password)),
        ("Digit", check_digit(password)),
        ("Special character", check_special_char(password))
    ]

    strength = sum(1 for _, check in criteria_checks if check)

    if strength == 5:
        return "Strong"
    elif strength >= 3:
        return "Medium"
    else:
        return "Weak"

def main():
    password = input("Enter your password: ")
    strength = assess_strength(password)
    print("Password strength:", strength)

if __name__ == "__main__":
    main()

