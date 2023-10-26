import qrcode
import re

forbidden_chars = r'[\/:*?"<>|]'

def validate():
    text = input("\nEnter the text to encode as QR: ")
    
    error_correction = input("\nSelect error correction level (Low-L, Medium-M, Quartile-Q, High-H): ").upper()

    if error_correction not in ['L','M','Q','H']:
        print("\nInvalid Input! Please select from L, M, Q, H\nQR code creation failed.\n")
        exit()
    
    filename = input("\nEnter the filename for the QR code image: ")
    if re.search(forbidden_chars, filename):
        print("\nInvalid filename! QR code creation failed.\nFilename can't contain \/:*?\"<>| symbols\n")
        exit()
    
    extension = input("\nEnter the image file extension for your QRCode (.jpeg, .jpg, .png): ")

    if extension not in ['.jpeg','.jpg','.png']:
        print("\nInvalid extension!!! Please select from .jpeg, .jpg, .png\n")
        exit()
    
    return [error_correction, text, filename, extension]

details = validate()

def generate_qrcode(details):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=getattr(qrcode.constants, f"ERROR_CORRECT_{details[0]}"),
            box_size=10,
            border=4,
        )

        qr.add_data(details[1])
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        image = "QRCodes/" + details[2] + details[3]
        img.save(image)
    except:
        print("\nOops! There was an error in creating QR.\n")
        exit()

generate_qrcode(details)

print("\nQR code created successfully!\n")
