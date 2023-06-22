import base64
import os 

filename = input("What is the key your password/passphrase ? ")

with open(f'{filename}.txt', 'r') as file:
    encoded_password = file.read()

decoded_password = base64.b64decode(encoded_password).decode()

print(f"Your decoded password/passphrase is \033[31m{decoded_password}\033[0m")

os.remove(f'{filename}.txt')
print("For security purpose, the file has been deleted.")
print("Thanks for using QuickGenius")