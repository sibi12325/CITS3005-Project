from flask import render_template, request
from app import app
from .modules.graph import g

@app.route('/')
def index():
	result = "Result will be displayed here"
	return render_template('index.html', graph=g.serialize(format='turtle'))

@app.route('/query', methods=['POST'])
def query():
	query_input = request.form.get('query')
	if query_input == "":
		result = "Enter details before submitting"
	else:
		try:
			result = g.query(f"""{query_input}""")
			result = result.serialize(format="csv")
			result = result.decode("utf-8")  # Decode from bytes to string
		except:
			result = "Query is not valid"
	return render_template('index.html', query=query_input, graph=result)

@app.route('/add', methods=['POST'])
def add():
	query_input = request.form.get('add')
	result = "Add doesnt work yet"
	return render_template('index.html', query=query_input, graph=result)

@app.route('/remove', methods=['POST'])
def remove():
	query_input = request.form.get('remove')
	result = "Remove doesnt work yet"
	return render_template('index.html', query=query_input, graph=result)

@app.route('/update', methods=['POST'])
def update():
	query_input = request.form.get('update')
	result = "Update doesnt work yet"
	return render_template('index.html', query=query_input, graph=result)
