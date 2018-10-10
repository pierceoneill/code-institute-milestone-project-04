# Daddy Does Dinner - Cookbook - Code Institute Milestone Project 04


The brief was to create a web application that allows users to store and easily access cooking recipes. The recipes are to be stored in a database which can be filtered by a user on the website using the categories. 
It is a data-driven application, and the target audience is any user but targeted towards stay at home moms and dads.
 
## UX
 
This application is intended for use by all but as a stay at home dad who is busy with study, school runs, extra curricular activities, coming up with dinners for my children that they will eat can be a challenge.
I designed the site so that users can share recipes and rate them accordingly.

User Stories:
- As a single mother, I would like an easy reference for meals so I can organize dinner on the train home.
- As a stay at home dad with limited cooking skilled, I would love to find recipes that are simple and easy to cook for my family.
- As a student away from home for the first time, I am looking for somewhere to get easy recipes.

WireFrames

Below are the wireframes for the project.

#### Home

![Screenshot](/Wireframes/home.png)

#### Recipes

![Screenshot](/Wireframes/recipes.png)

#### Add Recipes

![Screenshot](/Wireframes/add_recipe.png)

#### Recipe Detail

![Screenshot](/Wireframes/recipe_detail.png)

#### Dashboard

![Screenshot](/Wireframes/dashboard.png)

#### Contact Form

![Screenshot](/Wireframes/contact_form.png)

### Layout

The layout used the [Materialize CSS Parallax template](https://materializecss.com/templates/parallax-template/preview.html) which I modified to suit my own requirements. 

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 

### Existing Features
The following section describes the front-end features in this project.

1. **Navbar** - Consists of the DADDY DOES DINNER logo which returns the user to the "Home" page of the application. There is also links to the "Recipes", "My Recipes", "Login / Dashboard" and Contact forms. The navbar will appear on all pages.
2. **Home** - The home page consists of 4 sample recipes along with some information on contacting the webmaster and a link to the contact us page of the site.
3. **All Recipes** - Directs the user to the "All Recipes" page which displays **ALL** recipes from **ALL** users which have been entered on the site. The user can then filter or browse through the recipes. The can view more information on each recipe by selectign the "See Recipe" link which delivers the user to the "Recipe Detail" page.
4. **Recipe Detail** - Provides users with the recipe details containg a recipe name, description, image (if available), flavour, meal type, base ingredients, ingredients, instructions, author and date posted.
5. **My Recipes** - Provides the user with the recipes that they have added themselves. The user's recipes can be edited and deleted by using the buttons displayed under the recipes.
6. **Login/Dashboard** - When first selected the user will be prompted to create a username to login to the application so that they can add recipes to the database. Once logged in the user will be presented with their dashboard which provides a count of their recipes, along with 3 data charts depicting the number of base ingredients, meal types and food flavours associated with the recipes which have been added.
7. **Contact** - Delivers the user to the contact page. This page displays a blank form, which allows users to contact the website developers to offer feedback and suggestions (not currently wired up to an email address as this is not a real business). Their are also 4 social media buttons so that the user may interact on social networks. (Links NOT LIVE current social media pages for this project as this is not a real business)
8. **Social Links** - Provides users with links to the website social media pages and also shortcuts to the "All Recipes" & "My Recipes" pages.(Links NOT LIVE current social media pages for this project as this is not a real business).

### Features to Implement
1. **Dat Added** I was unable to get this function to work reliably. It would only produce the date of creation.
1. **Videos** - The ability to attach videos to the recipes so that the users can upload video instructions to the associated recipe.
2. **Blog** - Add a feature to include a blog page so that the company can bring intersting news, updates and stories to users of the applications.

## Technologies Used

- [Cloud 9 IDE](https://aws.amazon.com/cloud9/)
    - This project used **Cloud 9**, an online integrated development environment, to construct the code end to end.
- [Bootstrap](https://getbootstrap.com/)
    - This project used **Bootstrap**, a library of website themes. The [Materialize CSS Parallax template](https://materializecss.com/templates/parallax-template/preview.html), was used for this project.
    
- [Flask](http://flask.pocoo.org/)
    - This project uses **Flask**, a Python micro-framework. It is classified as a microframework because it does not require particular tools or libraries.
- [mLab](https://mlab.com/)
    - This project uses **mLab**, a fully managed cloud database service that hosts MongoDB databases. mLab runs on cloud providers Amazon, Google, and Microsoft Azure, and has partnered with platform-as-a-service providers. The developer used an mLab sandbox DB, which is for learning and prototyping. Json value pairs were added into the mLab document to align with the recipe wireframe. For example, 'Recipe_Title: Title', is the json value pair within the mLab database for the Recipe Title.
- [MongoDB](https://www.mongodb.com/)
    - This project uses **mongoDB**, a free and open-source cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with schemata.
- [Jinga](http://jinja.pocoo.org/)
    - This project uses **Jinja**, a template engine for Python, jinja code is included within the curly brackets.
- [Python](https://www.python.org/)
    - This project uses **Python**, an interpreted high-level programming language for general-purpose programming and used to write the logic of this game, which is included within `.py` files.
- [HTML](https://en.wikipedia.org/wiki/HTML)
    - This project uses **HTML**, the standard mark-up language used to build website layout, which is included within the `.html` files.
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - This project uses **CSS**, a style sheet language, used to add styling to a website. The `custom.css` file was added to this project, to add additional styling on top of the Bootstrap template.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - This project uses **JavaScript**, an object-oriented programming language used to create interactive effects within web browsers. JavaScript within this project was included with the Bootstrap template.
- [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools/)
    - This project uses **Chrome Dev Tools**, a set of web developer tools, to continuously test and inspect that the web pages are rendering as intended within the browser.
- [GitHub](https://github.com/)
    - This project uses **GitHub**, a web hosting service, for version control and final project backup.
- [Heroku](https://www.heroku.com/home)
    - This project uses **Heroku**, a web hosting service that supports Python applications, for final project deployment.
- [Font Awesome](https://fontawesome.com)
    - This project uses **Font Awesome**, vector icons and social logos on the website.
- [Materialize CSS](https://materializecss.com)
   - Created and designed by Google, Material Design is a design language that combines the classic principles of successful design along with innovation and technology. Google's goal is to develop a system of design that allows for a unified user experience across all their products on any platform

## Testing

### Manual Testing

1. Add Recipe Page:
    1. Go to the "Add Recipe" page.
    2. Try to submit the empty form and verify that the recipe will not submit without a RECIPE NAME.
    3. Try to submit the form without description and verify that the recipe will not submit without a RECIPE DESCRIPTION.
    4. Try to submit the form without **Vegan** selected and verify that an error message appears.

2. My Recipes Page
    1. Go to the "My Recipes" page.
    2. Try to Delete a recipe and verify that an error message appears stating that if the user goes ahead the recipe will be permanently deleted.

3. My Dashboard
    1. Once logged in, go to the Dashboard page.
    2. Verify that the "Recipe Count" box is displaying the correct number of recipes.
    3. Verify that the 3 graphs for "Base Ingredient", "Meal Type" & "Flavour" are displaying correctly.


4. Ratings
    1. The Average Rating field does not update correctly

5. Edit A Recipe
    1. when editing a recipe a new recipe will create instead of modifying the existing file.

## Responsive Testing 

   The app was tested on Samsung S8, Apple iPhone 6, Apple iPad Air 2 and also using the Google Chrome inspect feature to test for repsonsiveness and any errors that occurred. The main issue which was found was the sidevar/ navbar not resizing.

## Deployment

The following section describes the process to deploy this project to Heroku.

1. Ensure all required technologies are installed locally, as per the `requirements.txt`file.
2. Via Linux Terminal, login to Heroku, using 'heroku login' command. Input Heroku login details.
2. Create new Heroku app, using 'heroku apps:create appname' command.
3. Push project to Heroku, using 'push -u heroku master' command.
4. Create scale, using 'heroku ps:scale web=1' command.
5. Login to Heroku and select newly created app.
6. Select settings. Select ‘Reveal Config'. Add IP 0.0.0.0 and PORT 5000.
7. From 'More' menu on the top right, select 'Restart all dynos'.
8. View app: In settings, select Domain URL, NOT Git URL to view your hosted application.
9. Deployed via Heroku: [Daddy Does Dinner](https://cookbook-pierce.herokuapp.com/)


Please visit **DEMO** at https://cookbook-pierce.herokuapp.com/


## Credits

### Content
- The recipes came from the [Easy Food](http://easyfood.ie/) website.

### Media
- The photos used in this site were obtained from [Easy Food](http://easyfood.ie/) website.

### Acknowledgements

- I received inspiration for this project from [Easy Food](http://easyfood.ie/) website.
