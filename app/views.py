from flask import render_template
from app import app
from .request import get_news, process_results


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Current Affairs'
    return render_template("index.html", title = title)

