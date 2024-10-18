# Import used libraries
from flask import render_template, request
from rdflib import Namespace, Graph, Literal
from app import app
from .modules.graph import g, shacl_graph
from pyshacl import validate

# Default route. Start with displaying the current graph
@app.route('/')
def index():
	result = "Result will be displayed here"
	return render_template('index.html', graph=g.serialize(format='turtle'))

# Route to query the ontology based on input
@app.route('/query', methods=['POST'])
def query():

	# Ensure details were added before submitting
	query_input = request.form.get('query').strip()
	if query_input == "":
		result = "Enter details before submitting"
	else:
		# Attempt to query. If failed then syntax/logic of query is incorrect
		try:

			# Put into readable format
			result = g.query(f"""{query_input}""")
			result = result.serialize(format="csv")
			result = result.decode("utf-8")
			
			# Remove the variable names (headers formed from csv conversion)
			for i, val in enumerate(result):
				if val == '\n':
					result = result[i + 1:]
					break
			
			# Check if the result was empty
			if result.strip() == "":
				result = "No results found"

		# Case when query is invalid		
		except Exception as e:
			result = f"Query is not valid. Got error : {e}"

	return render_template('index.html', query=query_input, graph=result)

# The namespace to be used to add/remove from the database
EX = Namespace("http://example.org/ontologies.owl#")

# Add all valid subject classes and their respective properties
valid_subject_classes = {"Guide": ["has_title", "has_guidid", "has_step", "has_url", "uses_tool"]}
valid_subject_classes.update( {"Step": ["step_order", "step_text", "uses_tool"]} )
valid_subject_classes.update( {"Tool": ["has_url", "rdfs:label"]} )

# Route to add to the ontology
@app.route('/add', methods=['POST'])
def add():

	query_input = request.form.get('add').strip()

	# Ensure query is non empty
	if query_input == "":
		result = "Enter details before submitting"
		return render_template('index.html', query=query_input, graph=result)

	# Split and construct the subject, predicate, and object
	subject_str, predicate_str, object_str = query_input.split(',')
	subject = EX[subject_str.strip()]
	predicate = EX[predicate_str.strip()]

	# Extract the subject class prefix (e.g., "Guide" from "Guide_100110")
	subject_prefix = subject_str.split('_')[0]

	# Validate subject class and predicate
	if subject_prefix not in valid_subject_classes:
		return render_template('index.html', query=query_input, graph=f"Invalid subject class: {subject_prefix}. Allowed classes are: {', '.join(valid_subject_classes.keys())}")
	if predicate_str not in valid_subject_classes[subject_prefix]:
		return render_template('index.html', query=query_input, graph=f"Invalid predicate '{predicate_str}' for subject class '{subject_prefix}'.")

	# Determine if the object is a Literal or another entity
	if predicate_str in {"has_category", "has_title", "has_url"}:
		object = Literal(object_str.strip())
	elif predicate_str == "has_guidid":
		# Ensure a valid int was entered
		try:
			_ = int(object_str)
		except:
			return render_template('index.html', query=query_input, graph="Invalid data type for has_guidid. Expected an integer.")
	else:
		object = EX[object_str.strip()]

	# Temporarily add the triple to the graph for validation
	temp_graph = g + Graph()
	temp_graph.add((subject, predicate, object))

	# Validate the graph against the SHACL shapes
	conforms, _, report_text = validate(data_graph=temp_graph, shacl_graph=shacl_graph)

	if conforms:
		# If valid, add the triple to the main graph
		g.add((subject, predicate, object))
		result = "Added successfully"
	else:
		# If not valid, return the SHACL validation report
		result = f"Triple is not valid according to SHACL: {report_text}"

	return render_template('index.html', query=query_input, graph=result)

# Route to remove from ontology
@app.route('/remove', methods=['POST'])
def remove():
	query_input = request.form.get('remove').strip()

	# Ensure query is non empty
	if query_input == "":
		result = "Enter details before submitting"
		return render_template('index.html', query=query_input, graph=result)
      
	# Retrieve and prepare inputs for removal
	subject, predicate, object = query_input.split(',')
	subject = EX[subject.strip()]
	predicate = EX[predicate.strip()]

	# Try and remove otherwise report error
	try:
		g.remove((subject, predicate, object))
	except Exception as e:
		return render_template('index.html', query=query_input, graph=f"Invalid removal for triple, error : {e}")
	
	return render_template('index.html', query=query_input, graph=f"Removed ({subject},{predicate},{object})")