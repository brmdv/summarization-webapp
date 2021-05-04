from flask import Flask, render_template
import json

app = Flask(__name__)

# load book list
with open("books/books.json", "r") as jsonfile:
    available_books = json.load(jsonfile)


@app.route("/")
def index():
    return render_template("index.html", books=available_books)
