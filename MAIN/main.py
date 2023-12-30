# flask_app.py
from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/movies")
def Moviestreamlit():
    subprocess.run(["streamlit", "run", "movies.py"])
    return ""

@app.route("/courses")
def CourseStreamlit():
    # Run the Streamlit app as a subprocess
    subprocess.run(["streamlit", "run", "courses.py"])
    return ""

if __name__ == "__main__":
    app.run(debug=True)

