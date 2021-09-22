<h1 align="center">Address Book</h1>

[View the live project here.](link to website)

<p>Address Book is a Python Program which runs in the Code Institute mock terminal on Heroku. Users can add, view and search contacts in the address book</p>

-   ### User stories

    -   #### First Time Visitor Goals
        1. As a First Time Visitor, I want to learn add a contact

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to search a contact

    -   #### Frequent User Goals
        1. As a Frequent User, I want to view all contacts

-   ### Project Use
    -   #### Project goals for intended use are:
        1. Creating a system for managing contacts.
        2. Making this system easy and effective for all users.
        3. Displaying relevant informations so users can easily navigate.

    -   #### My personal goals
        1. To build an address book application.
        2. To gain knowledge of the Python program language

-   ### Users goals 
Users should find it simple to input and store contacts. Users should also be aware their data is being stored. Users should also find it easy to search and to view all contacts.

Target audience: Users of all ages.

-   ### Technical Design
<details><summary>Flowchart</summary>
<img src="Screenshot 2021-09-22 at 08.57.53.png">
</details>

-   ### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/Python_(programming_language))

-   ### Frameworks and Tools
    1. Git
    2. GitHub
    3. Gitpod
    4. Diagrams.net

-   ### Features
    
    <details><summary>Welcome message</summary>
    <img src="Screenshot 2021-09-22 at 09.35.53.png">
    </details>
    Users are greeted with a welcome message and guide of how to proceed through the application. Users are made aware that the contacts are saved and if the pc sleeps or is shut down the data is removed from the csv. Users are then provided with a list of various options to choose from which are outlined below.
    -   #### 1. Enter a new contact
    If the user selects option number one the user will have to fill out the below information:
    -   First name
    -   Last name
    -   Age
    -   Phone number
    -   Address
    -   Email address
    -   #### 2. Display all contacts
    If the user selects option number 2, the program provides a list of all contacts. Once the user is finished with the list they can press enter to continue. This will bring the user back to the list of options.
    -   #### 3. Find a contact
    If the user selects option number 3, the user is prompted to enter a name and the application will show all results witht hat name if valid.
    -   #### 4. Exit program
    Option number 4 quits the application.

-   ### Features
PEP8 online was used to check the code for PEP8 requirements. All the code passes with no errors and no warning signs to show.

-   ### Known bugs
Everytime the computer sleeps or is shut down it clears the contacts from the contacts.csv file.

-   ### Deployment
The website was deployed using Heroku by "following these steps:
1. Use the "pip freeze -> requiremnts.txt" command in the terminal to save any libraries that need to be instaled in the file
2. Login or create a Heroku account
3. Click the "new" button in the upper right corner and select "create new app"
4. Choose an app name and your region and click "Create app"
5. Go to the "settings" tab, add the python build pack and then the node.js build pack
6. Go to the "deploy" tab and pick GitHub as a deployment method
7. Search for a repository to connect to
8. Click enable automatic deploys and then deploy branch
9. Wait for the app to build and then click on the "View" link

-   ### Credits 
The project layout and idea came from the following YouTube videos:
-   https://www.youtube.com/watch?v=PxZE0e-ePoI&t=3s
-   https://www.youtube.com/watch?v=Ok8APOzMIAQ&t=4s
-   https://www.youtube.com/watch?v=nARBRCoFGMc

-   ### Acknowledgements

-   My Mentor for continuous helpful feedback and assistance.

-   Tutor support at Code Institute and my friends from my course for their support and guidance.






