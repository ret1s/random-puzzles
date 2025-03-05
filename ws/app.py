from flask import Flask, request, render_template
import sqlite3
import os
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)
DATABASE = 'database.db'
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Database connection function
def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

# Initialize database with tables and default data
def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        # Create banners table
        cursor.execute('''CREATE TABLE IF NOT EXISTS banners (
                            id INTEGER PRIMARY KEY,
                            image_path TEXT NOT NULL)''')
        # Create users table
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL,
                            email TEXT NOT NULL)''')
        # Insert default banner if not exists
        cursor.execute("SELECT * FROM banners WHERE id=1")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO banners (id, image_path) VALUES (1, 'static/default_banner.jpg')")
        # Insert some users if not exists
        cursor.execute("SELECT * FROM users")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO users (username, email) VALUES ('user1', 'user1@example.com')")
            cursor.execute("INSERT INTO users (username, email) VALUES ('user2', 'user2@example.com')")
        db.commit()
        db.close()

# Route to display the banner image
@app.route('/')
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT image_path FROM banners WHERE id=1")
    banner_path = cursor.fetchone()[0]
    db.close()
    return render_template('index.html', banner_path=banner_path)

# Route to display the upload form
@app.route('/upload', methods=['GET'])
def upload_form():
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    <button onclick="window.location.href='/'">Back</button>
    '''

# Route to upload an image
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return f'File uploaded: {os.path.join(app.config["UPLOAD_FOLDER"], filename)}'

# Route to display the update email form
@app.route('/update_email', methods=['GET'])
def update_email_form():
    return '''
    <!doctype html>
    <title>Update Email</title>
    <h1>Update Email</h1>
    <form method=post action="/update_email">
      <label for="user_id">User ID:</label>
      <input type="text" id="user_id" name="user_id"><br><br>
      <label for="email">New Email:</label>
      <input type="text" id="email" name="email"><br><br>
      <input type="submit" value="Update Email">
    </form>
    <button onclick="window.location.href='/'">Back</button>
    '''

# Vulnerable route susceptible to SQL injection
@app.route('/update_email', methods=['POST'])
def update_email():
    user_id = request.form['user_id']
    new_email = request.form['email']
    # Vulnerable SQL query with direct string concatenation
    sql = f"UPDATE users SET email='{new_email}' WHERE id={user_id}"
    db = get_db()
    cursor = db.cursor()
    try:
        # Using executescript allows multiple SQL statements, enabling SQL injection
        cursor.executescript(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        return f'Error: {e}'
    finally:
        db.close()
    return 'Email updated'

# Run the app
if __name__ == '__main__':
    init_db()
    app.run(debug=True)