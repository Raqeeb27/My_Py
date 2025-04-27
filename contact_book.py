# Script: contact_book.py
# Description: Contact Book to manage contact details.
# Author: Mohammed Abdul Raqeeb
# Date: 04/07/2024

try:
    from colorama import Fore, Style
except ImportError:
    print("\nERROR!\nThis script requires the 'colorama' module.\nPlease install it using 'pip install colorama' and try again.")
    exit(1)

from time import sleep


# Color settings
cyan = Fore.CYAN
green = Fore.GREEN
blue = Fore.BLUE
red = Fore.RED
yellow = Fore.YELLOW
bright = Style.BRIGHT
reset = Style.RESET_ALL


contacts = []


def display_menu():
    """Displays the contact book menu and processes user input."""

    print(f'{yellow}{bright}\n' + f' CONTACT BOOK '.center(40, "-") + f'{reset}\n')
    user_input = input(
        f'{cyan}1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit' + f'{blue}{bright}\n\n----> {reset}')

    if user_input == '1':
        add_contact()
    elif user_input == '2':
        view_contacts()
    elif user_input == '3':
        search_contact()
    elif user_input == '4':
        update_contact()
    elif user_input == '5':
        delete_contact()
    elif user_input == '6':
        print(f"{green}{bright}\nExiting...\nHave a nice day!{reset}")
        exit(0)
    else:
        sleep(0.2)
        print(f"{red}{bright}\nUnrecognized Input!!!{reset}")


def add_contact():
    """Adds a new contact to the contact book."""

    print(f"{yellow}{bright}\n------ Add Contact ------{reset}\n")
    name = input('Enter name: ')
    phone = input('Enter phone number: ')
    email = input('Enter email: ')
    address = input('Enter address: ')

    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })

    print(f"{green}{bright}\nContact added successfully!{reset}")


def view_contacts():
    """Displays all contacts in the contact book."""

    print(f"{yellow}{bright}\n------ Contact List ------{reset}\n")
    if not contacts:
        print(f"{red}{bright}No contacts found.{reset}")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"{green}{bright}{index}. {contact['name']} - {contact['phone']}{reset}")


def search_contact():
    """Searches for a contact by name or phone number."""

    print(f"{yellow}{bright}\n------ Search Contact ------{reset}\n")
    search_term = input('Enter name or phone number to search: ')

    found_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]

    if not found_contacts:
        print(f"{red}{bright}No contacts found.{reset}")
        return

    for contact in found_contacts:
        print(f"{green}{bright}\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}{reset}")


def update_contact():
    """Updates an existing contact's details."""

    print(f"{yellow}{bright}\n------ Update Contact ------{reset}\n")
    search_term = input('Enter name or phone number of the contact to update: ')

    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            print(f"{green}{bright}\nCurrent Details:\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}{reset}")

            contact['name'] = input('Enter new name (leave blank to keep current): ') or contact['name']
            contact['phone'] = input('Enter new phone number (leave blank to keep current): ') or contact['phone']
            contact['email'] = input('Enter new email (leave blank to keep current): ') or contact['email']
            contact['address'] = input('Enter new address (leave blank to keep current): ') or contact['address']

            print(f"{green}{bright}\nContact updated successfully!{reset}")
            return

    print(f"{red}{bright}Contact not found.{reset}")


def delete_contact():
    """Deletes a contact from the contact book."""

    print(f"{yellow}{bright}\n------ Delete Contact ------{reset}\n")
    search_term = input('Enter name or phone number of the contact to delete: ')

    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            contacts.remove(contact)
            print(f"{green}{bright}\nContact deleted successfully!{reset}")
            return

    print(f"{red}{bright}Contact not found.{reset}")


def main():
    while True:
        display_menu()
        sleep(0.5)
        user_input = input(f'{blue}\n\nDo you want to continue? (Y/n): {reset}').lower()

        if user_input in ['', 'y', 'yes']:
            continue
        elif user_input in ['n', 'no']:
            print(f"{green}{bright}\nExiting...\nHave a nice day!{reset}")
            break
        else:
            print(f"{red}\nUnrecognized Input!!!\n\nExiting...\nHave a nice day!{reset}")
            break

if __name__ == '__main__':
    main()
