import string
import random
import math

def generate_password(length: int, with_special_chars =True, with_uppercase : bool = True, with_lowercase : bool = True, with_digits : bool = True):
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

valid_input = False
while not valid_input:
    length = int(input("Select the length of the desired password ~ "))
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

password, entropy = generate_password(length, with_special_chars, with_uppercase, with_lowercase, with_digits)

password, entropy = generate_password(length, with_special_chars, with_uppercase, with_lowercase, with_digits)

print(f"The generated password : {password}")
print(f"The password entropy : {entropy} bits")