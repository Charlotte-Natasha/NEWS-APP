from flask import Flask, render_template
from app import app

@app.route('/')
def h1():
    return render_template("index.html")