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
			result = result.decode("utf-8")
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

@app.route('/addRelation', methods=['POST'])
def addRelation():
	query_input = request.form.get('relation')

	try:
		result = g.query(query_input)
		for triple in result:
			g.add(triple)
		
		result = result.serialize(format="csv")
		result = result.decode("utf-8")
	except:
		result = "Construct Query is not valid"
	
	return render_template('index.html', query=query_input, graph=result)


"""
PREFIX : <http://example.org/ontologies.owl#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

CONSTRUCT {
        :Guide_100110 a :Guide ;
            a owl:NamedIndividual ;
			:has_category "Cuisinart Mini-Prep DLC-2A"^^xsd:string ;
			:has_guidid 100110 ;
			:has_step :Step_185161,
						:Step_186898,
						:Step_186906,
						:Step_186911 ;
			:has_title "SIBI MOOTHEDAN"^^xsd:string ;
			:has_url "https://www.ifixit.com/Guide/SIBI+MOOTHEDAN/100110"^^xsd:string ;
			:uses_tool :Tool_phillips_screwdriver,
						:Tool_spudger .
    }
    WHERE {

    }
"""
