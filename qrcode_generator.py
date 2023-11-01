import qrcode
import re
import os

def generate_qrcode():
    forbidden_chars = r'[\/:*?"<>|]'

    text = input("\nEnter the text to encode as QR: ")

    error_correction = input("\nSelect error correction level (Low-L, Medium-M, Quartile-Q, High-H): ").upper()
    if error_correction not in ['L','M','Q','H']:
        print("\nInvalid Input! Please select from L, M, Q, H\nQR code creation failed.\n")
        return
    
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=getattr(qrcode.constants, f"ERROR_CORRECT_{error_correction}"),
            box_size=10,
            border=4,
        )

        qr.add_data(text)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")

        folder = input("\nEnter name of folder to save the QR code (Leave blank if current): ").strip()

        if not folder:
            folder = "./"

        if set(folder) <= {' ', '/'}:
            print("\nInvalid folder name\n")
            return     

        if not folder.endswith('/'):
            folder += '/'

        if not os.path.exists(folder):
            print(f"\nQR code creation aborted. Folder '{folder}' does not exist.")
            return

        filename = input("\nEnter the filename for the QR code image: ")
        if re.search(forbidden_chars, filename):
            print("\nInvalid filename! QR code creation failed.\nFilename can't contain \/:*?\"<>| symbols\n")
            return
        
        extension_type = input("\nEnter the image file extension for your QRCode\n 1. JPEG    2. JPG    3. PNG\n\n --> ").lower()

        if extension_type in ['1','jpeg']:
            extension = '.jpeg'
        
        elif extension_type in ['2','jpg']:
            extension = '.jpg'

        elif extension_type in ['3','png','']:
            extension = '.png'

        else:
            print("\nInvalid extension!!! Please select from the above options\n")
            return
        
        image = f"{folder}{filename}{extension}"

        counter = 1
        while os.path.exists(image):
            image = f"{folder}{filename}_{counter}{extension}"
            counter += 1

        img.save(image)

        print(f"\n\"{image[len(folder):]}\" QR code created successfully!\n")

    except:
        print("\nOops! There was an error in creating QR.\n")
        return
    
if __name__ == "__main__":
    generate_qrcode()
