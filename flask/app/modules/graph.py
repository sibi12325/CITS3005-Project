# Import all used libraries
from rdflib import Graph
import os

# Navigate to where the knowledge graphs are stored
cwd = os.path.abspath(os.path.dirname(__file__))
os.chdir(cwd)
os.chdir('..')
os.chdir('..')
os.chdir('knowledge_graphs')

# Initialise graph
g = Graph()
g.parse('Appliance.owl')

# Navigate to where the shapes ttl file is stored (for pyshacl)
os.chdir('..')
os.chdir('app')

# Initialise pyshacl graph
shacl_graph = Graph()
shacl_graph.parse('shapes.ttl', format='turtle')