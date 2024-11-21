from PIL import Image
import os

def resize_image(input_path, output_path, width, height, output_format):
    try:
        image = Image.open(input_path)
        resized_image = image.resize((width, height))
        resized_image.save(output_path, output_format)
        print(f"\nImage resized and saved to {output_path}\n")

    except FileNotFoundError:
        print(f"\nError: Input file '{input_path}' not found.\n")
    except Exception as e:
        print(f"\nError: {str(e)}\n")

def main():
    input_path = input("\nEnter image name to resize: ")

    if not os.path.exists(input_path):
        print("\nCan't find the specified file path\n")
        return
    
    try:
        width = int(input('\nEnter the new width: '))
        height = int(input('Enter the new height: '))

        if width <= 0 or height <= 0:
            print("\nInvalid input. Width and height must be positive integers.\n")
            return

        extension = input('\nEnter the output format (e.g., PNG, JPG, JPEG): ').lower()
        if not extension:
            extension = 'png'

        output_directory = os.path.dirname(input_path)

        output_filename = f'new_{width}x{height}.{extension}'
        output_path = os.path.join(output_directory, output_filename)

        resize_image(input_path, output_path, width, height, extension)
    except ValueError:
        print("\nInvalid input. Please enter valid integers for width and height.\n")

if __name__ == "__main__":
    main()
