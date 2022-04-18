
import sqlite3
import csv
from application import app
from application.forms import Login_form
from flask import render_template, request, redirect, flash, session, url_for
from contextlib import closing
import os

# secret key to run all routes 
SECRET_KEY = os.urandom(20)
app.config['SECRET_KEY'] = SECRET_KEY

# connect to database
connect = sqlite3.connect('recipes.sqlite', check_same_thread=False)
connect.row_factory = sqlite3.Row

# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# route for index page 
@app.route("/")
@app.route("/index")
def index():
    # get index.html page loaded
    return render_template('index.html')


# route for register page 
@app.route("/register")
def register():
    # get register.html page loaded
    return render_template("register.html")


# route for home page 
@app.route("/home")
def home():
    recipes = []
    # open csv file and load photo and recipe for food
    with open("allRecipes.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            recipes.append(row)
    print(recipes)

    # get home.html page loaded
    return render_template("home.html", recipes=recipes)

# image file path
app.config["UPLOAD_PATH"] = "application/static/img"

# route for uplode recipe 
@app.route("/uplode", methods=['POST', 'GET'])
def uplode():
    if request.method == 'POST':
        # get the image from the form       
        uploaded_file = request.files['file']
        # save the image to the path file
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], uploaded_file.filename))

        name = request.form.get('name')
        # get ingradients input from the form 
        ingredients = request.form.get('ingredients')
        # get instruction input from the form 
        instructions = request.form.get('instructions')
        # get serving from input the form 
        servings = request.form.get('servings')
        # add all inpits to recipe list 
        recipe= []
        recipe.append(uploaded_file.filename)
        recipe.append(name)
        recipe.append(ingredients)
        recipe.append(instructions)
        recipe.append(servings)
        # write all inputs to recipes  csv file 
        with open('allRecipes.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(recipe)
            
    # call back to home.html page   
    return redirect('home')


# route for delete recipe
@app.route('/delete', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        name = request.form.get('name')
        recipes = []
        # open csv file and load photo and recipe for food
        with open("allRecipes.csv", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                recipes.append(row)
        for recipe in recipes:
            if name == recipe[1]:
                recipes.remove(recipe)
        with open('allRecipes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for row in recipes:
                writer.writerow(row)

    return redirect(url_for('home'))


# route for registration 
@app.route('/register', methods=['POST', 'GET'])
def get_registration():
    # get the information from registration form
    email = request.form['email']
    password = request.form['password']
    with closing(connect.cursor()) as c:
        # insert into database tabel email and password
        c.execute('INSERT INTO Register (email, password) VALUES (?,?)', (email, password))
        # commit the query
        connect.commit()
        # get login.html page loaded
    return redirect(url_for('login'))


# route for login to recipes /home page 
@app.route("/login", methods=['POST', 'GET'])
def login():
    # get validation from class login form
    login_form = Login_form()
    # check if the validation pass or no
    if login_form.validate_on_submit() == True:

        if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
            email = request.form['email']
            password = request.form['password']
            # get the email and password from database
            with closing(connect.cursor()) as c:
                c.execute('SELECT * FROM Register WHERE email = ? AND password = ?', (email, password,))
                found = c.fetchone()
            # check if account found in database or not
            if found:
                session['password'] = found['password']
                session['email'] = found['email']
                return redirect(url_for('home'))
            else:
                # use flash and bootstrap to display error message
                flash("sorry : something went wrong.", "danger")
    return render_template('login.html', title="Login", form=login_form, login=False)
