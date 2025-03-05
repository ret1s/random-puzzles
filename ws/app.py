from flask import Flask, request, render_template_string
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'  # Directory where files are saved
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Simple HTML form for file upload
FORM_TEMPLATE = '''
    <h1>Upload a File</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    <p><a href="/">Back to Home</a></p>
'''

# Home page
@app.route('/')
def home():
    return "Welcome to the Home Page! <br><a href='/upload'>Upload a file</a>"

# Upload route
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if a file is in the request
        if 'file' not in request.files:
            return "No file part in the request!"
        
        file = request.files['file']
        
        # If no file is selected
        if file.filename == '':
            return "No file selected!"
        
        # Save the file to the upload folder (vulnerable: no validation!)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return f"File {file.filename} uploaded successfully! <a href='/'>Back</a>"
    
    # Show the upload form for GET requests
    return render_template_string(FORM_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)