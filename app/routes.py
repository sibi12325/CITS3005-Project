from flask import render_template
from app import app
from .graph import text

@app.route('/')
def index():
	return render_template('index.html', graph=text)
