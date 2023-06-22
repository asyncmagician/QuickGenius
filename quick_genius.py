import string
import random
import math
import hashlib
import requests

def generate_password(length: int, with_special_chars=True, with_uppercase=True, with_lowercase=True, with_digits=True):
    chars = ""

    if with_special_chars:
        chars += string.punctuation

    if with_uppercase:
        chars += string.ascii_uppercase

    if with_lowercase:
        chars += string.ascii_lowercase

    if with_digits:
        chars += string.digits

    if not chars:
        raise ValueError("Not any options have been selected for the generated password")

    password = "".join(random.choice(chars) for _ in range(length))
    entropy = length * math.log2(len(chars))

    return password, entropy

def check_pwned(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5_chars, rest = sha1_password[:5], sha1_password[5:]
    response = requests.get('https://api.pwnedpasswords.com/range/' + first_5_chars)
    return rest in response.text

valid_input = False
while not valid_input:
    length = int(input("Select the length of the desired password (8-128) ~ "))
    if 8 <= length <= 128:
        with_special_chars = input("Do we include special characters ? (Y/n)").lower() or "y"
        with_uppercase = input("Do we include uppercases letters ? (Y/n)").lower() or "y"
        with_lowercase = input("Do we include lowercases letters ? (Y/n)").lower() or "y"
        with_digits = input("Do we include numbers ? (Y/n)").lower() or "y"

        with_special_chars = True if with_special_chars == "y" else False
        with_uppercase = True if with_uppercase == "y" else False
        with_lowercase = True if with_lowercase == "y" else False
        with_digits = True if with_digits == "y" else False

        if with_special_chars or with_uppercase or with_lowercase or with_digits:
            valid_input = True
        else:
            print("You must select at least one option. Please try again.")
    else:
        print("The length of the password should be between 8 and 128. Please try again.")

password, entropy = generate_password(length, with_special_chars, with_uppercase, with_lowercase, with_digits)

if check_pwned(password):
    print(f"WARNING: The password has been pwned!")
else:
    print(f"The password is safe.")

entropy_status = "high" if entropy > 80 else ("medium" if entropy > 40 else "low")

print(f"Your generated password is {password}")
print(f"The password entropy equal to {entropy} bits, current is considered {entropy_status}")
