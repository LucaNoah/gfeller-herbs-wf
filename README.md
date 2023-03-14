# GFELLER HERBS

![Screenshot Responsiveness](/media/images_readme/screenshot_responsive.PNG)

Gfeller Herbs is an online store where natural products are sold.

The application underlies a B2C(Business-to-Consumer) business model.

The purpose of the application is to offer customers the possibility to inform themselves about the offered products and to buy and order them.

Customers can search for products or sort and categorize them using the fields in the navigation bar. If the customer wants to buy a product, a number of them can be placed in the shopping cart, then can be paid by credit card through a secure checkout procedure. The customer will be informed about orders placed by email and can view them on the website if a user account has been created before. If a user account is created, a standard delivery address can also be stored and a newsletter can be subscribed to.

Store owners/employees receive a special user account that allows them to add, edit and delete products directly from the website. Categories must be added via the admin panel and re-linked in the navigation bar.

Click [here](https://gfeller-herbs.herokuapp.com/) to live site.

## User Stories

---

GitHub Issues/Projects were used to document user stories.
The following labels were assigned for prioritization purposes: "Must Have", "Should Have", "Could Have" and "Won't Have".
The following milestones were assigned to categorize: "User Accounts", "Administration & Management", "Purchase & Payment", "Search & Sort", "View & Navigation"
I had to recreate all user stories and issues on GitHub because after cloning my own project they were only assigned to the GitHub project and not to the GitHub repository anymore.

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
- As a Customer, I can, if available for the product, choose between different weights, so that I can order the desired weight of a product.

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

To the right of the all products tab are the tabs with the available super categories. With a mouse click, these show their contained categories, as well as an option to all products of the contained categories and forward to the corresponding product catalog.

- Your Account

To the right of the category tabs is the "Your Account" tab. This opens a list with possible options to logout, sign-in/signup, view the user's profile and if the logged-in user is a superuser (store owner/employee) the option to add a product.

- Search Bar

The search bar sits in the middle between the Your Account tab and the shopping cart. This input field allows the user to search for and display entries in products and categories.

- Shopping Bag

The icon for the shopping cart is located at the left edge of the navigation bar. The small number to the right of it indicates how many products are currently in the shopping cart. If there is only one product in the shopping cart, the total value of the shopping cart is displayed below it.

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

If the user is logged in as superuser (store owner/employee), he has the possibility to delete or edit the product in the views of the product catalog and the product details. To add a new product, the user can navigate to the corresponding entry under the tab Your Account > Add Product. Creating and editing is done via form input and has user conformation.

### - Products Catalog

Through the button on the homepage or the navigation tab and the search input, it is possible for the user to view the product catalog. The selected products are displayed with their picture, name, if one sale the old price and the actual price. By clicking on the picture or the name, the user can view the details of the product. Above the products, there is a selection box for sorting. If one of the super categories is displayed, the user can use the buttons below the sorting option to display the various categories.

### - Product Detail

If the user is redirected to the detailed view of a product by clicking on the image or name of a product in the product catalog, he will see the name, a large image, the description, the respective category, if one sale the old price and the actual price, an input field for the quantity and two buttons, one to add the respective quantity of the product to the shopping cart and one to return to the product catalog.

### - Shopping Bag

In the shopping cart is displayed how many products are there at the time. The products in the shopping cart are displayed in tabular form. The name, quantity and price are displayed. The quantity can be changed via an input field. To remove a product, the user must enter 0 and press edit. Under the listed products, the total of the product price as well as the delivery costs and the total amount can be viewed. By 2 buttons below, the user can continue to the checkout or back to the product catalog.

### - Checkout

During checkout, the user must provide personal details, delivery information and credit card details. Required fields are marked with \*. Under the credit card information, the total costs with which the card is charged are displayed. Clicking on complete order initiates the payment process.

### - Checkout Success

Once the order and payment have been successfully processed, an order success page will be displayed showing the email address to which the order confirmation has been sent, a list of the products ordered and the delivery address.

### - Your Account

If the user is logged in, he can go to his personal user profile via the navigation bar. There is a list of all orders placed, an entry for the default delivery address which is automatically inserted during checkout, and a selection option to subscribe to the newsletter of the store.

### - Newsletter

The newsletter of the site can be subscribed by checking the checkbox in the Your Account area. The user only has to provide his email address and update his information. There are no real newsletter mails sent at the moment!

### - Messages

For many recurring events, the user is informed about successful or failed actions via a message box that appears at the top right and only disappears when it is closed. Such events are for example: logging in, adding a product to the shopping cart, adding a product to the catalog (store owner), when emails have been sent, etc...

### - Product Reviews

Via the Your Account tab of the navbar, the user has the possibility to write reviews about products, provided that a user account has been created. These are displayed under the respective product in the detail view. Before the review is publicly visible, it must be approved by an admin via the admin panel. Creation has user conformation.

### - Customer Feedback

If the customer navigates to the Your Account page via the Your Account tab of the navigation bar, he will see "Do you have any suggestions for improvement or ideas?" & a button under the welcome message. This leads to a form that sends a customer feedback. The form asks the customer for a categorized reason and a text message. If the user is logged in as a superuser (store owner/employee), he will see a button below the welcome message that leads to a list of all customer feedbacks.

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
- Amazon Web Services S3, IAM was used to host all media and static files

## Code Validation

---

### - HTML Validation

All code of all rendered HTML pages of the project was validated by the [W3C Markup Validation Service](https://validator.w3.org/).

The errors that occur there cannot be avoided and do not affect the function of the app. They can be considered irrelevant.

### - CSS Validation

All CSS files of the project have been validated by [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).

No errors raised.

### - JavaScript Validation

All JavaScript files of the project have been validated by [JShint](https://jshint.com/).

The warnings that occur there cannot be avoided and do not affect the function of the app. They can be considered irrelevant.

### - Python Validation

All Python files of the project were formatted by [Black Code Formatter](https://black.vercel.app/). (PEP8 Standard)

## Tests

---

### Lighthouse

![Screenshot Lighthouse](/media/images_readme/screenshot_lighthouse.PNG)

### Manual Tests

Tests were implied throughout the application. Further and more complex tests, especially in the checkout and bag app, will be implemented in the next development cycle.

## Bugs

---

### - Weight for Products

The application has been designed and developed to give a product the option to have a weight that is also passed on to the shopping cart and order. Shortly before the release, I noticed that the function is buggy, because the price is not adjusted for different weights. Therefore, the model field for this function was removed from the Product model. The templates, the view and all other functionality is still available and will be continued. The fix for this bug is planned for the next development cycle.

![Screenshot Weight Bug](/media/images_readme/screenshot_product_weight.PNG)

![Screenshot 2 Weight Bug](/media/images_readme/screenshot_product_weight2.PNG)

## Deployment

---

The steps taken to deploy the project are described below.

### Create a Database

- Create ElephantSQL account [here](https://www.elephantsql.com/)
- Log in to access your dashboard
- Create new instance
- Select Plan (Tiny Turtle Free) & Name (Your Project Name), leave the Tags field blank
- Select Region & Datacenter near to you
- Click "Review", check your details & click “Create instance”
- Return to the ElephantSQL dashboard
- Click your created database instance name
- In the URL section, copy the database URL

### Create Heroku App

- Create Heroku account [here](https://www.heroku.com/)
- Go to your dashboard
- Click "new" to create new app
- Set name to project name and choose region next to you
- Click "Create App"
- In the new app, navigate to settings tab
- In the Config Vars section click "Reveal Config Vars"
- Create config var **DATABASE_URL**, copy in your database url from ElephantSQL as value (without quotes)

### Preparation in Gitpod

- Open your project in GidPod
- In the terminal type: **pip3 install dj_database_url==0.5.0 psycopg2**
- Update requirements.txt, type **pip3 freeze > requirements.txt** in terminal
- In settings.py **import dj_database_url** underneath the import for os
- In settings.py Database section, comment out development database and add yours

**DO NOT commit this file with your database string in the code, this is temporary so that we can connect to the new database and make migrations**

```
 # DATABASES = {
 #     'default': {
 #         'ENGINE': 'django.db.backends.sqlite3',
 #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 #     }
 # }

DATABASES = {
    'default': dj_database_url.parse('your-database-url-here')
}
```

- In the terminal type: **python3 manage.py showmigrations** to confirm you are connected to the external database
- If you are, you should see a list of all migrations, none checked off
- Type **python3 manage.py migrate** in the terminal to migrate
- Type **python3 manage.py createsuperuser** in the terminal and follow steps to create superuser
- In settings.py uncomment development database & remove external database

### Confirm Database

- On the ElephantSQL page for your database, on the left side navigation, click "BROWSER"
- Click "Table queries" button, select "auth_user"
- When you click "Execute", you should see your newly created superuser

### Deploy to Heroku

- In settings.py Database section, create if statement like this:

```
if "DATABASE_URL" in os.environ:
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
```

- In the terminal type: **pip3 install gunicorn**
- Update requirements.txt, type **pip3 freeze > requirements.txt** in terminal
- On project level, create **Procfile** (no .filenameExtension)
- In Procfile add:

```
web: gunicorn YourDjangoAppName.wsgi:application
```

- In the terminal type: **heroku login** and follow steps to login
- In the terminal type: **heroku config:set DISABLE_COLLECTSTATIC=1 --app HerokuAppName** to disable static file collection while deployment
- In settings.py set ALLOWED_HOSTS to:

```
ALLOWED_HOSTS = ['HerokuAppName.herokuapp.com', 'localhost']
```

- Add and commit changes
- Push to GitHub
- Push to Heroku with **git push heroku main**
- In Heroku app within the Deploy tab under the Deployment method section, click "GitHub"
- Choose your repo and click "Connect"
- In Automatic Deploys section enable automatic deploys, now every time you push to GitHub you also push to Heroku

## Facebook Business Page

---

![Screenshot Facebook Business Page](/media/images_readme/screenshot_fb_page.PNG)

Live Page [here](https://www.facebook.com/people/Gfeller-Herbs/100090312308848/)

## Credits

---

Code Institute - Boutique Ado, Walkthrough Project
