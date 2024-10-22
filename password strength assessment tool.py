import re
import time
from termcolor import colored

def check_length(password):
    time.sleep(0.3)
    return len(password) >= 8

def check_uppercase(password):
    time.sleep(0.3)
    return any(char.isupper() for char in password)

def check_lowercase(password):
    time.sleep(0.3)
    return any(char.islower() for char in password)

def check_digit(password):
    time.sleep(0.3)
    return any(char.isdigit() for char in password)

def check_special_char(password):
    time.sleep(0.3)
    special_characters = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    return special_characters.search(password) is not None

def assess_password_strength(password):
    criteria_checks = {
        "Length (min 8 characters)": check_length,
        "Uppercase letter": check_uppercase,
        "Lowercase letter": check_lowercase,
        "Number": check_digit,
        "Special character": check_special_char
    }

    strength = 0
    feedback = []

    for criteria, check_function in criteria_checks.items():
        time.sleep(0.5)
        if check_function(password):
            strength += 1
            feedback.append((criteria, colored("✔", "green")))
        else:
            feedback.append((criteria, colored("✘", "red")))

    return strength, feedback

def print_feedback(feedback):
    time.sleep(0.5)
    print("\nPassword Strength Feedback:")
    for criteria, status in feedback:
        status_color = "green" if status == "✔" else "red"
        print(f"{criteria}: {colored(status, status_color)}")

def print_strength_meter(strength):
    time.sleep(0.5)
    meter = colored("■" * strength, "green") + colored("□" * (5 - strength), "red")
    print("\nPassword Strength Meter:")
    print(meter)

def main():
    print("Password Strength Checker\n")
    while True:
        password = input("Enter your password: ")
        if len(password) == 0:
            print("Password cannot be empty. Please try again.")
        else:
            break

    print("\nAssessing password strength...")
    time.sleep(1)

    strength, feedback = assess_password_strength(password)

    print("\nPassword Strength:", f"{strength} / 5")
    print_strength_meter(strength)
    print_feedback(feedback)

    if strength == 5:
        print("\nCongratulations! Your password is strong.")
    else:
        print("\nYour password is weak. Please consider the feedback provided.")
    
    with open("task3.txt", "a") as file:
        file.write(f"Password: {password}, Strength: {strength}/5\n")

if __name__ == "__main__":
    main()
