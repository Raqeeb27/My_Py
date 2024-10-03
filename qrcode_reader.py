import os

# Function to read QR code using zbarimg
def read_qr_code(image_path):
    # Command to use zbarimg to read QR code
    result = os.popen(f'zbarimg --quiet --raw {image_path}').read().strip()
    if result:
        print("QR Code Data:", result)
    else:
        print("No QR code found or image is unreadable.")

# Replace with your image file path
image_path = 'car-red.png'

# Call the function
read_qr_code(image_path)

