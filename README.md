# Book summarization webapp

This is a simple Flask app to accompany my exploration of [automatic
summarization of novels](https://github.com/brmdv/usecase-summarization). 

## Current status

I did not get to useable results for summarization, so this app is (for now?) mainly the basic skeleton of the webapp. My goal was also to get at least the **character extraction** with *named entity recognition* working.

## Demo

Live demo is hosted on Heroku. 

<https://brams-book-summarizer.herokuapp.com>

## Included books

Some books are already predownloaded from Project Gutenberg, in the directory
_books/_. If you want to add/remove any book, you'll have to rerun the script
[booklist.py](bookllist.py), to generate _books/books.json_.
