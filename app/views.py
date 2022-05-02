from flask import render_template
from app import app


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'FOXNEWS'
    return render_template("index.html", title = title)

