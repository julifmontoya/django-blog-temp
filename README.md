
# Travel Blog Django 4.0 Templete

## 1. Definition Problem

The objective is to design a travel blog application that allows users to create, edit, and delete their own posts. Each user should have exclusive access to their own posts, without being able to view publications made by other users. Additionally, the application should allow all users, regardless of login status, to view and comment posts created by any user.

## 2. Project Goal
Create a platform where travelers can share their journeys, insights, and recommendations, as well as leave comments on each post. The platform should prioritize easy navigation and be responsive across various devices.

## 3. Technologies I've used
- Balsamiq was used to create the wireframes during the design process
- GitHub was used to store the project.
- PostgreSQL was used as the relational database.
- Django is the framework used to write models, classes and templates .
- Pep8 was used for formatting and error-checking Python code.
- Crispyforms were used to display forms.
- Google fonts are used to add fonts for aesthetic and UX purposes
- Responsive CSS was implemented using Bootstrap 5.


## 4. Database Design
[Database schema](https://github.com/julifmontoya/django-blog-temp/blob/master/doc/3_DB_Schema.jpg)

## 5. Agile Methodology
All functionality and development of this project were managed using [Trello](https://github.com/julifmontoya/django-blog-temp/blob/master/doc/3_DB_Schema.jpg)

## 6. User stories
###  6.1 Register
As a site user, I want to be able to register on the application in order to publish or update posts. [Wireframe](https://github.com/julifmontoya/django-blog-temp/blob/master/doc/6_1_Register.png)

###  6.2 Login
As a site user, I want to be able to log in to the application in order to publish or update posts. [Wireframe](https://github.com/julifmontoya/django-blog-temp/blob/master/doc/6_2_Login.png)

###  6.3 Post List for Non-Logged-in Users
As a site user, I want to be able to log in to the application in order to publish or update posts. [Wireframe](https://github.com/julifmontoya/django-blog-temp/blob/master/doc/6_3_Post%20List%20Non-Logged-in.png)

###  6.4 Post List for Logged-in Users
As a site user, I want to be able to view the posts that I create for update or view the post. [Wireframe](https://github.com/julifmontoya/django-blog-temp/blob/master/doc/6_4_FIlter%20Category.png)

###  6.5 Filter Category for Non-Logged-in Users
As a site user, I want the ability to filter posts based on different categories.
[Wireframe](https://github.com/julifmontoya/django-blog-temp/blob/master/doc/6_5_Comments.png)

###  6.6 Comments for Non-Logged-in Users
As a site user, I want the ability to leave comments on each post. [Wireframe](https://github.com/julifmontoya/django-blog-temp/blob/master/doc/6_6_Post%20List%20for%20Logged-in.png)

### 6.7 Create Post
As a site user, I want to be able to create a post to publish on the blog. [Wireframe](https://github.com/julifmontoya/django-blog-temp/blob/master/doc/6_7_Create%20Post.png)

### 6.8 Update Post
As a site user, I want to be able to edit a post and make changes to its fields.
[Wireframe](https://github.com/julifmontoya/django-blog-temp/blob/master/doc/6_8_Update.png.png)

### 6.9 Delete Post
As a site user, I want to be able to delete a post so that it no longer appears on the blog. [Wireframe](https://github.com/julifmontoya/django-blog-temp/blob/master/doc/6_9_Delete%20Confirm.png)

## 7. Design Structure
### 7.1 Font
Google font Lato was chosen with to be used across the entire site.

### 7.2 Colors
| Use           | Hex     | Color                                                    |
| ------------- | ------- | -------------------------------------------------------- |
| Background    | #f8f9fa | ![#f8f9fa](https://via.placeholder.com/10/f8f9fa?text=+) |
| Cards         | #fff    | ![#fff](https://via.placeholder.com/10/fff?text=+)       |
| NavBar        | #343a40 | ![#343a40](https://via.placeholder.com/10/343a40?text=+) |
| Footer        | #424649 | ![#424649](https://via.placeholder.com/10/424649?text=+) |
| Btn Primary   | #6c757d | ![#6c757d](https://via.placeholder.com/10/6c757d?text=+) |
| Inputs        | #ccc    | ![#ccc](https://via.placeholder.com/10/ccc?text=+)       |

### 7.3 Navigation
- Navbar is on top to facilitate users to navigate through pages easily
- Add, Edit/Update are straightforward forms to allow users to use the features without issues

## 8. Results
[Link to the project](https://django-blog-temp.vercel.app/)

###  8.1 [Register]()

###  8.2 [Login]()

###  8.3 [Post List for Non-Logged-in Users]()

###  8.4 [Post List for Logged-in Users]()

###  8.5 [Filter Category for Non-Logged-in Users]()

###  8.6 [Comments for Non-Logged-in Users]()

### 8.7 [Create Post]()

### 8.8 [Update Post]()

### 8.9 [Delete Post]()

## 9. Testing
### 9.1 Lighthouse report
- Home page [Result](https://github.com/julifmontoya/django-blog-temp/blob/master/doc/9_1_Home.JPG)
- Login page [Result](https://github.com/julifmontoya/django-blog-temp/blob/master/doc/9_1_Login.JPG)

### 9.2 WAVE Webaim Accessibility testing
The WAVE tool was used to test all pages on the app. Some errors repeat over each page tested, these were due to the social links not having the link. 

- Home page WAVE [Result](https://github.com/julifmontoya/django-blog-temp/blob/master/doc/9_2_Home.JPG)
- Login page WAVE [Result](https://github.com/julifmontoya/django-blog-temp/blob/master/doc/9_2_Login.JPG)
- Register page WAVE [Result](https://github.com/julifmontoya/django-blog-temp/blob/master/doc/9_2_Register.JPG)

### 9.3 CSS Validator results
I use https://jigsaw.w3.org/css-validator/validator.html.en option Validate by direct input the style.css. [Result](https://github.com/julifmontoya/django-blog-temp/blob/master/doc/9_3_CssChecker.JPG)

### 9.4 HTML Validation
I use https://validator.w3.org/ option Validate by URI to test html. [Result](https://github.com/julifmontoya/django-blog-temp/blob/master/doc/9_4_HtmlChecker.JPG)

### 9.5 Manual Testing
During the manual testing phase, I examined the user inputs and functionality of the website. My objective was to compare the feedback and results obtained from testing against the expected outcomes. Any unexpected outputs or outcomes encountered were promptly addressed and resolved.

#### Desktop Testing:
I thoroughly tested all aspects of the site on this browser, and I am pleased to report that everything functions flawlessly. Pages load swiftly, and all features, including CRUD operations, user authentication (login/logout), register process, trips addition, and category filter work without any issues.

#### Mobile Testing:
I conducted thorough testing on three different mobile devices: Apple iPhone 11, Samsung S20FE, and Samsung S7 tablet. The website showcased excellent responsiveness and adaptability across various devices. The site performed seamlessly on Apple's Safari browser as well.

## 10. Features left to implement
I would like to: 
-	Add a search bar to find travel posts
-	Include a user profile page allowing users to edit, or delete their profile
-	Add more fields to the blog like most likes

## 11. Deployment
The site was deployed using Heroku, following the steps offered by Codeinstitute.
- Using my Heroku account 
- Create a new app whilst logged in
- Connect your GitHub repository via "Connect to GitHub"
- Set up your config vars.
- Enable either "Automatic Deploy”

## 12. Credits and references
Travel blog images was taken from https://unsplash.com/
