
# main.py.
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit_form", methods=['POST'])
def submit_form():
    return "Form submitted successfully!"

if __name__ == "__main__":
    app.run(debug=True)
