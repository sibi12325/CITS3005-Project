from flask import render_template, request
from app import app
from .graph import graph, g

@app.route('/')
def index():
	result = "Result will be displayed here"
	return render_template('index.html', graph=graph, result=result)

@app.route('/query', methods=['POST'])
def query():
	query_input = request.form.get('query')
	result = g.query(f"""{query_input}""")
	result = result.serialize()
	return render_template('index.html', graph=query_input, result=result)
