# Script: tiny_url_generator.py
# Description: Shorten your Long URLs.
# Author: Mohammed Abdul Raqeeb
# Date: 08/07/2024

try:
    from colorama import Fore, Style
    import pyshorteners
except ImportError:
    print("\nERROR!\nThis script requires 'colorama' & 'pyshorteners' module.\nPlease install it using 'pip install colorama pyshorteners' and try again.")
    exit(1)

from time import sleep


# Define colors and styles
blue = Fore.BLUE
cyan = Fore.CYAN
green  = Fore.GREEN
magenta = Fore.MAGENTA
red = Fore.RED
yellow = Fore.YELLOW
bright = Style.BRIGHT
reset = Style.RESET_ALL

# Function to create tiny URL
def create_tiny_url(long_url):
    try:
        # Create a Shortener object
        s = pyshorteners.Shortener()

        # Shorten the URL using TinyURL
        short_url = s.tinyurl.short(long_url)

        return short_url

    except KeyboardInterrupt:
        print(f"\n{red}{bright}Keyboard Interrupt!\nExiting....\n{reset}")
        exit(1)
    except:
        print(f"\n{red}{bright}No Internet connection!\nExiting...\n{reset}")
        exit(1)

# Main
if __name__ == "__main__":
    print(f"\n{yellow}{bright}" + " Tiny URL Script ".center(35, '-') + f"{reset}\n")

    long_url = input(f"{cyan}{bright}Enter Your Long URL: {reset}").strip()
    if long_url == "" or len(long_url) <= 10:
        print(f"{red}{bright}\nPlease enter a valid URL\n{reset}")
        exit(1)

    print(f"\n{magenta}Creating Tiny URL....{reset}")
    tiny_url = create_tiny_url(long_url)

    print(f"\n{blue}{bright}Original URL: \"{long_url}\"{reset}")
    print(f"{green}{bright}Tiny URL: \"{tiny_url}\"{reset}")
    sleep(1)
    print(f"\n{magenta}Thank You!\nHave a nice day...\n{reset}")
