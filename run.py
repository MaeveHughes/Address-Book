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

contact_details = ""

print("Welcome to the address book program")

while contact_details != "X":
    print("Please select from the below options")
    print("A - Enter a new contact")
    print("B - Display all contacts")
    print("C - Find a contact")
    print("X - exit program")
    contact_details = input("Select option: ")

    if contact_details  == "A":
        print("Please enter your contact's details")

        first_name = input("First name = ")
        last_name = input("Last name = ")
        age = input("Age = ")
        phone_number = input("Phone number = ")

        the_contact = contact(first_name,last_name,age,phone_number)
        contacts.append(the_contact)
        print("Thank you for entering your contact's information")

    elif contact_details  == "B":
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
