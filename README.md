# QuickGenius - Simple and Customizable Password Generator

Welcome to QuickGenius! This script helps you generate random passwords ou passphrase with ease. You can customize the length, character set, and more to create a strong and secure password/passphrase for your online accounts. It's 100% open-source. 

## ⚠️ Important Note
QuickGenius is a simple password generator and **NOT** a password manager. It store the generated password/passphrase locally and removes it after it's been decoded.
🌍 Internet is required, it uses [HaveIbeenPwnd](https://haveibeenpwned.com/API/v2) and [DataMuse](https://haveibeenpwned.com/API/v2) APIs

Please use a dedicated password manager, like [Passbolt](https://github.com/passbolt), to store and manage your passwords securely.

## Get Started

1. Clone QuickGenius
```bash
git clone https://github.com/asyncmagician/QuickGenius.git
```

2. Run `quick_genius.py` script to generate a password or passphrase.

3. Select the generation type:
    - (p) for a password
    - (pa) for a passphrase

4. Choose the desired length for the password or the number of words in the passphrase.
5. Answer the questions to customize the password or passphrase based on your preferences.
6. A text file will be created to store the encoded password or passphrase. The filename will be displayed on the screen.
7. To decode the password or passphrase, run `_decode.py` script.
8. Enter the filename (key) of the password or passphrase to decode.
9. The password or passphrase will be decoded and displayed in color.
10. The text file will be automatically deleted for security purposes.