import os
import qrcode
import re


## ===========================================================================
### Functions

# Function to input QR text
def get_text():

    print("\nEnter the text to encode as QR (Press Enter \'Thrice\' to finish):\n")

    text_lines = []
    enter_pressed = 0
    
    while True:
        line = input()
        if not line:
            enter_pressed += 1
            if enter_pressed > 2:
                break
            text_lines.append("")
            continue
        else:
            enter_pressed = 0
        text_lines.append(line.rstrip())

    input_text = '\n'.join(text_lines).strip()

    if input_text.strip() == "":
        print("No Input!!!\nCan't generate QR without input text\n")
        exit(1)

    return input_text


## --------------------------------------------------------------------------
# Function to generate QR
def qr_gen(input_text, error_correction):
    qr = qrcode.QRCode(
        version=1,
        error_correction=getattr(qrcode.constants, f"ERROR_CORRECT_{error_correction}"),
        box_size=10,
        border=4,
    )

    qr.add_data(input_text)
    qr.make(fit=True)
    
    qr_image = qr.make_image(fill_color="black", back_color="white")

    return qr_image


## --------------------------------------------------------------------------
# Function to get QR Image extension type
def extension_menu():
    
    extension_type = input("\nEnter the image file extension for your QRCode\n 1. JPEG    2. JPG    3. PNG\n\n --> ").lower()

    if extension_type in ['1','jpeg']:
        extension = '.jpeg'
    
    elif extension_type in ['2','jpg']:
        extension = '.jpg'

    elif extension_type in ['3','png','']:
        extension = '.png'

    else:
        print("\nInvalid extension!!! Please select from the above options\n")
        exit(1)
    
    return extension


## --------------------------------------------------------------------------
# Function manage all QR creation tasks
def generate_qrcode():
    # Get input text from the user
    input_text = get_text()

    # Get the QR Error Correction Level
    error_correction = input("\nSelect Error Correction level (Low-L, Medium-M, Quartile-Q, High-H): ").upper()
    if error_correction not in ['L','M','Q','H']:
        print("\nInvalid Input! Please select from L, M, Q, H\nQR code creation failed.\n")
        exit(1)
    
    try:
        # Generate QR Image
        qr_image = qr_gen(input_text, error_correction)

        filename = input("\nEnter the filename for the QR code image: ")
        if re.search(FORBIDDEN_CHARS, filename):
            print("\nInvalid filename! QR code creation failed.\nFilename can't contain \/:*?\"<>| symbols\n")
            return
        
        # Get the extension type
        extension = extension_menu()
        
        qr_image_path =  os.path.join(QRCODES_DIRECTORY_PATH, f"{filename}{extension}")

        # Handle if QR Code Image has existing filename
        counter = 1
        while os.path.exists(qr_image_path):
            qr_image_path = f"{QRCODES_DIRECTORY_PATH}{filename}_{counter}{extension}"
            counter += 1

        # Save the QR Code
        qr_image.save(qr_image_path)

        return qr_image_path

    except:
        print("\nOops! There was an error in creating QR.\n")
        exit(1)


### ===========================================================================
## Main 
#
if __name__ == "__main__":

    QRCODES_DIRECTORY = 'QRCodes'
    FORBIDDEN_CHARS = r'[\/:*?"<>|]'
    QRCODES_DIRECTORY_PATH = os.path.join(os.getcwd(), QRCODES_DIRECTORY)

    os.makedirs(QRCODES_DIRECTORY_PATH, exist_ok=True)

    print()
    print(" QR Code Generator ".center(29, "-"))

    qr_image_path = generate_qrcode()

    print(f"\nQR code \"{qr_image_path[len(QRCODES_DIRECTORY_PATH):]}\" created successfully!\n")
