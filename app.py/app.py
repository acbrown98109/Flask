#import necessary libraries
from flask import Flask, request, render_template

# Create a Flask application instance
app = Flask(__name__)
# Define a route for the root URL and home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')
# Define routes for about page
@app.route('/about')
def about():
    return render_template('about.html', title='About')
# Define a route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

#initialize the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='') 
