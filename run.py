"""
Main file run.py, for Address Book by Maeve Hughes

This is the main file for a command line interface address book.

The main objective is for users to log personal contact information.
"""

#Contact class
class contact: 
    def __init__(self, first_name, last_name, age, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number

    def full_name(self):
        print(f"{first_name} {last_name}")

    def __str__(self):
        return_str = "---------\n"
        return_str += f"{self.first_name}\n"
        return_str += f"{self.last_name}\n"
        return_str += f"{self.age}\n"
        return_str += f"{self.phone_number}\n"
        return_str += "---------\n"
        return return_str

#Giving the user the ability to add a contact to the address book
print("Welcome to the address book program")
print("Please enter your contact's details")

first_name = input("First name = ")
last_name = input("Last name = ")
age = input("Age = ")
phone_number = input("Phone number = ")

print("Thank you for enterting your contact's information")

#Printing the full persons name by using the "the_contact.full_name" method to print that out into the terminal
the_contact = contact(first_name,last_name,age,phone_number)
print(the_contact)