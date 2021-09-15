from flask import Flask, render_template, url_for
app = Flask(__name__)

posts=[
    {
        'Author': "Mukund C Menon",
        'Title': "Blog Post 1",
        'Content': "Python Development",
        'Date_Posted': "15 Sept 2021"
    },
    {
        'Author': "Sindhu L",
        'Title': "Blog Post 2",
        'Content': "Hindi Classes",
        'Date_Posted': "16 Sept 2021"
    }
]

# Creating the Home Page
@app.route("/")  # route() decorator to tell Flask what URL should trigger our function.
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


# Creating an about page i.e http://127.0.0.1:5000/about
@app.route("/about")
def about():
    return render_template('about.html', title="About")



# Run web browser with python alone and not using command line in CMD
if __name__=='__main__':
    app.run(debug=True)


## ------------------Step1------------------------------------------------
# Use the command >> set FLASK_APP=name_of_program.py then load the webpage using >> flask run
# This will run the web browser on the Ip address generated in CMD
# The ip address can be modified to localhost:5000
# By default the Debug mode is off hence wven the slighest change in code requires the web page to be rerun from command line
# To over come this switch off the Debug mode
# To switch off debug mode >> set FLASK_DEBUG=1 (caps not necessary), now >> flask run
# To run the web browser without command line (only using python) use the above if command



##---------------------------Step 2--------------------------------------

# To make the HTML contents, to make sure the editor looks clean we use templates to make the html file
# Create a template folder in the same project
# Create html files named home.html, about.html and so on
# Now the html file has to be imported using the render_template package

##---------------------------Step 3---------------------------------------

# To make sure only necessary code exist in each of the html files and remove reoetative codes from it we use template inheritance
# For that create a template inheritance
# Create a layout.html file in which write the code block {% block content %}{% endblock %} in the body
# Type the repetative code in the title (if that is where it has to go)
# Go to home.html and about.html and use {% extends "layout.html" %} for template inheritance
# In home.html and about.html and put the code specific to these html files within the code block of {% block content %}{% endblock %}


##---------------------------Step 4---------------------------------------

# Using bootstrap
# Copy the CSS and Bootstrap and paste it in the head of the layout page from which all the pages would inherit
# Copy the JavaScript and paste it in the head of the layout page from which all the pages would inherit
# Now keep the content of the home and about in a container class within a div tag to make it look neat


##---------------------------Step 5---------------------------------------

# Creating a navigation bar, main section and bringing in CSS in the code
# The navigation bar code is placed in the body of the layout.html and the main.html replaces the inheritance block content
# Copy the required snippets
# To bring in static files like CSS and JavaScript into the flask code create a new folder called static
# Create a main.css file and copy the snippet into it
# To use the CSS file in the layout.htm a new package url_for has to be used
# <link rel="stylesheet" type="text/css" href="{{url_for('static', filename= 'main.css')}}> for linking the main.css file with layout.html
