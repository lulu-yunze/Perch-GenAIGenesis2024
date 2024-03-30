from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    # Assuming you're passing the project name dynamically
    app_data = {'project_name': 'Your Project Name'}
    return render_template("index.html", app_data=app_data)

if __name__ == "__main__":
    app.run(debug=True)
