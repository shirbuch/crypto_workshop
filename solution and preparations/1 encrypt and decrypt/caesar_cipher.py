def encrypt(message, shift):
    ciphertext = ""
    for char in message:
        if char.isalpha():
            shifted_char = char.lower()  # Work with lowercase letters
            shifted_char = chr(((ord(shifted_char) - ord('a') + shift) % 26) + ord('a'))

            # Preserve original case
            if char.isupper():
                shifted_char = shifted_char.upper()

            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext


def decrypt(ciphertext, shift):
    return encrypt(ciphertext, -shift)


def main():
    with open("message.txt", "r") as file:
        message = file.read()

    print(f"message:\n{message}\n")
    shift = 17
    ciphertext = encrypt(message, shift)
    print(f"ciphertext (shift of {shift}):\n{ciphertext}\n")
    plaintext = decrypt(ciphertext, shift)
    print(f"plaintext:\n{plaintext}\n")


if __name__ == "__main__":
    main()
