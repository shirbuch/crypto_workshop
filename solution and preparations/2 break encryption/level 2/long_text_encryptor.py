def clean_text(text):
    return ''.join(char.lower() for char in text if char.isalpha())


def caesar_cipher(text, shift):
    encrypted = []
    for char in text:
        shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        encrypted.append(shifted_char)
    return ''.join(encrypted)


def main():
    # Specify UTF-8 encoding to avoid UnicodeDecodeError
    with open("text.txt", "r", encoding="utf-8") as file:
        text = file.read()

    cleaned_text = clean_text(text)

    with open("cleaned_text.txt", "w") as file:
        file.write(cleaned_text)

    shift = 14
    ciphertext = caesar_cipher(cleaned_text, shift)        
    with open("ciphertext.txt", "w") as file:
        file.write(ciphertext)


if __name__ == "__main__":
    main()
