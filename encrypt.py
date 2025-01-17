# Encryption function
def encrypt(text, n, m):
    encrypted_text = ""
    for char in text:
        # For lowercase a-m
        if 'a' <= char <= 'm':
            encrypted_text += chr(((ord(char) - ord('a') + n * m) % 13) + ord('a'))
        # For lowercase n-z
        elif 'n' <= char <= 'z':
            encrypted_text += chr(((ord(char) - ord('n') - (n + m)) % 13) + ord('n'))
        # For uppercase A-M
        elif 'A' <= char <= 'M':
            encrypted_text += chr(((ord(char) - ord('A') - n) % 13) + ord('A'))
        # For uppercase N-Z
        elif 'N' <= char <= 'Z':
            encrypted_text += chr(((ord(char) - ord('N') + m**2) % 13) + ord('N'))
        # Special characters, and numbers remain unchanged
        else:
            encrypted_text += char
    return encrypted_text
# Decryption function
def decrypt(text, n, m):
    decrypted_text = ""
    for char in text:
        # Reverse lowercase a-m
        if 'a' <= char <= 'm':
            decrypted_text += chr(((ord(char) - ord('a') - n * m) % 13) + ord('a'))
        # Reverse lowercase n-z
        elif 'n' <= char <= 'z':
            decrypted_text += chr(((ord(char) - ord('n') + (n + m)) % 13) + ord('n'))
        # Reverse uppercase A-M
        elif 'A' <= char <= 'M':
            decrypted_text += chr(((ord(char) - ord('A') + n) % 13) + ord('A'))
        # Reverse uppercase A-M
        elif 'N' <= char <= 'Z':
            decrypted_text += chr(((ord(char) - ord('N') - m**2) % 13) + ord('N'))
        # Special characters, and numbers remain unchanged
        else:
            decrypted_text += char
    return decrypted_text

# to get valid integer input from user

def get_valid_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    # to get encryption parameter from user
    n = get_valid_integer("Enter the value of n: ")
    m = get_valid_integer("Enter the value of m: ")

    # Attempt to read the input file with error handling
    try:
        with open("raw_text.txt", "r") as file:
            original_text = file.read()
    except FileNotFoundError:
        print("Error: The file 'raw_text.txt' was not found.")
        exit(1)

    # Encrypt the text and save the file 
    encrypted_text = encrypt(original_text, n, m)
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)
    print("Encryption complete. The encrypted text has been saved to 'encrypted_text.txt'.")

    # Decrypt the text and check the correctness
    decrypted_text = decrypt(encrypted_text, n, m)
    if original_text == decrypted_text:
        print("Decryption successful! The decrypted text matches the original.")
    else:
        print("Decryption failed! The decrypted text does not match the original.")