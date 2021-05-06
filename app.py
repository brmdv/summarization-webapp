from flask import Flask, render_template, request, Response, redirect
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
        return render_template(
            "base.html",
            pagetitle="Summary of user text",
            page_message=request.form.get("text"),
        )

    elif request.args.get("book"):
        # use selected predownloaded book
        book = available_books[int(request.args.get("book"))]

        # book summarization goes here

        return render_template(
            "summary.html",
            book=book,
            info={"Used model": "None"},
            characters=[],
            pagetitle=f"Summary of {book['title']} – {book['author']}",
        )

    elif request.args.get("url"):
        # user sent link
        return render_template(
            "base.html",
            pagetitle="Not implemented yet",
            page_message="Link loading not implemented.",
            status=400,
        )

    return redirect("/")


@app.route("/book/<int:id>")
def book_info(id):
    """Get available information about book in JSON format."""
    try:
        book = available_books[int(id)]
        return jsonify(book)
    except IndexError:
        return Response("Book not found", status=400)
    except:
        return Response("Internal error.", status=404)
