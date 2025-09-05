def encrypt_text(shift1, shift2):
    def shift_char(c):
        if c.islower():
            if 'a' <= c <= 'm':
                # Shift forward by shift1 * shift2
                shifted = chr((ord(c) - ord('a') + shift1 * shift2) % 26 + ord('a'))
            else:
                # Shift backward by shift1 + shift2
                shifted = chr((ord(c) - ord('a') - (shift1 + shift2)) % 26 + ord('a'))
            return shifted
        elif c.isupper():
            if 'A' <= c <= 'M':
                # Shift backward by shift1
                shifted = chr((ord(c) - ord('A') - shift1) % 26 + ord('A'))
            else:
                # Shift forward by shift2 squared
                shifted = chr((ord(c) - ord('A') + shift2 ** 2) % 26 + ord('A'))
            return shifted
        else:
            # Other characters remain unchanged
            return c

    with open("raw_text.txt", "r") as infile:
        text = infile.read()

    encrypted_text = ''.join(shift_char(c) for c in text)

    with open("encrypted_text.txt", "w") as outfile:
        outfile.write(encrypted_text)


def decrypt_text(shift1, shift2):
    def unshift_char(c):
        if c.islower():
            if 'a' <= c <= 'm':
                # Reverse shift forward by shift1 * shift2
                shifted = chr((ord(c) - ord('a') - shift1 * shift2) % 26 + ord('a'))
            else:
                # Reverse shift backward by shift1 + shift2
                shifted = chr((ord(c) - ord('a') + (shift1 + shift2)) % 26 + ord('a'))
            return shifted
        elif c.isupper():
            if 'A' <= c <= 'M':
                # Reverse shift backward by shift1
                shifted = chr((ord(c) - ord('A') + shift1) % 26 + ord('A'))
            else:
                # Reverse shift forward by shift2 squared
                shifted = chr((ord(c) - ord('A') - shift2 ** 2) % 26 + ord('A'))
            return shifted
        else:
            return c

    with open("encrypted_text.txt", "r") as infile:
        text = infile.read()

    decrypted_text = ''.join(unshift_char(c) for c in text)

    with open("decrypted_text.txt", "w") as outfile:
        outfile.write(decrypted_text)


def verify_decryption():
    with open("raw_text.txt", "r") as original_file, open("decrypted_text.txt", "r") as decrypted_file:
        original = original_file.read()
        decrypted = decrypted_file.read()

    if original == decrypted:
        print("Decryption successful: Decrypted text matches the original.")
    else:
        print("Decryption failed: Decrypted text does not match the original.")


def main():
    shift1 = int(input("Enter shift1 value: "))
    shift2 = int(input("Enter shift2 value: "))

    encrypt_text(shift1, shift2)
    decrypt_text(shift1, shift2)
    verify_decryption()


if __name__ == "__main__":
    main()
