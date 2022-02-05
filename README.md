# Cardiff Skatebord Club  
![CSC Mockup](static/images/am_I_responsive.png)


[View deployed site here](https://cardiff-skateboard-club.herokuapp.com/)

## __Table of Contents__
1. [Introduction](#introduction)
2. [User Stories](#user-stories)


3. [Design](#design)
4. [Wireframes](#wireframes)
5. [Layout and Features](#layout-and-features)
6. [Features left to implement](#features-left-to-implement)
7. [Database](#database)
8. [Testing](#testing)
9. [Deployment](#deployment)
10. [Technologies Used](#technologies-used)
11. [Credits](#credits)
12. [Media and Content](#media-and-content)
13. [Acknowledgements](#acknowledgements)

## Introduction
CSC or 'Cardiff Skateboard Club' was founded originally in 2008 by a group of local skateboarders, as a sort of informal club/collective, and is a way for like minded people to get together, socialize organise events and above all ride skateboards. When Cardiff's famous City Surf store closed in 2016, Cardiff Skateboard Club was able to fill that void and have been successfully running a skate shop from the centre of Cardiff ever since. The good folks at CSC were kind enough to allow me to base my MS4 project on their store, they have provided me with a selection of products complete with images, prices and descriptions as well as use of their logo and some additional decorative images. From this I have built a functioning e-commerce store, that organises and showcases the available products and allows user to view and purchase them directly.

## User stories
Here I will address the aims and goals of the store from both the perspectives of a new user, registered user and of the owner. |

### As a new user I want to
* Quickly and easily understand the purpose of the site to decide if I want to stay
* Have clear navigation tools to move around the site to find what I am looking for easily
* *Be able to prowse the full range of available products to decide if there is something I wish to purchase
* Be able to filter the products by their specific categories or brands so I can browse a particular brand or category I am looking for
* Search for items in the shop by their name or description so I can easily find items I am looking for
* Sort the items in the shop by price, name, brand and category to find items within my budget, or within my desired brand/category
* View individual product details to decide if a product meets my needs
* See product reviews and ratings from other users, so I can buy an item with confidence
* Add items to my bag easily so that I can continue to browse the store and make further purchases
* View my bag, and make adjustments to it before I check out, to enjoy a convenient and pleasant experience
* Create an account easily so I cake purchases and save my details for future use
* Have my performed actions confirmed to me so I am sure my intended action was completed
### As a registered user I also want to
* Easily log in or out so I can view my personal profile
* Be able to save and remove items to a wishlist so I can decide if I want purchase them later
* View and edit my delivery and account details to ensure my details are correct
* Edit my reviews so that I can ensure the reviews are correct
* View my purchase history so I can keep track of past orders
* Receive confirmation emails following a purchase so I know the purchase was successful
### As the site owner I want
* Be able to add, edit or delete products to keep the store updated
* Ensure that only superusers are able to add, edit or delete products in order to maintain control of the items in the store
* Be able to delete a users review in case it may be inappropriate or unfair.


## Design

### Overview

* Mobile first, user friendly design
* Intuitive layout, easy to navigate
* Users led through the store, aided by coherent and consistent navigation and signposting
* Users guided towards the store, aided to find the products they want, then guided to the checkout or back to the store to continue shopping.
* Minimal design aesthetic to ensure the site is clean and uncluttered, and not distracting or confusing for shoppers.
* Use of icons where applicable, but in keeping with a minimalist design aesthetic
* Design adheres to current norms and conventions e.g clear navigation, icons.
* Accessibility – content is accessible to as many users as possible – clear text, sufficiently contrasted to the background, ‘alt’ tags and ‘aria’ labels used appropriately.

### Colours

![Colour Pallet](media/readme-images/csc-colors.png) source www.coolers.co
* The main background of the site will be white. This is to keep things neutral and uncluttered (#FFFFFF). The product images are so colorful and vibrant that it would be distracting to have too many colours and textures vying for the user's attention, and would not enhance the user experience and potentially affect a decision to purchase.
* I have used a light grey color (#E9ECEF) to separate areas of the site areas, such as the header and footer and for forms and where there is a lot of information presented such as the 'product detail' page.
* Bootstrap cards and a shadow effect have also been used for the same purpose on the 'products' page.
* The main recurring color in the design is a bright pink (#F53DA2) which is used to inject some colour and vibrancy into the design in keeping with the skateboarding culture.
* The pink also used to subtly donate a positive action, e.g the 'buy now' button, 'add to favorites' etc. Whereas less positive actions such as 'go back', 'previous' or 'cancel' have a plain black/white aesthetic.
* Pink is also used as a hover effect on links, for review stars, and to animate the shopping bag when it contains items.

### Fonts

* The site exclusively uses [Assistant](https://fonts.google.com/specimen/Assistant) for its neutral and factual aesthetic.
* If unavailable the browser is set to default to 'Helvetica' or any sans serif.
* Text color will be plain black.

### Bootstrap

* I have used the CSS framework Bootstrap to achieve a design consistency across the site. Bootstrap's responsive breakpoints have been utilised to ensure the site layout is responsive across all viewports and devices
* I have used customised Bootstrap's modals, cards, alerts, toasts, forms and responsive navbar, throughout the site to achieve a uniformity of design that is visually pleasing and responsive.

### Buttons
* The majority of the sites button have been customised from Bootstrap, with pink 'outline' buttons used to denote forward or positive actions while black outline buttons have been used for negative or returning actions.
* All buttons have square corners for a clean uniformity, and a pink hover effect to confirm the action to the user.

### Images
* Images are predominantly of the products. Skateboarding products are incredibly vibrant and provide most of the colour for the site.
* The homepage has a 'hero' image which is overlayed with the CSC logo to quickly establish the nature of the site.
* Other general images and artwork (provided by CSC) are used to animate the homepage.

### Icons
* Remix Icon's have been used for their clean aesthetic and simplicity, to convey meaning quickly to users and to keep the design minimal. Notably they are used for the 'search' 'user profile' and 'bag' links in the navbar as well as a heart for the user favorites/wishlist,   rating stars and social media footer links.

### Wireframes
* My initial wireframes can be seen [here](media/readme-images/wireframes.png)
* The layout of the site has been largely governed by the accepted norms of a modern e-commerce store


layout and Features





### Wireframes



I have largely stuck to my initial vision for the site in terms of the layout and design. Some features were not implemented due to practical time constraints, and some things were changed following testing. I detail this further in the 'Features left to implement' and 'Testing' section.

### Site Layout

My initial layout and functionality plans can be seen [here](static/images/site_maps).
These were really useful in developing and building the site. Again not all features were implemented and I elaborate on this in the features section.

### Database 

I choose to use [MongoDB](https://www.mongodb.com/) to store and access all the data for the site.  
My database schema plans can be viewed [here](static/images/site_maps).
Initially I had planned to have two collections, one for the plant sheets and one for users, but this was expanded to three to include a categories collection in order to better group the sheets. For the purposes of this site, categories could have been part of the sheets collections, but with a view to allow future scalibility it was added as a seperate collection.  MongoDB was the right choice for my purposes as there is not a lot of relational data sets, and the flexibility it offers is key.

__Sheets Collection__
| id             	| ObjectId 	|
|----------------	|----------	|
| Category name  	| string   	|
| Image          	| string   	|
| Common Name    	| string   	|
| Botanical Name 	| string   	|
| Difficulty     	| string   	|
| Light          	| string   	|
| Water          	| string   	|
| Feed           	| string   	|
| General Info   	| string   	|
| Created By     	| string   	|

__Users Collection__
| id       	| ObjectId 	|
|----------	|----------	|
| Username 	| string   	|
| Password 	| string   	|
| Email    	| string   	|

__Categories Collection__
| id            	| ObjectId 	|
|---------------	|----------	|
| Category Name 	| string   	|


## Features
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[Back to Top](#table-of-contents)
### Site Header and Footer
* Strap at the top of the site to frame he page and to deliver a headline of the sites aim
* Site logo in the top left that links to the home page
* Navigation menu - items change dependent on whether the user is logged in
* User Logo in the top right, shows if the user is logged out, or displays their userbame if logged in
* User logo hidden on mobile navbar to reduce cluttering
* User logo links to login if the user is not logged in, or to profile page if they are
* Footer displays the social media icons (for demonstration, not currently active)
* Footer navigation menu shows key navigation items so users can easily navigate from the bottom of the page

### Home page

![Home Page](static/images/Features/features-1.png)
* Simple clean design
* Welcome paragraph, introduces the features of the site to users
* Buttons to get users on their way, buttons change depending on wheteher the user is logged in

### Login Page
* Simple clean design
* Icons used to incease accessibility
* Supporting instructive text
* Toggle button to hide/view users password
* Form validation in place to require input and in the correct format
* Backend checks that the username and password match the databse
* User feedback provided by flashed messages
* Link to register now, if the user is not signed up

### Regiser Page
* Simple clean design
* Icons used to incease accessibility
* Supporting instructive text
* Toggle button to hide/view users password
* Form validation in place to require input and in the correct format
* Confirm password field to ensure user enters their intended password
* Password hashing, to encrypt passwords for security
* Backend checks that the username is not already in use
* User feedback provided by flashed messages
* Link to login now, if the user is already signed up

### Profile Page
* Greeting message flashed to the user upon signing in
* Username displayed, with a welcome message
* User logo in the navbar becomes un-checked and the users name is added
* Users care sheets displyed in a neat column, as a summary card
* Sheets are paginated to 6 sheets per page for convenience
* pagination links at the top and nottom of the column to aid navigation
* Button to view each sheet in more detail

### View Sheet Page

![Home Page](static/images/Features/features-3.png)

* Plant image on the left of the screen
* Quick facts card shown on the right
* Plant care information summarised in succinct easily digestible fashion
* Light, water and feed information have icons to reinforce the meaning quickly and easily
* If the user is the sheet owner, edit and delete buttons are shown
* Plant name, botanical name and general care advice displayed underneath the image
* Sheet owners name displayed 
* Convenient buttons to return to the sheets page or the profile page

### Add Sheet Page
* Neat and convenient form for users to create a new sheet
* Clearly labelled input fields
* Supporting instructive text
* Form validation in place to require input, and ensure the correct format
* Dropdown boxes allow for selected user input
* Default image added as a placeholder in the URL field to ensure a URL is uploaded if user cannot provide one
* Functionality added to ensure if there is an error loading an image or if the image is not found, the default image is loaded to the site
* User feedback provided by flashed messages on completeing the form
* Backend checks prevent a user accessing this page if they are not logged in

### Edit Sheet Page

![Home Page](static/images/Features/features-4.png)

* Neat and convenient form for users to update an existing sheet
* Input fields pre-populated with the existing sheet information
* Clearly labelled input fields
* Supporting instructive text
* Form validation in place to require input, and ensure the correct format
* Dropdown boxes allow for selected user input
* Default image added as a placeholder in the URL field to ensure a URL is uploaded if user cannot provide one
* Functionality added to ensure if there is an error loading an image or if the image is not found, the default image is loaded to the site
* User feedback provided by flashed messages on completeing the form
* Option to cancel editing a sheet, user returned to the sheets page
* Backend checks prevent a user accessing this page if they are not logged in or if they do not own this sheet

### Delete Sheet functionality
* users have the option to delete their own sheets
* Backend checks prevent a user accessing this option if they are not logged in or if they do not own this sheet
* Defensive programming modal asks user to confirm they wish to delete the sheet
* Option to cancel and return to the view sheet page

### Sheets Page

![Sheets Page](static/images/Features/features-2.png)
* All sheets laid out on summary cards in a responsive layout.
* Pagination prevents the page from being cluttered 
* Pagination lnks allow user to scroll through the pages.
* Each card links to a more detailed individual plant sheet
* Search bar provided for users to search through the sheets
* Users can search by plant name and botanical name to see if the plant they want exists in the collection
* Message displayed to the users if no results returned
* Searvh results paginated 

### Other features
* Custom 404 and 500 error pages displayed if displayed if a page can't be found
* Button and menu links on the error pages so user can easily return to the site
* Logout button, logs user out of their account, and displays a confirmation message
* Flashed messages appear for 3 seconds and then dissapear 

## Features To Be Implemented

* Full backend image validation
* The ability to filter sheets by category
* Users able to 'favourite' other sheets and view their favourites under their user profile
* Superuser functionality rather than and admin account
* A more detailed user profile, that users can update e.g changing passwords
* Comments section so that users can comment on other sheets

## Testing
You can view my separate TESTING.md file [here](TESTING.md)

## Deployment
This project was developed using [Gitpod](https://www.gitpod.io/) and was committed and pushed to [Github](https://github.com/) using the following terminal commands within Gitpod:

- _git add -A_ 
- _git commit –m “commit message”_
- _git push_

The repository was then automatically deployed to Heroku. In order to do this the following steps were taken:

### Creating an env.py file

You will need to create an __env.py__ file in __Github__. This file will hold your application’s environment variables and should contain the following:
```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", " your secret key")
os.environ.setdefault("MONGO_URI", " mongodb+srv://username@clustername.gkqqu.mongodb.net/ databasename?retryWrites=true&w=majority ")
os.environ.setdefault("MONGO_DBNAME", " your database name ") 

```
Because it contains sensitive information it is important that you __env.py__ file is listed in your __.gitignore__ file to prevent it from being pushed to Github and being available publicly


### Creating Dependancies

Heroku will need to know the dependencies that are required to run your application. These will be stored in a __requirements.txt__ file. In order to create this run the following command in the github terminal
```
pip3 freeze --local > requirements.txt

```
You will then need to create a Procfile using the following command:

```
echo web: python app.py > Procfile

```
You should now have a __requirements.txt__ file which lists your dependencies, as well as __Procfile__ which needs to contain the following line

```
web: python app.py

```

* Push these 2 files to Github
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[Back to Top](#table-of-contents)

### Creating the Heroku App

* Login to your Heroku account
* From the Dashboard click on __new__ then click on __create new app__
* Name your app (this needs to be lowercase and use dashes or minuses instead of spaces
* Select the region closest to where you are based
* Click __Create app__
* Under the __Deploy__ tab select __Connet to Github__ as the __Deployment method__
* Ensure that your Github profile name is showing and add your repository name in the search field     * Click __search__ to locate your Github repository
* Once you have found your repository click __Connect__
* Before you click on __Enable Automatic Deployment__ click on the __Settings__ tab near the top of the screen
* In the __Config Vars__ section click on __Reveal Config Vars__
* You need to tell __Heroku__ which variables are required, these should match those contained in the __env.py__file, as follows:

```
Key			    Value
IP			    0.0.0.0
PORT			5000
SECRET_KEY		your secret key
MONGO_URI 		mongodb+srv://username@clustername.gkqqu.mongodb.net/databasename?retryWrites=true&w=majority	
MONGO_DBNAME	your database name
```
* Now __Enable Automatic Deployment__
* In the __Manual Deploy__ section select __Master__ from the dropdown 
* Click __Deploy Branch__
* After a few minutes you should see a message confirming __Your app was successfully deployed__
* Click __Open App__ located near the top of the page to launch your app

### Cloning this repository

In order to clone and run this project locally, you will need to follow these steps:

1. On the main repository page in __Github__, click the button to download the _Code_ (located at the top above the list of files)
2. Under the _HTTPS_ tab copy the URL for the repository
3. Open the Terminal in your preferred __IDE__.
4. Change the current working directory to the location that you would like for the new cloned directory.
5. Type _git clone_ into the terminal and then paste in the URL that you copied earlier.
6. Hit _enter_ to create your clone.
7. Remember that you will need to create an env.py file to store your variables as detailed above

Full details of these summarised steps can be found [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)


## Technologies Used

* HTML 5 
* CSS3 
* Javascript 
* [JQuery](https://jquery.com/) 
* [Popper.js](https://popper.js.org/) 
* [PIP3](https://pip.pypa.io/en/stable/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Flask-PyMongo](https://pypi.org/project/Flask-PyMongo/)
* [dnspython](https://www.dnspython.org/)
* [Flask-Paginate](https://pythonhosted.org/Flask-paginate/)
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
* [MongoDB](https://www.mongodb.com/)
* [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)
* [RandomKeyGen](https://randomkeygen.com/)
* [Responsinator](https://www.responsinator.com/)
* [Bootstrap](https://getbootstrap.com/) 
* [Git](https://git-scm.com/) 
* [Github](https://github.com/) 
* [Gitpod](https://www.gitpod.io/) 
* [Heroku](https://www.heroku.com/)
* [Balsamiq](https://balsamiq.com/) 
* [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/)
* [Google Lighthouse](https://developers.google.com/web/tools/lighthouse)
* [Google Fonts](https://fonts.google.com/) 
* [Font Awesome](https://fontawesome.com/) 
* [Photoshop](https://www.photoshop.com/en) 
* [W3C](https://validator.w3.org/) 
* [w3C](https://jigsaw.w3.org/css-validator/) 
* [JSHint](https://jshint.com/)
* [AutoPrefixer](https://autoprefixer.github.io/) 
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[Back to Top](#table-of-contents)

## Credits

* This project was created from a [Code Institute](https://codeinstitute.net/) student template
* [Bootstrap](https://getbootstrap.com/) modal, buttons, alerts, navbar and the Bootstrap Grid system was used to streamline layouts and responsive design.
* Ideas and knowledge gleamed from: 
  * [W3 Schools](https://www.w3schools.com/)
  * [CSS-Tricks](https://css-tricks.com/)
  * [Bootstrap](https://getbootstrap.com/)
  * [Stack Overflow](https://stackoverflow.com/) - (specific credits have been added as comment in the code)
  * [MDN](https://developer.mozilla.org/en-US/)
  * [Flask Paginate](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9)
  * [Flask Documents](https://flask.palletsprojects.com/en/1.1.x/)
  * Duckett, J. 2011. HTML and CSS: Design and Build Websites. John Wiley & Sons Inc.
  * Duckett, J. 2014. Javascript & JQuery. John Wiley & Sons Inc.

## Media and Content

* Fonts [Google Fonts](https://fonts.google.com/)
* Icons [Font Awesome](https://fontawesome.com/)
* Images [TheSpruce](www.thespruce.com)
* Images [Vecteezy](www.vecteezy.com)
* Images [Unsplash](https://unsplash.com/)
* Icons [Favicon](https://favicon.io/)
* Icons [Favicon](http://clipart-library.com/)
* Audio [Zapsplat](https://www.zapsplat.com/)
* Color choice [Colorhunt](https://colorhunt.co/)
               [Coolers] (https://www.coolers.co)
* Content [Gardeneres World](https://www.gardenersworld.com/)
* Content [RHS](https://www.rhs.org.uk/)
* Content [TheSpruce](www.thespruce.com)
* Content [Gardening Know How](https://www.gardeningknowhow.com/)


## Acknowledgements

* My mentor, Can Sucullu - for his knowledge, patience and guidance.
* Code institute tutors, for their help and guidance (at all hours of the day/night)
* Task manager project - Tim Nelson
* Fellow student projects - [Self-Isolution](https://github.com/Edb83/self-isolution)
                          - [CocktailHour](https://github.com/AmyOShea/MS3-Cocktail-Hour)
* Slack forums/webinars 

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[Back to Top](#table-of-contents)



### Disclaimer - This project was developed purely for educational purposes
