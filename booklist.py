"""Simple script to collect all available book files and put them in a JSON file.
"""
import json
from pathlib import Path

from book_reading import Book

# all html files in folder books/
available_books = [bookfile for bookfile in Path("./books/").glob("*.html")]

# generate output list
out = []
for i, bookpath in enumerate(available_books):
    # parse book
    book = Book(bookpath)
    out.append(
        {
            "id": i,
            "title": book.book_title,
            "author": book.book_author,
            "path": str(bookpath),
            "chapters": book.chapter_names,
        }
    )

# write to json
with (Path("books") / "books.json").open("w") as jsonfile:
    json.dump(out, jsonfile)