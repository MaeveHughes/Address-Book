"""
Main file run.py, for Address Book by Maeve Hughes

This is the main file for a command line interface address book.

The main objective is for users to log personal contact information.
"""
#Installing google auth which will use our creds.json file to set up the authentication needed 
#to access the Google Cloud project. Also installing gspread to access and update data in the spreadsheet.

import os

#Contact class
class Contact: 
    def __init__(self, first_name, last_name, age, phone_number, address, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.address = address
        self.email = email

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f"{self.first_name} {self.last_name} : {self.age} : {self.phone_number} : {self.address}: {self.email}"

#Providing the user with different choices
#Giving the user a choice to add a contact and to print out all of the comtacts

contacts = list()

if os.path.isfile("contacts.csv"):
    with open("contacts.csv") as f:
        csv_list = f.readlines()
        for line in csv_list:
            data = line.rstrip().split(",")
            person = Contact(data[0],
                             data[1], 
                             data[2],
                             data[3],
                             data[4],
                             data[5])
            contacts.append(person)

contact_details = ""

print('Welcome to the address book program\n')
print('To use this app, hit enter after each choice.\n')
print('Attention: Contacts will be saved to the contacts.csv file.')
print('If your PC sleeps or is shut down the contacts will be removed from the csv file')


while True:
#Get functions choice
    while True:
        try:
            contact_details = input("\nPlease select from the below options:\n 1 - Enter a new contact\n 2 - Display all contacts\n 3 - Find a contact\n 4 - Exit program\n Select option: ")
            if (int(contact_details) >= 1 and int(contact_details) <= 4):
                break
            else:
                print("Please ensure the number you entered is between 1 and 3. Try again.")
        except Exception as e:
            print("Please enter a number. Try again.") 

    if contact_details == "1":
        print("\nPlease enter your contact's details\n")
        print('Your data will be saved to our database upon confirmation.\n') 
        while True:
            try:
                first_name = input("First name = ")
                import string

                allowed_alpha = string.ascii_letters + string.whitespace

                # a test name
                #name = "Mark Zumkoff"

                # gives False because of space
                #print(first_name.isalpha())

                # this test allows spaces
                if all(c in allowed_alpha for c in first_name):
                    break
                else:
                    print("Can you please check the spelling? Please do not use numbers or symbols!")
            except Exception as e:
                print("Please enter a letter. Try again.") 
        
        while True:
            try:
                last_name = input("Last name = ")
                import string

                allowed_alpha = string.ascii_letters + string.whitespace

                # a test name
                #name = "Mark Zumkoff"

                # gives False because of space
                #print(first_name.isalpha())

                # this test allows spaces
                if all(c in allowed_alpha for c in last_name):
                    break
                else:
                    print("Can you please check the spelling? Please do not use numbers or symbols!")
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
                    print("Please ensure that the phone number has 9 digits. Try again.")
            except:
                print("Please ensure you have entered a phone number. Try again.")

        address = input("Postal Address = ")

        while True:
            email = input("Email address: ")
            if ("@" in email):
                break
            else:
                print("Please ensure you have entered an email address. Try again.")

        the_contact = Contact(first_name, last_name, age, phone_number, address, email)
        contacts.append(the_contact)
        print("\nThank you for entering your contact's information")

    elif contact_details == "2":
        for Contact in contacts:
            print(Contact)
        input("\nContacts displayed above. Hit enter to continue.")

    elif contact_details == "3":
        runner = True 
        while runner:
            to_lookup = input("\nEnter contact's name to lookup: \n\n Please ensure you use capital letters if capital letters were used when adding a contact.\n \n If there is no contact available press enter again and a list with all contacts appears.\n")

            for Contact in contacts:
                
                if to_lookup in Contact.full_name():
                    print(Contact)
                    runner = False 
                

    elif contact_details.lower() == "4":
        break

# Reading and Writing Data from a CSV File in Python for the Address Book 
  
with open("contacts.csv", "w") as f:
    for contact in contacts:
        f.write(f"{Contact.first_name}, {Contact.last_name}, {Contact.age}, {Contact.phone_number}, {Contact.address}, {Contact.email}\n")

    
print("\nThank you for using the address book, we hope to see you soon")
