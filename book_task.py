contacts = {}

def add_contact(name, phone, email, address):
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact {name} added successfully.")

def view_contacts():
    if contacts:
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}\n")
    else:
        print("No contacts found.")

def search_contact(name):
    if name in contacts:
        details = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}")
    else:
        print(f"No contact found with name {name}.")

def update_contact(name, phone=None, email=None, address=None):
    if name in contacts:
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        if address:
            contacts[name]["address"] = address
        print(f"Contact {name} updated successfully.")
    else:
        print(f"No contact found with name {name}.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"No contact found with name {name}.")

def main():
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(name)

        elif choice == "4":
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            address = input("Enter new address (leave blank to skip): ")
            update_contact(name, phone, email, address)

        elif choice == "5":
            name = input("Enter name to delete: ")
            delete_contact(name)

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
