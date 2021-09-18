"""
Main file run.py, for Address Book by Maeve Hughes

This is the main file for a command line interface address book.

The main objective is for users to log personal contact information.
"""

import os

#Contact class
class contact: 
    def __init__(self, first_name, last_name, age, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f"{self.first_name} {self.last_name} : {self.age} : {self.phone_number}"

#Providing the user with different choices
#Giving the user a choice to add a contact and to print out all of the comtacts

contacts = list()

if os.path.isfile("contacts.csv"):
    with open("contacts.csv") as f:
        csv_list = f.readlines()
        for line in csv_list:
            data = line.rstrip().split(",")
            person = contact(data[0],
                             data[1], 
                             data[2],
                             data[3])
            contacts.append(person)

contact_details = ""

print('Welcome to the address book program\n')
print('To use this app, hit enter after each choice.\n')
print('Attention: using the comma button when entering entering a name')
print('in this application causes the app to malfunction. We are aware of')
print('this and are working on it. Thank you for your patience.\n')

while contact_details != "X":
    print("Please select from the below options\n")
    print("Please use capital letters\n")
    print("A - Enter a new contact")
    print("B - Display all contacts")
    print("C - Find a contact")
    print("X - exit program")
    contact_details = input("\nSelect option: ")

    if contact_details == "A":
        print("\nPlease enter your contact's details\n")
        print('Your data will be saved to our database upon confirmation.\n')

        first_name = input("First name = ")
        last_name = input("Last name = ")
        age = input("Age = ")
        phone_number = input("Phone number = ")

        the_contact = contact(first_name, last_name, age, phone_number)
        contacts.append(the_contact)
        print("Thank you for entering your contact's information\n")
        print("Please select from the below options/n")
        print("Please use capital letters\n")

    elif contact_details == "B":
        for contact in contacts:
            print(contact)
        input("Contacts displayed. Hit enter to continue.")

    elif contact_details == "C":
        to_lookup = input("Enter contact's name to lookup\n")
        for contact in contacts:
            if to_lookup in contact.full_name():
                print(contact)

    elif contact_details.lower() == "X":
        break

    # Reading and Writing Data from a CSV File in Python for the Address Book 
   
with open("contacts.csv", "w") as f:
    for contact in contacts:
        f.write(f"{contact.first_name},{contact.last_name},{contact.age},{contact.phone_number}\n")

print("Thank you for using the address book, we hope to see you soon")
