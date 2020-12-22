from flask import render_template
from app import app

@app.route('/')
def home():
   return "<h1>Hello World</h1></br><h2>There's new changes<h2>"

@app.route('/template')
def template():
    return render_template('home.html')
