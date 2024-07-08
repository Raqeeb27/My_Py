# Script: tiny_url_generator.py
# Description: Shorten your Long URLs.
# Author: Mohammed Abdul Raqeeb
# Date: 08/07/2024

try:
    import pyshorteners
except ImportError:
    print("\nERROR!\nThis script requires the 'pyshorteners' module.\nPlease install it using 'pip install pyshorteners' and try again.")
    exit(1)
from time import sleep

# Function to shorten a URL
def shorten_url(long_url):
    try:
        # Create a Shortener object
        s = pyshorteners.Shortener()

        # Shorten the URL using TinyURL
        short_url = s.tinyurl.short(long_url)

        return short_url
    except:
        print("\nNo Internet connection!\nExiting...")
        exit(1)

# Example usage
if __name__ == "__main__":
    print("\n" + " URL Shortner Script ".center(30, '-') + "\n")
    long_url = input("Enter Your Long URL: ")
    print("\nProcessing...")
    short_url = shorten_url(long_url)
    print(f"\nOriginal URL: {long_url}")
    print(f"Shortened URL: {short_url}")
    sleep(1)
    print("\nThank You!\nHave a nice day...")

