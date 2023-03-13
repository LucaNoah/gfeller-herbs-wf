# GFELLER HERBS
![Screenshot Responsiveness](/media/images_readme/screenshot_responsive.PNG)

Gfeller Herbs is an online store where natural products are sold.

The purpose of the application is to offer customers the possibility to inform themselves about the offered products and to buy and order them. 

Customers can search for products or sort and categorize them using the fields in the navigation bar. If the customer wants to buy a product, a number of them can be placed in the shopping cart, then can be paid by credit card through a secure checkout procedure. The customer will be informed about orders placed by email and can view them on the website if a user account has been created before. If a user account is created, a standard delivery address can also be stored and a newsletter can be subscribed to.

Store owners/employees receive a special user account that allows them to add, edit and delete products directly from the website. Categories must be added via the admin panel and re-linked in the navigation bar.

Click [here](https://gfeller-herbs.herokuapp.com/) to live site.


## User Stories
---

GitHub Issues/Projects were used to document user stories. 
The following labels were assigned for prioritization purposes: "Must Have", "Should Have", "Could Have" and "Won't Have".
The following milestones were assignet to categorize: "User Accounts", "Administration & Management", "Purchase & Payment", "Search & Sort", "View & Navigation"

### Fulfilled User Stories
- As a Customer, I can register for a newsletter, so that I will be informed about new offers or sales.
- As a Customer, I can have a user profile, so that I have an overview of my order history, delivery address, delivery confirmation & newsletter subscriptions.
- As a Customer, I can select the quantity and size of the product, so that I can make an exact order.
- As a Customer, I can sort the displayed products, so that I get the order I am most interested in.
- As a Customer, I can change the number of each product directly in the shopping cart, so that adjustments can be made to the quantity to be purchased.
- As a Customer, I can display search requests for products, so that I can find specific products.
- As a Customer, I can register for an account, so that I can view my profile.
- As a Customer, I can be sure that my payment information is protected and safe, so that I can enter the necessary information with confidence.
- As a Customer, I can choose between different categories, so that I can view the related products.
- As a Customer, I can recover my password, so that I can recover access to my account if I forget my password.
- As a Customer, I can add products to the shopping bag, so that I have an overview of the products before checkout.
- As a Customer, I can view a list of products, so that I can select one to view and purchase.
- As a Customer, I can view the product details, so that I see what the product is exactly about.
- As a Customer, I can login or logout, so that I can access my account.
- As a Customer, I can have a simple, easy to see overview of the total costs, so that I know how much money I am about to spend.
- As a Customer, I can receive a confirmation email after a purchase, so that I can be sure my order has been received by the supplier.
- As a Customer, I can check the order before payment, so that I avoid unintentional purchases.
- As a Customer, I can easily enter my payment information without any problems, so that I keep the momentum of wanting to buy until checkout.
- As a Supplier, I can add a product, so that I can add new products to my store.
- As a Supplier, I can edit a product, so that I can modify the product attributes.
- As a Supplier, I can delete a product, so that I can delete products that are no longer offered.

### User Stories for next release
- As a Customer, I can leave reviews on products I bought, so that other customers can see my opinion about them.
- As a Customer, I can if available for the product, choose between different weights, so that can order the desired weight of a product.


## Agile Methodology
---
![Screenshot User Stories](/media/images_readme/screenshot_user_stories.PNG)

MoSCoW priority setting was used to create an agile project via GitHub Issues & GitHub Projects. 

Link to the project with live issues can be found [here](https://github.com/users/LucaNoah/projects/10).


## Wireframes
---
![Image Wireframe](/media/images_readme/wireframe.jpg)

The web application was designed on a laptop screen size. This wireframe was used.


## Existing Features
---
### - Navbar
- Logo

The logo text "Gfeller Herbs" is clickable and leads to the home page, it is located on the left edge.
- All Products

The all products tab is located to the right of the logo and opens a list with the option to view all products or sort them. If you follow one of these options, you will be taken to the product catalog.
- Categories

To the right of the all products tab are the tabs with the available super categories. With a mouse click, these show their contained categories as well as an option to all products of the contained categories and forward to the corresponding product catalog.
- Your Account

To the right of the category tabs is the "Your Account" tab. This opens a list with possible options to logout, sign-in/signup, view the user's profile and if the logged-in user is a superuser (store owner/employee) the option to add a product.
- Search Bar

The search bar sits in the middle between the Your Account tab and the shopping cart. This input field allows the user to search for and display entries in products and categories.
- Shopping Bag

The icon for the shopping cart is located at the left edge of the navigation bar. the small number to the right of it indicates how many products are currently in the shopping cart. If there is only one product in the shopping cart, the total value of the shopping cart is displayed below it.

### - Home Page
The home page of the application informs the user about the benefits and the target audience of the website. 
The customer is invited to open the product catalog via the "discover products" button or to view the operator's social media pages by clicking the icons.

### - Register
Via the navbar the user has the possibility to get to a page to register. 
Email address, username and password are required.

### - Log In
If the user has already registered, he can navigate via the navbar to the login page to log in with username/email & password.

### - Log Out
If the user is logged in, he can navigate to the logout page via the navbar.

### Add, Edit & Delete Products
If the user is logged in as superuser (store owner/employee), he has the possibility to delete or edit the product in the views of the product catalog and the product details. To add a new product, the user can navigate to the corresponding entry under the tab Your Account > Add Product. Creating and editing is done via form input an has user conformation.

### - Products Catalog
Through the button on the homepage or the navigation tab and the search input, it is possible for the user to view the product catalog. The selected products are displayed with their picture, name and price. By clicking on the picture or the name, the user can view the details of the product. Above the products, there is a selection box for sorting. If one of the super categories is displayed, the user can use the buttons below the sorting option to display the various categories.

### - Product Detail
If the user is redirected to the detailed view of a product by clicking on the image or name of a product in the product catalog, he will see the name, a large image, the description, the respective category, the price, an input field for the quantity and two buttons, one to add the respective quantity of the product to the shopping cart and one to return to the product catalog. 

### - Shopping Bag
In the shopping cart is displayed how many products are there at the time. The products in the shopping cart are displayed in tabular form. The name, quantity and price are displayed. The quantity can be changed via an input field. to remove a product, the user must enter 0 and press edit. Under the listed products, the total of the product price as well as the delivery costs and the total amount can be viewed. By 2 buttons below the user can continue to the checkout or back to the product catalog.

### - Checkout
During checkout, the user must provide personal details, delivery information and credit card details. Required fields are marked with *. Under the credit card information, the total costs with which the card is charged are displayed. Clicking on complete order initiates the payment process.

### - Checkout Success
Once the order and payment have been successfully processed, an order success page will be displayed showing the email address to which the order confirmation has been sent, a list of the products ordered and the delivery address.

### - Your Account
If the user is logged in, he can go to his personal user profile via the navigation bar. There is a list of all orders placed, an entry for the default delivery address which is automatically inserted during checkout and a selection option to subscribe to the newsletter of the store.

### - Newsletter
The newsletter of the site can be subscribed by checking the checkbox in the Your Account area. The user only has to provide his email address and update his information. There are no real newsletter mails sent at the moment!

### - Messages
For many recurring events, the user is informed about successful or failed actions via a message box that appears at the top right and only disappears when it is closed. Such events are for example: logging in, adding a product to the shopping cart, adding a product to the catalog (store owner), when emails have been sent, etc...

### - Reviews
Via the Your Account tab of the navbar, the user has the possibility to write reviews about products, provided that a user account has been created. These are displayed under the respective product in the detail view. Before the review is publicly visible, it must be approved by an admin via the admin panel. Creation has user conformation.


## Future Features
---
### - Product Weight
The possibility of adding products with weight and properly reflecting this information in the shopping cart as the order, also with adjusted prices.

### - Delete Shopping Bag Products
In the future, products in the shopping cart should also be deleted by pressing a button (like the edit button) instead by entering 0.


## Technologies Used
---
### Languages Used
- HTML5
- CSS3
- Python
- Django
- jQuery
- JavaScript

### Technologies and Programs Used
- GitHub was used for version control and planning/user stories of the agile project. 
- GitPod was used as IDE to write the actual code and push to GitHub.
- Heroku was used to deploy the application
- ElephantSQL was used as database
- Stripe was used as payment service
- Amazon Web Services S3, IAM was used to host all media an static files


## Code Validation
---
### HTML Validation
All code of all rendered HTML pages of the project was validated by the [W3C Markup Validation Service](https://validator.w3.org/). 

The errors that occur there cannot be avoided and do not affect the function of the app. They can be considered irrelevant.

### CSS Validation
All CSS files of the project have been validated by [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).

No errors raised.

### JavaScript Validation
All JavaScript files of the project have been validated by [JShint](https://jshint.com/).

The warnings that occur there cannot be avoided and do not affect the function of the app. They can be considered irrelevant.

### Python Validation
All Python files of the project were formatted by [Black Code Formatter](https://black.vercel.app/). (PEP8 Standard)

Max line lenght 80 instead of 79 (PEP8).


## Tests
---
### Lighthouse
![Screenshot Lighthouse](/media/images_readme/screenshot_lighthouse.PNG)


### Manual Tests
Tests were implied throughout the application. Further and more complex tests, especially in the checkout and bag app, will be implemented in the next development cycle.


## Bugs
---
### Weight for Products
The application has been designed and developed to give a product the option to have a weight that is also passed on to the shopping cart and order. Shortly before the release I noticed that the function is buggy, because the price is not adjusted for different weights. Therefore model field for this function was removed from the products model. The templates, the view and all other functionality is still available and will be continued. The fix for this bug is planned for the next development cycle.

![Screenshot Weight Bug](/media/images_readme/screenshot_product_weight.PNG)

![Screenshot 2 Weight Bug](/media/images_readme/screenshot_product_weight2.PNG)


## Deployment
---


## Credits
---
No Credits so far...