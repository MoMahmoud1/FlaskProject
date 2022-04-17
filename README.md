# FlaskProject >> 
creat wep app for recipes ,have login system using squlite3 database to save register data I register page and call it in login page ,home page have display all recipes and otipn to add new recepe and delete recipe,learn how to connect to database from cs50 and stack overflow and how to use flask from https://www.linkedin.com/learning/full-stack-web-development-with-flask/creating-and-running-a-simple-flask-application?autoSkip=true&autoplay=true&resume=false&u=27766394

*main page have image for recipes app logo.

*footer and navbar in main page.

*registr page and login page in main page using jinja2.
*show message in register page using js validation .
*show error message in login page using bootstrap.
*after login >>>home page will display recipes.
*home page have logout botton to go back to login page.
*home page have uplode recipe form using jinja2 to include it .
*using validation for uplode image and inputs for add new recipe.
*if the user uplode recipe will display in home page directly.
*home page have delete button to remove recipe by enter the recipe name.
*using SQlite3 for loin system to save the enterd data .
*using CSV file to save the recipes.
Application layout.
*application folder contain.
1-static folder for CSS for styling.
	1-images.css to store image for main page in application.
	2-img.css to store image for home page in application.
2-java scripts for validation the user inputs(script.js).
*Create templates folder contains.
	1-Will have base html page to using for inheriting among all pages.
2-Html page for main page(login.html).
	3-Html page for navigation(nav.html).
	4-Html page for footer(footer.html).
	5-Html page for register(register.html).
	6-Html page for home (home.html).
	7-Html page for upload recipe (upload.html).
	8-Html page for delete recipe (delete.html)
	9-init.py it will import all routs.
	10-forms.py have validation method for inputs.
	11-routs.py have all routs for all app.
	*Venv
1-app.py just importing the App from the Application folder.
2-config.py include a secret key
3-requirements .txt have all libraries to run the website.



