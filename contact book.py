def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    # Store phone and email inside a list as the dictionary value
    contacts[name] = [phone, email]
    print(f"Contact '{name}' added successfully!\n")

def search_contact(contacts):
    name = input("Enter the name to search: ").strip()
    if name in contacts:
        phone, email = contacts[name]
        print(f"\nContact Found:")
        print(f"Name  : {name}")
        print(f"Phone : {phone}")
        print(f"Email : {email}\n")
    else:
        print(f"\nContact '{name}' does not exist in the contact book.\n")

def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found in the contact book.\n")
    else:
        print("\n--- Saved Contacts ---")
        for name, details in contacts.items():
            print(f"Name  : {name}")
            print(f"Phone : {details[0]}")  # Fixed: Accessing index 0 for phone
            print(f"Email : {details[1]}")  # Fixed: Accessing index 1 for email
            print("-" * 22)
        print()

def main():
    contacts = {}
    
    while True:
        print("=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. View Contacts")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            view_contacts(contacts)
        elif choice == '4':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 4.\n")

if __name__ == "__main__":
    main()
