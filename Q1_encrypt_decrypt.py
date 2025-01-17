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
   def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter an integer.")

# With this:
n = get_valid_integer("Enter the value of n: ")
m = get_valid_integer("Enter the value of m: ")

# Define content with a default value to avoid NameError
content = ""

try:
    # Attempt to open the file and read its content
    with open("raw_text.txt", "r") as file:
        content = file.read()
        print("File content successfully read.")
except FileNotFoundError:
    # Handle the error if the file doesn't exist
    print("Error: The file 'raw_text.txt' was not found.")

# Check if content has been successfully read
if content:
    # Proceed with encryption only if content is not empty
    encrypted_text = encrypt(content, n, m)

    # Write the encrypted content to a new file
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)
    print("Encryption complete. The encrypted text has been saved to 'encrypted_text.txt'.")
else:
    print("No content to encrypt.")
