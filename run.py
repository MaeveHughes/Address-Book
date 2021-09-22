"""
Main file run.py, for Address Book by Maeve Hughes.
This is the main file for a command line interface address book.
The main objective is for users to log personal contact information.
"""
import os

# Contact class


class Contact:
    """
    A Class is like an object constructor,
    or a "blueprint" for creating objects.
    The __init__() function is called automatically
    every time the class is being used to create a new object.
    """
    def __init__(self, first_name, last_name, age,
                 phone_number, address, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.address = address
        self.email = email

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f"{self.first_name} {self.last_name} : {self.age} :\
             {self.phone_number} : {self.address} : {self.email}"

# Providing the user with different choices.
# Giving the user a choice to add a contact,
# display all contacts, search for a contact and delete a contact.

contacts = list()

if os.path.isfile("contacts.csv"):
    with open("contacts.csv") as f:
        csv_list = f.readlines()
        for contact_line in csv_list:
            contact_data = contact_line.rstrip().split(",")
            person = Contact([0],
                             [1],
                             [2],
                             [3],
                             [4],
                             [5])
            contacts.append(person)

contact_details = ""

print('Welcome to the address book program\n')
print('To use this app, hit enter after each choice.\n')
print('Attention: Contacts will be saved to the contacts.csv file.')
print('If your PC sleeps or is shut down the contacts')
print('will be removed from the csv file.\n')

while True:
    # Get functions choice
    while True:
        try:
            contact_details = input("Please select from the below options:\
                 \n 1 - Enter a new contact \n 2 - Display all contacts \n\
                  3 - Find a contact\n 54- Exit program\
                       \n Select option: \n")
            if (int(contact_details) >= 1 and int(contact_details) <= 4):
                break
            else:
                print("Please ensure the number you entered is ")
                print("between 1 and 5. Try again.")
        except Exception as e:
            print("Please enter a number. Try again.")

    if contact_details == "1":
        # Adds a contact to the database.
        # Keyword arguments:
        # contact -- List containing contact entry information

        print("\nPlease enter your contact's details.\n")
        print('Your data will be saved to our database upon confirmation.\n')
        while True:
            try:
                first_name = input("First name = ")
                import string

                allowed_alpha = string.ascii_letters + string.whitespace

                # a test name
                # name = "Mark Zumkoff"

                # gives False because of space
                # print(first_name.isalpha())

                # this test allows spaces
                if all(c in allowed_alpha for c in first_name):
                    break
                else:
                    print("Can you please check the spelling?")
                    print("Please do not use numbers or symbols!")
            except Exception as e:
                print("Please enter a letter. Try again.")
        while True:
            try:
                last_name = input("Last name = ")
                import string

                allowed_alpha = string.ascii_letters + string.whitespace

                # a test name
                # name = "Mark Zumkoff"

                # gives False because of space
                # print(first_name.isalpha())

                # this test allows spaces
                if all(c in allowed_alpha for c in last_name):
                    break
                else:
                    print("Can you please check the spelling?")
                    print("Please do not use numbers or symbols!")
            except Exception as e:
                print("Please enter a letter. Try again.")
        while True:
            try:
                age = input("Age = ")
                if (int(age) <= 150):
                    break
                else:
                    print("Is this a valid age?")
            except Exception as e:
                print("Please enter a number. Try again.")

        while True:
            try:
                phone_number = input("Phone number = ")
                if (len(str(phone_number)) == 9):
                    break
                else:
                    print("Please ensure that the phone number ")
                    print("has 9 digits. Try again.")
            except:
                print("Please ensure you have entered")
                print("a phone number. Try again.")

        address = input("Postal Address = ")

        while True:
            email = input("Email address = ")
            if ("@" in email):
                break
            else:
                print("Please ensure you have entered")
                print("an email address. Try again.")

        the_contact = Contact(first_name, last_name, age,
                              phone_number, address, email)
        contacts.append(the_contact)
        print("\nThank you for entering your contact's information.")

    elif contact_details == "2":
        # Displays all contacts inputted from the database.
        for person in contacts:
            print(person)
        input("\nContacts displayed above. Hit enter to continue.")

    elif contact_details == "3":
        # Creates a search bar for users to search for a contact.
        runner = True
        while runner:
            to_lookup = input("\nEnter contact's name to lookup: ")
            print("Please ensure you use capital letters if capital\
                 letters were used when adding a contact. If there is\
                      no contact available press enter again and a\
                           list with all contacts appears.")
            for person in contacts:
                if to_lookup in person.full_name():
                    print(person)
                    runner = False
# Tried to create a delete contact option however the\
# contact was only deleting temporarily. Commenting the\
# code out so I can review at a later date

    # elif contact_details == "4":
        # Removes a contact.
        # Keyword arguments:
        # Contacts have to be spelt exactly how they were inputted

        # to_lookup = input("Enter the name to delete: ")
        # for person in contacts:
        # if to_lookup in person.full_name():
        #  del person
            # print("Deleted the contact.")

    elif contact_details.lower() == "4":
        # Ends the program.
        break

# Reading and Writing Data from a CSV File in Python for the Address Book
with open("contacts.csv", "w") as f:
    for person in contacts:
        f.write(f"{person.first_name}, {person.last_name}, {person.age},\
             {person.phone_number}, {person.address},{person.email}")
print("\nThank you for using the address book, we hope to see you soon!")
