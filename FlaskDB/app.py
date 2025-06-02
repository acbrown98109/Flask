# Import necessary libraries
from flask import Flask, request, render_template
import sqlite3  # Import SQLite for database operations
# Create Flask application instance
app = Flask(__name__)

# Function to initialize the database
def init_db():
    # Initialize the database connection
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Create a table if it doesn't exist (name only)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()  # Close the connection after setup

# Define route for the home page
@app.route('/', methods=['GET', 'POST'])
# Handle GET and POST requests to the home page
def index():
    if request.method == 'POST':
        name = request.form['name']
        # Save submitted name to the database
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO entries (name) VALUES (?)', (name,))
            conn.commit()
    return render_template('index.html')  # Render the HTML template

# Run the app only if this script is executed directly
if __name__ == '__main__':
    init_db()  # Set up database on startup
    app.run(debug=True)
