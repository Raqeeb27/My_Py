def caesar_cipher(text, shift):
    """
    Encrypts or decrypts a text using the Caesar cipher.

    Args:
        text: The text to be encrypted or decrypted.
        shift: The number of positions to shift the letters. Can be negative to shift backward.
    Returns:
        The encrypted or decrypted text.
    """

    result = ""
    for char in text:
        if char.isalpha():
            # Determine the starting index of the alphabet
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            # Calculate the shifted index
            shifted_index = (ord(char) - start + shift) % 26 + start

            # Convert the index back to a character
            result += chr(shifted_index)
        else:
            result += char
    return result

print(" Caesar Cipher ".center(25,"-") + "\n")
text = input("Enter the CipherText or PlainText: ")
try:
    shift_value = int(input("Enter the shift value (Negative if reverse shift): "))
except:
    print("\n\nInvalid Input!\n\nEnter integer shift value!\nExiting...")
    exit(1)
    
result_text = caesar_cipher(text, shift_value)

print("\nOriginal text:", text)
print("Encrypted text:", result_text)