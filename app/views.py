from flask import render_template
from app import app
from newsapi import NewsApiClient

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/')
# def index():
#     newsapi = NewsApiClient(api_key="4c212547c2de4b73a5917d14dfba0343")   
#     topheadlines = newsapi.get_top_headlines(sources = "Fox Business")

#     articles = topheadlines['articles']

#     desc = []
#     news = []
#     img = []

#     for i in range (len(articles)):
#         myArticles = [articles[i]]


#         news.append(myArticles['title'])
#         desc.append(myArticles['description'])
#         img.append(myArticles['urlToImage'])
 
#     myList = zip(news, desc, img)

#     return render_template('index.html', context= myList)