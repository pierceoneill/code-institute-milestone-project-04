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
app.secret_key = "daddy_day"

app.config['MONGO_DBNAME'] = 'cook_book'
app.config["MONGO_URI"] = 'mongodb://admin:admin01@ds161102.mlab.com:61102/cook_book'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_home')
def get_home():
    return render_template('index.html',
                          recipes = mongo.db.recipes.find())

@app.route('/get_recipes')
def get_recipes():
 
    return render_template('recipes.html',
                           recipes=mongo.db.recipes.find())


@app.route("/recipedetail/<recipe_id>")
def recipedetail(recipe_id):
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('recipedetail.html',
    recipe=the_recipe) 
    


                           
@app.route('/update_recipe_rating/<recipe_id>', methods=['POST'])
def update_recipe_rating(recipe_id):
   
    recipe = mongo.db.recipes
    
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
   
    recipes = mongo.db.recipes
    
    recipes.insert_one(request.json)
    
    return ('', 204)
    

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
   
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_my_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe=the_recipe)


@app.route('/update_edited_recipe/<recipe_id>', methods=['POST'])
def update_edited_recipe(recipe_id):
    recipes = mongo.db.recipes
    
    recipes.insert_one(request.json),
    {
        'recipe_name': request.form.get['recipe_name'],
        'recipe_description': request.form.get['recipe_description'],
        'flavour': request.form.get['flavour'],
        'meal_type': request.form.get['meal_type'],
        'base_ingredient': request.form.get['base_ingredient'],
        'recipe_image_url': request.form.get['recipe_image_url'],
        'is_vegan': request.form.get['is_vegan'],
        'ingredients': request.form.get['ingredients'],
        'steps': request.form.get['steps'],
        'author_name': request.form.get['author_name']
    }
    return redirect(url_for('get_my_recipes'))

@app.route('/contact')
def contact():
    '''Routing view to render/call contact.html in browser'''
    return render_template("contact.html")




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)