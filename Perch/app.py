from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    # Assuming you're passing the project name dynamically
    app_data = {'project_name': 'Perch'}
    return render_template("index.html", app_data=app_data)

@app.route("/layout")
def layout(): 
    app_data = {'project_name': 'Perch'}  # Define app_data variable
    return render_template("layout.html", app_data=app_data)
    
if __name__ == "__main__":
    app.run(debug=True)
