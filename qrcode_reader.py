import os
import sys

# Function to read a single QR code using zbarimg
def read_qr_code(image_path, save_to_file=False, output_file=None):
    # Check if the image file exists
    if not os.path.isfile(image_path):
        print(f"Error: File '{image_path}' does not exist.")
        return

    # Run zbarimg to decode the QR code
    result = os.popen(f'zbarimg --quiet --raw {image_path}').read().strip()

    if result:
        print("QR Code Data:", result)

        # Save to file if specified
        if save_to_file and output_file:
            with open(output_file, 'w') as file:
                file.write(result + '\n')
            print(f"QR code data saved to {output_file}")
    else:
        print("No QR code found or the image is unreadable.")

# Command-line interface for the script
if __name__ == '__main__':
    # Check for image path argument
    if len(sys.argv) < 2:
        print("Usage: python qr_reader.py <image_path> [output_file]")
        sys.exit(1)

    # Get the image path from the first argument
    image_path = sys.argv[1]

    # Optional: Output file to save QR code data
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    # Call the function to read the QR code
    read_qr_code(image_path, save_to_file=bool(output_file), output_file=output_file)

