# Testing for How Till Spake Norn Irish

## Code Validators

The W3C Markup Validator and the W3C CSS Validator were used to validate the HTML and CSS files in the project and ensure there were no syntax errors. The following shows the results:

- HTML error for lack of heading in section class - fixed by changing section elements to div elements instead
- Contact - type attribute is unnecessary for javascript resources - removed
- Add Word and Edit Word - type attribute not allowed on textarea element - removed
- Dictionary and Profile - no div within ul - replace div with li element
- Home, Sign Up, Login, 404, 500 - no errors

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
  - No errors found in style.css
  - The validator displayed a warning for the use of the root colour variable names
  - Originally passed CSS through autoprefixer which displayed errors
  - Displayed error for use of colour variables in linear gradient

JS Hint was used to check JavaScript code in the project to ensure that the code complies with coding rules and that there were no syntax errors:

- [JS Hint](https://jshint.com/)
  - No errors found in script.js
  - Found one undefined and one unused variable in contact.js

PEP8 Online was used to check Python code for PEP8 requirements:

- [PEP8 Online](http://pep8online.com/)
  - Errors displaying for lines being too long
  - No errors found in app.py
  
## Testing User Stories

### First Time Visitor Goals

- As a **first time visitor**, I want to understand the main purpose of the site:
  - I've added an about section to the home page that explains the purpose of the site

- As a **first time visitor**, I want to be able to easily navigate through the site:
  - I've added a navigation bar at the top of all pages to provide links to all other pages on the site
  - I've also added external links in the footer to social media platforms and various Northern Ireland tourism sites, as well as a link to the contact form on the site

- As a **first time visitor**, I want to be able to find out which common words and phrases are used by locals in Northern Ireland:
  - I've created a dictionary page titled 'Our Wee Guide' which contains a collapsible list of all the words and phrases that have been added to the site so far
  - When a visitor clicks on a word in the list, the word will pop out with a definition of that word and an example of it being used in conversation

- As a **first time visitor**, I want to be able to sign up for an account to add my own suggestions:
  - I've added a page with a sign up form to the site to allow visitors to create an account
  - After creating an account, the user will then have the option to add a word to the dictionary

- As a **first time visitor**, I want to be able to contact the site owner

### Registered User Goals

- As a **registered user**, I want to be able to easily login and logout of my account
- As a **registered user**, I want to be able to add words or phrases to the dictionary
- As a **registered user**, I want to be able to edit any words or phrases I've added to the dictionary
- As a **registered user**, I want to be able to delete any words or phrases I've added to the dictionary
