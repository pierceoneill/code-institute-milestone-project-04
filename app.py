import os
from flask import Flask, render_template, flash, redirect, request, url_for, session, make_response, current_app
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
from datetime import datetime
from functools import update_wrapper

# MONGO_DBNAME = os.environ.get('MONGODB_NAME')
# MONGODB_URI = os.environ.get('MONGODB_URI')


app = Flask(__name__)
app.config['TESTING'] = True
app.testing = True
app.secret_key = "recipe_secret"

app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = 'mongodb://admin:admin01@ds161102.mlab.com:61102/cook_book'

mongo = PyMongo(app)

# # Jinja Custom Filter Datetime Object - START
# @app.template_filter('strftime')
# def _jinja2_filter_datetime(date, fmt=None):
#     date = dateutil.parser.parse(date)
#     native = date.replace(tzinfo=None)
#     format='%b %d, %Y'
#     return native.strftime(format)
# ## Jinja Custom Filter Datetime Object - END



@app.route('/')
@app.route('/get_home')
def get_home():
    return render_template('index.html',
                          recipes = mongo.db.recipes.find())

@app.route('/get_recipes')
def get_recipes():
    """
    This function shows all the updated recipes in the database
    """
    return render_template('recipes.html',
                           recipes=mongo.db.recipes.find())


@app.route('/recipedetail/<recipe_url>', methods=['GET', 'POST'])
def recipedetail(recipe_url):
    """
    This function takes you to the recipe page of a specific cocktail
    you've selected
    """
 
    recipe = {}
    recipe = mongo.db.recipes.find()
    
    
    print(recipe)
    print('*************************')

    for recipe in recipe:
        if recipe['recipe_url'] == recipe_url:
            recipes = recipe
         
           
        
    return render_template('recipedetail.html',
                           recipe=recipe)

                           
@app.route('/update_recipe_rating/<recipe_id>', methods=['POST'])
def update_recipe_rating(recipe_id):
    """
    This function takes the new recipe_rating after clicking on the stars and
    updates the recipe_rating field in the open document
    """
    recipes = mongo.db.recipes
    
    this_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    
    number_of_votes = int(this_recipe['number_of_votes'])
    print('number_of_votes is: ', number_of_votes)
    
    initial_recipe_rating = int(this_recipe['recipe_rating'])
    print('initial recipe rating is: ',  initial_recipe_rating)
    
    latest_recipe_rating = int(request.json['recipe_rating'])
    print('latest recipe rating posted is: ', latest_recipe_rating)
    
  
    
    return ('', 204)
    

@app.route('/get_login', methods=['GET', 'POST'])
def get_login():
    """
    This function shows you the login form if you're not logged in, and takes
    you to your dashboard if you are logged in
    """
    
    logged_in = False
    if request.method == 'GET' and not 'username' in session:
        return render_template('login.html',
                               logged_in=logged_in)
    elif request.method == 'GET' and 'username' in session:
        logged_in = True
        recipes = mongo.db.recipes.find()
        
        recipes_dict = {}
        
        for i, recipe in enumerate(recipes):
            recipe.pop('_id', None)
            recipes_dict[i] = recipe
        
        recipes_dict = json.dumps(recipes_dict)

        return render_template('login.html',
                               username=session['username'],
                               logged_in=logged_in,
                               recipes=recipes_dict)
    if request.method == 'POST':
        session['username'] = request.form["username"]
        logged_in = True
        recipes=mongo.db.recipes.find()
        recipes_dict = {}
        
        for i, recipe in enumerate(recipes):
            recipe.pop('_id', None)
            recipes_dict[i] = recipe
        
        recipes_dict = json.dumps(recipes_dict)
            
        return render_template('login.html',
                              username=session['username'],
                              logged_in=logged_in,
                              recipes=recipes_dict)


@app.route('/get_logout')
def get_logout():
        print('logged out')
        session.clear()
        return redirect(url_for('get_home'))


@app.route('/get_my_recipes', methods=['GET', 'POST'])
def get_my_recipes():
    if not 'username' in session:
        return redirect('/get_login')
    else:
        recipes = mongo.db.recipes.find()
        return render_template('user_recipes.html',
                           username=session['username'],
                           recipes=recipes)


@app.route('/get_add_recipe_form')
def get_add_recipe_form():
    """
    This function renders the form that we'll use to fill the fields to 
    create a recipe, and pass to the front end the options for the
    selectors
    """
    if request.url.startswith('http://'):
        request.url = request.url.replace('http://', 'https://', 1)
    print('url when get_add_recipe_form: ', request.url)
    return render_template('addrecipe.html',
                           flavour=mongo.db.flavour.find(),
                           meal_type=mongo.db.meal_type.find(),
                           base_ingredient=mongo.db.base_ingredient.find(),
                           unit_measurement=mongo.db.unit_measurement.find(),
                           author_name=mongo.db.author_name.find())


@app.route('/write_to_recipe_database', methods=['POST'])
def write_to_recipe_database():
    """ 
    This function takes the input from get_add_recipe_form and writes it into
    our database. The it redirects to get_my_recipes, where you'll see your 
    recipe as the most recently added
    """
    recipes = mongo.db.recipes
    
    recipes.insert_one(request.json)
    
    return ('', 204)
    

@app.route('/delete_cocktail/<recipe_id>')
def delete_cocktail(recipe_id):
    """
    This function deletes a cocktail from the database
    """
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_my_recipes'))


@app.route('/get_edit_recipe/<recipe_id>')
def get_edit_edit_recipe(recipe_id):
    """
    This function reopens the form and lets you rewrite on a recipe
    """
    this_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    is_vegan = this_recipe['is_vegan']
    all_meal_type = mongo.db.meal_type.find()
    all_base_ingredient= mongo.db.base_ingredient.find()
    all_flavour = mongo.db.flavour.find()
    
    return render_template('edit_recipe.html',
                           is_vegan=is_vegan,
                           meal_type=all_meal_type,
                           base_ingredient=all_base_ingredient,
                           flavour=all_flavour,
                           recipe=this_recipe)


@app.route('/update_edited_recipe/<recipe_id>', methods=['POST'])
def update_edited_recipe(recipe_id):
    """
    This recipe will rewrite the contents of a document according to the changes
    added when editing a cocktail
    """
    recipes = mongo.db.recipes
    
    recipes.update({'_id': ObjectId(recipe_id)}, request.json)
    
    return ('', 204)

@app.route('/update_edited_cocktail/<recipe_id>', methods=['POST'])
def update_edited_cocktail(recipe_id):
    """
    This recipe will rewrite the contents of a document according to the changes
    added when editing a cocktail
    """
    recipes = mongo.db.recipes
    
    recipes.update({'_id': ObjectId(recipe_id)}, request.json)
    
    return ('', 204)



@app.route('/get_search')
def get_search():
    recipes = mongo.db.recipes.find()
        
    recipes_dict = {}
    
    for i, recipe in enumerate(recipes):
        recipe.pop('_id', None)
        recipes_dict[i] = recipe
    
    recipes_dict = json.dumps(recipes_dict)

    return render_template('search.html',
                           recipes=recipes_dict)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)