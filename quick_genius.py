import string
import random
import math
import hashlib
import requests
import base64

def generate_passphrase(length: int):
    response = requests.get('https://api.datamuse.com/words?max=1000&ml=planet')
    word_library = [item['word'] for item in response.json()]   
    passphrase = " ".join(random.choice(word_library) for _ in range(length))
    entropy = length * math.log2(len(word_library))

    return passphrase, entropy

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

valid_ptype = False
while not valid_ptype:
    ptype = input("Do you want to generate a (p)assword or a (pa)ssphrase? ").lower()

    if ptype in ["p", "pa"]:
        valid_ptype = True
    else:
        print("Invalid input, please enter either 'p' or 'pa'")

valid_length = False
while not valid_length:
    length = int(input("Select the length of the desired password or number of words in passphrase (4-128) ~ "))
    if 4 <= length <= 128:
        if ptype == "p":
            with_special_chars = input("Do we include special characters ? (Y/n)").lower() or "y"
            with_uppercase = input("Do we include uppercases letters ? (Y/n)").lower() or "y"
            with_lowercase = input("Do we include lowercases letters ? (Y/n)").lower() or "y"
            with_digits = input("Do we include numbers ? (Y/n)").lower() or "y"

            with_special_chars = True if with_special_chars == "y" else False
            with_uppercase = True if with_uppercase == "y" else False
            with_lowercase = True if with_lowercase == "y" else False
            with_digits = True if with_digits == "y" else False

            password, entropy = generate_password(length, with_special_chars, with_uppercase, with_lowercase, with_digits)
            entropy_status = "high" if entropy > 80 else ("medium" if entropy > 40 else "low")

            password_encoded = base64.b64encode(password.encode()).decode()
            print(f"Your encoded password is {password_encoded}")
            print(f"The password entropy equal to {entropy} bits, which is considered {entropy_status}")
            print("Please use _decode.py to decode the password")
        elif ptype == "pa":
            passphrase, entropy = generate_passphrase(length)
            entropy_status = "high" if entropy > 80 else ("medium" if entropy > 40 else "low")

            passphrase_encoded = base64.b64encode(passphrase.encode()).decode()
            print(f"Your encoded passphrase is {passphrase_encoded}")

            print(f"The passphrase entropy equal to {entropy} bits, which is considered {entropy_status}")
            print("Please use _decode.py to decode the passphrase")
        valid_length = True
    else:
        print("The length of the password or the number of words in the passphrase should be between 4 and 128. Please try again.")
