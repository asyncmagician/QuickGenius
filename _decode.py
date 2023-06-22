import base64

password_encoded = input("Enter your base64 encoded password: ")
password = base64.b64decode(password_encoded).decode()

print(f"Your decoded password/passphrase is... {password}")
