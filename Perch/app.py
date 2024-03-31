from flask import *
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Assuming you're passing the project name dynamically
    app_data = {'project_name': 'Perch'}
    return render_template("index.html", app_data=app_data)

@app.route('/success', methods = ['POST'])  
def success():  
    # Check if a file was uploaded
    if 'file' not in request.files:
        return "No file uploaded"

    file = request.files['file']
    
    # Check if the file is empty
    if file.filename == '':
        return "Empty filename"
    
    # Save the uploaded file
    file_path = os.path.join('uploads', file.filename)
    print(file_path)
    file.save(file_path)
    
    # Call your Python script to process the uploaded file
    output = run_python_script(file_path)
    
    # Redirect to another HTML page with the output
    return redirect(url_for('show_output', output=output))

def run_python_script(file_path):
    # Your code to run the Python script and process the uploaded file
    # This function should return the output of the Python script
    # For demonstration purposes, let's just read the content of the file
    
    with open(file_path, 'r') as f:
        return f.read()
    
@app.route('/show_output')
def show_output():
    # Retrieve the output from the query parameter
    output = request.args.get('output', '')
    return render_template('output.html', output=output)


if __name__ == "__main__":
    app.run(debug=True)
