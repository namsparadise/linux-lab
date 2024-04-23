import sys

def caesar_cipher(message, shift):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            encoded_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encoded_message += encoded_char
    return encoded_message

def main():
    if len(sys.argv) != 2:
        print("Usage: python caesar_cipher.py <shift>")
        sys.exit(1)
    
    try:
        shift = int(sys.argv[1])
        if shift < 0 or shift >= 26:
            print("Shift must be between 0 and 25")
            sys.exit(1)
    except ValueError:
        print("Shift must be an integer")
        sys.exit(1)

    message = input("Enter your message: ").upper()
    encoded_message = caesar_cipher(message, shift)

    # Print the encoded message in blocks of five letters
    block_size = 5
    for i in range(0, len(encoded_message), block_size):
        print(encoded_message[i:i+block_size], end=" ")
        if (i+block_size) % (block_size * 10) == 0:
            print()

if __name__ == "__main__":
    main()
