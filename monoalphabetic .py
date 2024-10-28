import random

def encrypt(plain_text):
    keys = []
    
    # Generate unique random keys for each character in plain_text
    while len(keys) != len(plain_text):
        x = random.randint(0, 25)  # Keys are in the range of 0-25
        if x not in keys:
            keys.append(x)
    
    cipher_text = ""
    for u in range(len(plain_text)):
        if plain_text[u] != " ":
            # Encrypt the character using the corresponding key
            t = (ord(plain_text[u]) - 65 + keys[u]) % 26 + 65  # Shift character and wrap around
            cipher_text += chr(t)
        else:
            cipher_text += plain_text[u]
    
    return cipher_text, keys

def decrypt(cipher_text, keys):
    plain_text = ""
    for i in range(len(cipher_text)):
        if cipher_text[i] != " ":
            # Decrypt the character using the corresponding key
            t = (ord(cipher_text[i]) - 65 - keys[i]) % 26 + 65  # Reverse shift and wrap around
            plain_text += chr(t)
        else:
            plain_text += cipher_text[i]
    
    return plain_text

# Input and process
plain_text = input("Enter your plain text (uppercase letters only): ").upper()
cipher_text, keys = encrypt(plain_text)
print("Cipher Text:", cipher_text)

decrypted_text = decrypt(cipher_text, keys)
print("Decrypted Text:", decrypted_text)
