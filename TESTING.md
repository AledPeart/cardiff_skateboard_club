## User Stories

### ___As a new user I want to:___

* Quickly and easily understand the purpose of the site to decide if I want to stay
    * Introductory paragraph underneath the hero image introduces the site and explains its purpose
    * Hero images and site logo show the site's purpose.

![supporting screenshot](media/awaiting-image.jpeg) 

* Have clear navigation tools to move around the site to find what I am looking for easily
    * Clear navigation bar at the top each page containing links to the products.
    * Icons in the top right corner of the navbar, provide quick navigation to key areas, bag, dashboard etc
    * Numerous navigation buttons on various pages allowing users to find their way around the site
    * Back to top button on the products page allows users to return to the top of the page quickly
    * Dropdown menus used to keet screen 'clutter' to a minimum.

* Be able to browse the full range of available products to decide if there is something I wish to purchase
    * Products page allows users to browse the full range of products.
    
* Be able to filter the products by their specific categories or brands so I can browse a particular brand or category I am looking for
    * Filter buttons/dropdown menu allows users to filter the results by category or brand and find the items they are interested in quickly.

* Search for items in the shop by their name or description so I can easily find items I am looking for
    * Users are able to click the search icon on all pages and search through the product range by name and description

* Sort the items in the shop by price, name, brand and category to find items within my budget, or within my desired brand/category
    * Convenient drpdown selector on mobile and filter buttons on desktop allow users to determine the order in which the products are listed

* View individual product details to decide if a product meets my needs.
    * Users can view the specifics of individual products on the product details page.
    * Price, product details and other information presented clearly to the customer.

* See product reviews and ratings from other users, so I can buy an item with confidence.
    * On the products page users can see the average rating of each product (if it has been rated)
    * On the product details page users can see the ratings, and how many customers have recommended the product.
    * Users can also read individual review in full, and see how recent they are.

* Add items to my bag easily so that I can continue to browse the store and make further purchases.
    * On the products detail page users have the option to add items to their back with one click.
    * Users can then either continue shopping or checkout.

* View my bag, and make adjustments to it before I check out, to enjoy a convenient and pleasant experience.
    * On adding items to their bag Users receive a confirmation message with a link to view their bag.
    * Users can access the bag at any time form the navigation bar.
    * Users have the option to increase the amount of items in their bag easily.
    * Users can also remove items completely.

* Create an account easily so I cake purchases and save my details for future use.
    * Django allauth allows users to quickly and easily create an account
    * Users need only provide a username, email and password to create an account
    * When users make a subsequent purchase they have the option to save their details to their account

* Have my performed actions confirmed to me so I am sure my intended action was completed.
    * Confirmation messages shown to the users following key user actions e.g adding items to bag, signing in and out, adding items to a wishlist

### ___As a registered user I also want to:___

* Easily log in or out so I can view my personal profile
    * Users can login or ou of te site with a few simple clicks.
    * confirmation message shown to the user to confirm their action
    * Personal dashboard is linked from the users icon in the main navbar

* Be able to save and remove items to a wishlist so I can decide if I want purchase them later
    * Users are able to quickly add and remove items on their wishlist either from the product and product detail page.
    * Filled heart icon shows the user quickly if the item is in their wishlist
    * Confirmation message given to the user on adding an item to their wishlist along with an invitaion to view the wishlist.
    * Users can view their complete wishlist from the user dashboard

* View and edit my delivery and account details to ensure my details are correct
    * From the dashoard users can view their personal details and edit them.

* Leave a product review
    * Registered users who are signed in can leave a review of a chosen product
    * Users are able to give te product a rating and a reccomendation to inform their fellow customers

* Edit my reviews so that I can ensure the reviews are correct
    * Users can subsequently edit a review from the product detail page.
    * Users can only edit a review that they left

* View my purchase history so I can keep track of past orders
    * In their dashboard users can view their order history.
    * Users can see all past orders and speciic details of individual orders

* Receive confirmation emails following a purchase so I know the purchase was successful
    * Users are sent a confirmation email to their account email address following a succesful purchase.

### ___As the site owner I want:___

* Be able to add, edit or delete products to keep the store updated
    * Admin users can edit and delete products from the individual product detail page
    * Admin users can add new products in the product admin section.
* Ensure that only superusers are able to add, edit or delete products in order to maintain control of the items in the store.
    * This functionality is exclusive to superusers and has been ensured programatically in the back-end.
    * Warning messages given to users who try to force entry to restricted pages.

* Be able to edit or delete a users review in case it may be inappropriate or unfair.
    * Only Admin users are able to delete reviews again this has been ensured programatically in the back-end.
    * Admin Users can also edit any review

## Manual Functionality Testing

### Base Template
| Test Condition                                                                               | Result |
|----------------------------------------------------------------------------------------------|--------|
| CSC navbar logo links to the homepage                                                        | Pass   |
| Navbar dropdown links take users to the products                                             | Pass   |
| Each navbar link filter the products correctly                                               | Pass   |
| When not logged in, user icon links show 'register' and 'login'                              | Pass   |
| When logged in, user icon links show 'dashboard' and 'logout'                                | Pass   |
| When an admin user is logged in, user icons also show product management link                | Pass   |
| Bag icon links to the bag page                                                               | Pass   |
| Search bar icon reveals the hidden search bar                                                | Pass   |
| Search bar functions correctly and finds items by 'name'                                     | Pass   |
| Search bar functions correctly and finds items by 'description'                              | Pass   |
| If items found correct message shows No of items found for the search term                   | Pass   |
| If no items are found, correct message shows 0 items found                                   | Pass   |
| If no search criteria entered, warning message shown and user returned to the products page  | Pass   |

### Homepage 
| Test Condition                                                                   | Result |
|----------------------------------------------------------------------------------|--------|
| Shop Now' button in the introductory paragraph links to the products page        | Pass   |
| The 'see more' link in the introductory paragraph links to the about CSC section | Pass   |
| The 3 product image containers fade on hover and reveal the corect button        | Pass   |
| The 3 product imagebuttons link correctly to the relevant products               | Pass   |