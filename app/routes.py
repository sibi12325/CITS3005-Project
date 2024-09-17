from flask import render_template, request
from app import app
from .graph import graph

@app.route('/')
def index():
	return render_template('index.html', graph=graph)

@app.route('/query', methods=['POST'])
def query():
	query_input = request.form.get('query')  # Retrieves the input with the 'name' attribute 'query'
	return render_template('index.html', graph=query_input)
