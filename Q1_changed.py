def encrypt(text, n, m):
    encrypted_text = ""
    for char in text:
        if 'a' <= char <= 'm':
            encrypted_text += chr(((ord(char) - ord('a') + n * m) % 13) + ord('a'))
        elif 'n' <= char <= 'z':
            encrypted_text += chr(((ord(char) - ord('n') - (n + m)) % 13) + ord('n'))
        elif 'A' <= char <= 'M':
            encrypted_text += chr(((ord(char) - ord('A') - n) % 13) + ord('A'))
        elif 'N' <= char <= 'Z':
            encrypted_text += chr(((ord(char) - ord('N') + m**2) % 13) + ord('N'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, n, m):
    decrypted_text = ""
    for char in text:
        if 'a' <= char <= 'm':
            decrypted_text += chr(((ord(char) - ord('a') - n * m) % 13) + ord('a'))
        elif 'n' <= char <= 'z':
            decrypted_text += chr(((ord(char) - ord('n') + (n + m)) % 13) + ord('n'))
        elif 'A' <= char <= 'M':
            decrypted_text += chr(((ord(char) - ord('A') + n) % 13) + ord('A'))
        elif 'N' <= char <= 'Z':
            decrypted_text += chr(((ord(char) - ord('N') - m**2) % 13) + ord('N'))
        else:
            decrypted_text += char
    return decrypted_text

def get_valid_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    n = get_valid_integer("Enter the value of n: ")
    m = get_valid_integer("Enter the value of m: ")

    # Attempt to read the input file
    try:
        with open("raw_text.txt", "r") as file:
            original_text = file.read()
    except FileNotFoundError:
        print("Error: The file 'raw_text.txt' was not found.")
        exit(1)

    # Encrypt the text
    encrypted_text = encrypt(original_text, n, m)
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)
    print("Encryption complete. The encrypted text has been saved to 'encrypted_text.txt'.")

    # Decrypt the text
    decrypted_text = decrypt(encrypted_text, n, m)
    if original_text == decrypted_text:
        print("Decryption successful! The decrypted text matches the original.")
    else:
        print("Decryption failed! The decrypted text does not match the original.")
