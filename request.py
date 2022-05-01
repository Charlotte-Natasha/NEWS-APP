import json
from app import app
from urllib.request import json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']