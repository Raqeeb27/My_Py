from random import choice           # Mohammed Abdul Raqeeb
import string

# Define Morse code dictionary
morse_code_dict = {
    'A': '.-',       # A
    'B': '-...',     # B
    'C': '-.-.',     # C
    'D': '-..',      # D
    'E': '.',        # E
    'F': '..-.',     # F
    'G': '--.',      # G
    'H': '....',     # H
    'I': '..',       # I
    'J': '.---',     # J
    'K': '-.-',      # K
    'L': '.-..',     # L
    'M': '--',       # M
    'N': '-.',       # N
    'O': '---',      # O
    'P': '.--.',     # P
    'Q': '--.-',     # Q
    'R': '.-.',      # R
    'S': '...',      # S
    'T': '-',        # T
    'U': '..-',      # U
    'V': '...-',     # V
    'W': '.--',      # W
    'X': '-..-',     # X
    'Y': '-.--',     # Y
    'Z': '--..',     # Z
    '1': '.----',    # 1
    '2': '..---',    # 2
    '3': '...--',    # 3
    '4': '....-',    # 4
    '5': '.....',    # 5
    '6': '-....',    # 6
    '7': '--...',    # 7
    '8': '---..',    # 8
    '9': '----.',    # 9
    '0': '-----',    # 0
    '.': '.-.-.-',   # Period
    ',': '--..--',   # Comma
    '?': '..--..',   # Question mark
    "'": '.----.',   # Apostrophe
    '!': '-.-.--',   # Exclamation mark
    '/': '-..-.',    # Slash
    '(': '-.--.',    # Left parenthesis
    ')': '-.--.-',   # Right parenthesis
    '&': '.-...',    # Ampersand
    ':': '---...',   # Colon
    ';': '-.-.-.',   # Semicolon
    '=': '-...-',    # Equal sign
    '-': '-....-',   # Hyphen
    '_': '..--.-',   # Underscore
    '"': '.-..-.',   # Quotation marks
    '$': '...-..-',  # Dollar sign
    '@': '.--.-.',   # At symbol
    '%': '...-.',    # Percent sign
    '|': '.-..-'     # Vertical bar
}


# Function to translate text to Morse code
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        elif char == ' ':
            morse_code += '/ '  # Use slash for space in Morse code
        else:
            morse_code += char + ' '  # Take non-alphanumeric characters directly in Morse code
    return morse_code.strip()  # Strip trailing space


# Function to translate Morse code to Obfuscated_code
def obfuscate_morse_code(morse_code):
    obfuscated_code = ''
    for char in morse_code:
        if char == '.':
            obfuscated_code += choice(string.ascii_letters)
        elif char == '-':
            obfuscated_code += choice(string.digits)
        elif char == '/':
            obfuscated_code += '*'
        else:
            obfuscated_code += char
    return obfuscated_code


def deobfuscate_obfuscated_code(obfuscated_code):
    morse_code = ''
    for char in obfuscated_code:
        if char.isalpha():
            morse_code += "."
        elif char.isdigit():
            morse_code += "-"
        elif char == '*':
            morse_code += '/'
        else:
            morse_code += char
    return morse_code


# Function to translate Morse code to text
def morse_to_text(morse_code):
    text = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        if code in morse_code_dict.values():
            for char, morse in morse_code_dict.items():
                if morse == code:
                    text += char
                    break
        elif code == '/':
            text += ' '  # Add space for slash in Morse code
        else:
            text += code  # Take Morse code directly if not found in dictionary
    return text


text = input("Enter text: ")

morse = text_to_morse(text)
print("Morse Code:", morse)

obfuscated_code = obfuscate_morse_code(morse)
print("Obfuscated Code:", obfuscated_code)

deobfuscated_code = deobfuscate_obfuscated_code(obfuscated_code)
print("Deobfuscated Code:", deobfuscated_code)

decoded_text = morse_to_text(deobfuscated_code)
print("Decoded Text:", decoded_text)
