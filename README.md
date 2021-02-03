# How Till Spake Norn Irish

How Till Spake Norn Irish (How to Speak Northern Irish) is an online guide to all the words and phrases you're likely to hear when visiting Northern Ireland.

- **Insert Am I Responsive Screenshot**

The image above is a screenshot of the site displayed on different devices using [Am I Responsive](http://ami.responsivedesign.is/).

A demo of the website can be found here: **Add Link to Deployed Site on Heroku**

## Contents

- [**User Experience (UX)**](<#user-experience-(ux)>)
  - Project Goals
  - User Stories
    - First Time Visitor Goals
    - Registered User Goals
  - Site Owner Goals
  - Design
    - Colour Scheme
    - Typography
    - Imagery
  - Wireframes
  
- [**Database Schema**](#database-schema)

- [**Features**](#features)
  - Features that have been implemented
  - Features left to be implemented

- [**Technologies Used**](#technologies-used)
  - Languages Used
  - Frameworks, Libraries and Programs Used
  - Dependencies

- [**Testing**](#testing)

- [**Deployment**](#deployment)
  - GitHub
  - Heroku
  - Cloning the Repository

- [**Credits**](#credits)
  - Code
  - Content
  - Media
  - Acknowledgements

---

## User Experience (UX)

### Project Goals

The goal of this project is to create an online dictionary of all the different words and phrases used in Northern Ireland. Each word or phrase in the dictionary will have a definition along with an example of how the word or phrase might typically be used in conversation by locals.

The site is aimed at:

- Anyone visiting Northern Ireland for the first time
- Anyone who has visited but struggled to understand some of the words and phrases used by locals
- Anyone who has visited and was lucky enough to learn some of the words and phrases used by locals during their visit, and wants to share this with other travellers
- Anyone from Northern Ireland who wants to share some of the words and phrases they use to help anyone visiting the country

First time visitors to the site will be able to sign up for an account so they can easily add any words or phrases to the dictionary that might be missing, as well as rate the words and phrases featured in the dictionary.

### User Stories

#### First Time Visitor Goals

- As a **first time visitor**, I want to understand the main purpose of the site
- As a **first time visitor**, I want to be able to easily navigate through the site
- As a **first time visitor**, I want to be able to find out which common words and phrases are used by locals in Northern Ireland
- As a **first time visitor**, I want to be able to sign up for an account to add my own suggestions
- As a **first time visitor**, I want to be able to contact the site owner

#### Registered User Goals

- As a **registered user**, I want to be able to easily login and logout of my account
- As a **registered user**, I want to be able to add words or phrases to the dictionary
- As a **registered user**, I want to be able to edit any words or phrases I've added to the dictionary
- As a **registered user**, I want to be able to delete any words or phrases I've added to the dictionary
- As a **registered user**, I want to be able to rate any of the words or phrases featured in the dictionary

#### Site Owner Goals

- As a **site owner**, I want to provide the user with information about the purpose of the site
- As a **site owner**, I want to include a navigation bar to allow users to easily navigate to other pages on the site
- As a **site owner**, I want to provide the user with access to the dictionary without having to create an account
- As a **site owner**, I want to allow the user to easily sign up for an account to allow them to add their own suggestions to the dictionary
- As a **site owner**, I want to allow the user to easily edit and delete any words or phrases they've added to the dictionary
- As a **site owner**, I want to allow the user to rate the words and phrases featured in the dictionary
- As a **site owner**, I want all visitors and registered users to be able to easily contact me through email or social media platforms

### Design

Design, Colours and Typography based on discovernorthernireland.com

#### Colour Scheme

![Colour palette generated using coolors.co](static/images/spake-norn-irish-palette.png)
_Colour palette generated using [coolors.co](https://coolors.co)_

#### Typography

Google Fonts: Permanent Marker with suggested pairing of Open Sans

#### Imagery

#### Wireframes

The wireframes for my site were created using [Balsamiq](https://balsamiq.com/). I created wireframe for mobile, tablet and desktop devices.

Links to the wireframes can be found below. Each link contains the wireframes for mobile, tablet and desktop devices:

- [Site Map](https://github.com/KirstChat/how-till-spake-norn-irish/blob/master/static/wireframes/site-map.pdf)
- [Home](https://github.com/KirstChat/how-till-spake-norn-irish/blob/master/static/wireframes/home.pdf)
- [Dictionary](https://github.com/KirstChat/how-till-spake-norn-irish/blob/master/static/wireframes/dictionary.pdf)
- [Login](https://github.com/KirstChat/how-till-spake-norn-irish/blob/master/static/wireframes/login.pdf)
- [Profile](https://github.com/KirstChat/how-till-spake-norn-irish/blob/master/static/wireframes/profile.pdf)
- [Sign Up](https://github.com/KirstChat/how-till-spake-norn-irish/blob/master/static/wireframes/sign-up.pdf)
- [Contact](https://github.com/KirstChat/how-till-spake-norn-irish/blob/master/static/wireframes/contact-us.pdf)

[Contents](#contents)

---

## Database Schema

MongoDB Collections:

### Dictionary Collection

| Key | Value |
| :---: | :---: |
| _id: | ObjectId("unique_id") |
| word: | "string" |
| definition: | "string" |
| example: | "string" |
| added_by: | "string" |

### User Profile Collection

| Key | Value |
| :---: | :---: |
| _id: | ObjectId("unique_id") |
| first_name: | "string" |
| username: | "string" |
| password: | "string" |

[Contents](#contents)

---

## Features

### Features that have been implemented

- Responsive on all devices:
  - The site has a mobile-first design using the Materialize framework
  - Media queries **will** be added for tablet, laptop and desktop devices

- Easy to use navigation bar that links to different pages:
  - This is located at the top of all pages in the site
  - There is a collapsible side navigation menu on mobile devices which can be accessed by clicking the menu bar icon located at the top right or by swiping from the right side of the screen
  - When a user isn't logged in to their account, the following links will display on the navigation bar:
    - Home, Dictionary, Login, Sign Up, Contact Us
  - When a user is logged in to their account, the following links will display on the navigation bar:
    - Home, Dictionary, Profile, Log Out, Contact Us

- Home page with different sections:
  - An about section explaining the purpose of the site with a link to the dictionary
  - A section with button links to the login page and the sign up page

- Dictionary page
  - Features a collapsible Materialize accordion that displays all the words from the dictionary
  - When a word in the accordion is clicked, the word definition and an example is displayed

- Sign up page:
  - Features an easy to use form that requires first time visitors to enter their name, a username and a password to create an account
  - Also features a button link to the login page to allow users to sign in to their account if they already have one

- Login page:
  - Features an easy to use form that requires the user to enter their username and password to login in to their account
  - Also features a button link to the sign up page to allow first time visitors to create an account if they don't already have one

- Contact us page:
  - Features an easy to use form to allow first time visitors or users to contact the site owner to provide feedback or ask any questions

- Footer with social links:
  - This is located on all pages in the site
  - Features links to Facebook, Instagram and Twitter
  - Also features an email link to the contact us page

### Features left to be implemented

- Media Queries for tablet, laptop and desktop devices

- Dictionary
  - Filter system
    - Sort Alphabetically
    - Search for a word
  - Voting System

- Profile Page
  - Submissions (with options to edit or delete)
  - Favorites (add this later and replace with voting system?)

- Contact Page
  - Functioning Email Form

- 404 Error Page

- 500 Error Page (necessary?)

[Contents](#contents)

---

## Branches

Throughout the development process, different branches have been created to test different features and layouts which have been merged with the master branch.

Dictionary Branch:

- This branch was created to test a different layout for the dictionary template
- I initially used a grid layout with each of the words in a materialize card container which when clicked, displayed the word definition and example
- This layout caused overflow issues in some of the cards which meant that the cards couldn't have a fixed height
- To fix this issue, I tested using the materialize collapsible accordion feature to display the dictionary which fixed the height sizing issue with the original card layout

Sort Branch:

- This branch was created to test a sort function which would sort the words in the dictionary alphabetically from A-Z or Z-A
- This was achieved by creating two new routes in app.py; one route for the ascending order and another route for the descending order
- I then added a Materialize dropdown button to the dictionary template and linked each option in the dropdown the relevant route

[Contents](#contents)

---

## Technologies Used

### Languages

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)

### Frameworks, Libraries and Programs

- [Balsamiq](https://balsamiq.com/)
  - Balsamiq was used to create the wireframes for desktop, tablet and mobile during the design process.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  - Flask was the microframework use to build the application.
- [Font Awesome](https://fontawesome.com/)
  - Font Awesome was used to add various icons throughout the site.
- [Google Fonts](https://fonts.google.com/)
  - Google Fonts was used to add...
- [Git](https://git-scm.com/)
  - Git was used for version control by utilising the terminal in VS Code to commit to Git and push to GitHub. Git was also used to create branches to test new features before merging with the master branch.
- [GitHub](https://github.com/)
  - GitHub was used to store the project code that was pushed from VS Code.
- [Heroku](https://www.heroku.com/)
  - Heroku is a cloud platform that was used to deploy and run the application from the GitHub repository.
- [Materialize](https://materializecss.com/)
  - Materialize is a modern responsive CSS framework that was used to give the website a simple, responsive layout.
- [MongoDB](https://www.mongodb.com/)
  - MongoDB Atlas is a cloud database service used to create and store the database collections for the application.
- [VS Code](https://code.visualstudio.com/)
  - Visual Studio Code was the IDE used to code the project.

### Dependencies

- [autopep8](https://pypi.org/project/autopep8/)
  - A tool that automatically formats Python code to conform to the PEP 8 style guide.
- [click](https://palletsprojects.com/p/click/)
  - Composable command line interface toolkit.
- [dnspython](https://www.dnspython.org/)
  - A DNS toolkit for Python.
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
  - PyMongo support for Flask applications.
- [itsdangerous](https://palletsprojects.com/p/itsdangerous/)
  - Various helpers to pass data to untrusted environments and back
- [Jinja2](https://palletsprojects.com/p/jinja/)
  - Templating language for Python.
- [MarkupSafe](https://palletsprojects.com/p/markupsafe/)
  - Safely add untrusted strings to HTML/XML markup.
- [pymongo](https://pypi.org/project/pymongo/)
  - Python driver for MongoDB.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
  - A comprehensive WSGI web applications library.

[Contents](#contents)

---

## Testing

Further Testing information can be found in a separate document: [TESTING.md](TESTING.md)

[Contents](#contents)

## Deployment

### GitHub

This project was coded in VS Code and pushed to GitHub using the following steps:

- Create a new folder in your preferred area in your local drive
- Open the folder in VS Code and create a README.md file
- Open source control in VS Code and select **"Publish to GitHub"**
- If prompted, sign into GitHub to connect your account to VS Code if you haven't done so already
- In source control, select **"Publish to GitHub"**
- Give your repository a name and select **"Publish to GitHub Public Repository"**
- After the repository is successfully published to GitHub, you can use git bash to add, commit and push any changes to the GitHub repository
- To stage a file commit, use ```git add``` and the name of the file you want to commit
- After adding a file to commit, use ```git commit -m "add commit message"``` to specify what changes you have made to that file
- After committing a file, use ```git push``` to push all staged changes to the GitHub repository
- Before installing any additional packages, create a virtual environment - this will ensure that packages installed are only installed in the virtual environment folder: ```python3 -m venv venv```
- Ensure that the interpreter path at the bottom left of the IDE window is the virtual environment you created: ```Python 3.7.4 64-bit('venv': venv)```
- Create a **env.py** file to store environment variables: IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME
- Add the **env.py** file and the virtual environment folder to a **.gitignore** file to ensure this information isn't pushed to the repository

### Heroku

This project is hosted on Heroku - A cloud platform service that enables developers to build, run and operate applications entirely in the cloud:

- Before creating a Heroku app, open the repository in VS Code and create a requirements file that lists all the applications and dependencies required to run the application: ```pip3 freeze --local > requirements.txt```
- Create a Heroku specific file called a Procfile - this is what Heroku looks for to know which file runs the app and how to run it: ```echo web: python run.py > Procfile```
- Open [Heroku](www.heroku.com) and login to your account - or sign up for an account if you don't already have one
- Open the dashboard and select **"New"** to create a new app
- Name the app and set the region to Europe
- Open the settings tab and open **"Reveal Config Vars"**
- Add the environment variables from the **env.py** file:
  - **KEY:** IP | **VALUE:** 0.0.0.0
  - **KEY:** PORT | **VALUE:** 5000
  - **KEY:** SECRET_KEY | **VALUE:** SECRET_KEY
  - **KEY:** MONGO_URI | **VALUE:** MONGO_URI
  - **KEY:** MONGO_DBNAME | **VALUE:** MONGO_DBNAME
- To deploy the app from GitHub, open the deploy tab and change the deployment method to GitHub
- Connect to your GitHub account and search for the name of the repository to connect to
- Once connected, **"Enable Automatic Deployments"** and select the **"Master"** or **"Main"** branch to deploy
- Click the **"Deploy Branch"** button to deploy the app to Heroku

### Cloning the Repository

To clone the repository and make a local copy on your computer, follow these steps:

- Open GitHub and locate the GitHub repository: [https://github.com/KirstChat/how-till-spake-norn-irish](https://github.com/KirstChat/how-till-spake-norn-irish)
- Under the repository name, click "Code" and copy the link to clone the repository using "HTTPS"
- After copying the link, open terminal on your computer - this step can also be done in the terminal in your preferred IDE
- Change the current working directory to the location where you want the cloned directory to be saved
- Type ```git clone```, and then paste the URL: [https://github.com/KirstChat/how-till-spake-norn-irish.git](https://github.com/KirstChat/how-till-spake-norn-irish.git)
- Press Enter to create a local clone
- To then run the repository locally, install the required dependencies from the **requirements.txt** file: ```pip3 install requirements.txt```
- Run the app from your local IDE using the following command: ```python3 app.py```

[Contents](#contents)

---

## Credits

### Code

- The following video by Corey Schafer provided some guidance on creating a virtual environment in VS Code on Mac: [https://www.youtube.com/watch?v=06I63_p-2A4&t=1571s](https://www.youtube.com/watch?v=06I63_p-2A4&t=1571s)

- The following video by Pretty Printed explained how to use categories with flash messages in Flask to display messages to the user in specific places on each template: [https://www.youtube.com/watch?v=lcVdZtVvnnk](https://www.youtube.com/watch?v=lcVdZtVvnnk)

- The following function was used to capitalise the users first name: [https://www.w3schools.com/python/ref_string_capitalize.asp](https://www.w3schools.com/python/ref_string_capitalize.asp)

- The following CSS was used to add text blocks to images: [https://www.w3schools.com/howto/howto_css_image_text_blocks.asp](https://www.w3schools.com/howto/howto_css_image_text_blocks.asp)

- The following code from stack overflow was used to help add active classes to the navigation bar using Jinja: [https://stackoverflow.com/questions/55895502/dynamically-setting-active-class-with-flask-and-jinja2/55895621#55895621](https://stackoverflow.com/questions/55895502/dynamically-setting-active-class-with-flask-and-jinja2/55895621#55895621)

- The following code was used to sort the MongoDB Dictionary collection in ascending and descending order: [https://www.w3schools.com/python/python_mongodb_sort.asp](https://www.w3schools.com/python/python_mongodb_sort.asp)

- The following code was used to add a custom error page: [https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/)

- The following password regex was used for the sign up and login forms: [https://www.html5pattern.com/Passwords](https://www.html5pattern.com/Passwords)

- MongoDB count(): [https://docs.mongodb.com/manual/reference/method/db.collection.count/](https://docs.mongodb.com/manual/reference/method/db.collection.count/)

### Content

### Media

#### Images

As this project is for educational purposes, images have been used from a variety of sites as it was difficult to find the required images on free image sites. Links to these resources can be found below:

- Belfast City Hall Image from [Visit Belfast](https://visitbelfast.com/partners/belfast-city-hall/)
- Carrick-A-Rede Image from [Discover Northern Ireland](https://discovernorthernireland.com/things-to-do/carrick-a-rede-rope-bridge-p675071)
- Dark Hedges Image from [Pixabay](https://pixabay.com/photos/avenue-trees-the-dark-hedges-3464777/)
- Dunluce Castle Image from [Discover Northern Ireland](https://discovernorthernireland.com/things-to-do/dunluce-castle-medieval-irish-castle-on-the-antrim-coast-p675011)
- Giants Causeway Image from [Visit Belfast](https://visitbelfast.com/partners/giants-causeway/#&gid=1&pid=6)
- Mussenden Temple Image from [Discover Northern Ireland](https://discovernorthernireland.com/things-to-do/mussenden-temple-and-downhill-demesne-p675701)
- Open Mouth Vector Icon from [Flat Icon](https://www.flaticon.com/authors/smashicons)
- Peace Bridge Image from [Discover Northern Ireland](https://discovernorthernireland.com/things-to-do/peace-bridge-p701951)
- Titanic Museum Belfast Image from [Visit Belfast](https://visitbelfast.com/partners/titanic-belfast/)

### Acknowledgements

- A huge thanks to Igor in Tutor Support for helping me spot an error in my code that wouldn't let me render the edit_word functionality. (It's always the silly things that catch me out!)
- Thanks to the Code Institute Slack community for being an incredible bunch of people! Especially Ed B who helped someone in a thread in #data-centric-dev that was having similar issues with a delete confirmation modal deleting the first word in the collection rather than the targeted word.

[Contents](#contents)
