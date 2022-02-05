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

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;[Back to Top](#table-of-contents)

## Layout and Features

### Site Header and Footer
* CSC logo in the top left that links to the home page
* Navigation menu is positioned centrally and includes a series of dropdown menus that allow users to filter products by type or brand, as well as to order the products by price and category.
* On the far right of the navbar are search, user and bag icons, that reveal a hidden search bar, links to the user's dashboard and their shopping bag.

* Footer displays the social media icons (for demonstration, not currently active)








