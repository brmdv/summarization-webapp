from flask import Flask, render_template, request
import json

from flask.json import jsonify

app = Flask(__name__)

# load book list
with open("books/books.json", "r") as jsonfile:
    available_books = json.load(jsonfile)


@app.route("/")
def index():
    return render_template("index.html", books=available_books)


@app.route("/summarize", methods=["GET", "POST"])
def summarize():
    if request.method == "POST":
        # user sent raw text
        return request.form.get("text")

    elif request.args.get("book"):
        # use selected predownloaded book
        return jsonify(available_books[int(request.args.get("book"), 0)])

    elif request.args.get("url"):
        # user sent link
        return "Link loading not implemented."

    return "Not ready"