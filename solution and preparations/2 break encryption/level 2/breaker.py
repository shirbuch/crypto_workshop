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


############ Level 1 ###########
def main():
    ciphertext = "Yrtbvizfk ilcvj"

    for shift in range(26):
        plaintext = decrypt(ciphertext, shift)
        print(f"Shift {shift}: {plaintext}")


if __name__ == "__main__":
    main()
