def encrypt(text, n, m):
    encrypted_text = ""
    for char in text:
        if 'a' <= char <= 'm':
            encrypted_char = chr(((ord(char) - ord('a') + n * m) % 13) + ord('a')) 
        elif 'n' <= char <= 'z':
            encrypted_char = chr(((ord(char) - ord('n') - (n + m)) % 13) + ord('n')) 
        elif 'A' <= char <= 'M':
            encrypted_char = chr(((ord(char) - ord('A') - n) % 13) + ord('A')) 
        elif 'N' <= char <= 'Z':
            encrypted_char = chr(((ord(char) - ord('N') + m**2) % 13) + ord('N')) 
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

def decrypt(text, n, m):
    decrypted_text = ""
    for char in text:
        if 'a' <= char <= 'm':
            decrypted_char = chr(((ord(char) - ord('a') - n * m + 13) % 13) + ord('a')) 
        elif 'n' <= char <= 'z':
            decrypted_char = chr(((ord(char) - ord('n') + (n + m) + 13) % 13) + ord('n')) 
        elif 'A' <= char <= 'M':
            decrypted_char = chr(((ord(char) - ord('A') + n + 13) % 13) + ord('A')) 
        elif 'N' <= char <= 'Z':
            decrypted_char = chr(((ord(char) - ord('N') - m**2 + 13) % 13) + ord('N'))
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text

def check_decryption(original, decrypted):
    return original == decrypted

if __name__ == "__main__":
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))

    try:
        with open("raw_text.txt", "r") as file:
            text = file.read()
    except FileNotFoundError:
        print("Error: raw_text.txt not found.")
        exit()

    encrypted_text = encrypt(text, n, m)

    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)

    decrypted_text = decrypt(encrypted_text, n, m)

    if check_decryption(text, decrypted_text):
        print("Decryption successful!")
    else:
        print("Decryption failed!")
    with open("decrypted_text.txt", "w") as file:
        file.write(decrypted_text)