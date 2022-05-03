from webbrowser import get
from flask import redirect, render_template, url_for
from app import app
from newsapi import NewsApiClient
from .request import get_news, process_results

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Current Affairs'
    newsapi = NewsApiClient(api_key=app.config['NEWS_API_KEY'])
    topheadlines = newsapi.get_top_headlines(sources="https://www.bbc.com/news")
    
    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myArticles = [articles[i]]

        news.append(myArticles['title'])
        desc.append(myArticles['description'])
        img.append(myArticles['urlToImage'])

    myList = zip(news, desc, img)    
    
    return render_template("index.html", title = title, context= myList)

  

