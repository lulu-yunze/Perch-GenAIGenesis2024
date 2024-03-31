from flask import *
import os
import assemblyai as aai

app = Flask(__name__)

app_data = {'project_name': 'Perch'}

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
    file.save(file_path)

    if file.filename.endswith('.mp3'):
        transcribe_audio(file_path)
        file_path = os.path.join('uploads', file.filename + "transcribed")
    
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

def transcribe_audio(file_path):

    # Replace with your API key
    aai.settings.api_key = "ce7e699b08654c93bd8db3f5fe302921"

    # URL of the file to transcribe
    FILE_URL = file_path

    # You can also transcribe a local file by passing in a file path
    # FILE_URL = './path/to/file.mp3'

    config = aai.TranscriptionConfig(auto_highlights=True)

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(
    FILE_URL,
    config=config
    )

    transcription_text = transcript.text
    transcribed_file_path = os.path.join(file_path + "transcribed")
    with open(transcribed_file_path, 'w') as file:
        file.write(transcription_text)

    return transcript.text
    
@app.route('/show_output')
def show_output():
    # Retrieve the output from the query parameter
    
    output = request.args.get('output', '')
    return render_template('output.html', output=output, app_data=app_data)

@app.route('/dev')
def dev():
    app_data = {'project_name': 'Perch'}
    return render_template('dev.html', app_data=app_data)

if __name__ == "__main__":
    app.run(debug=True)
