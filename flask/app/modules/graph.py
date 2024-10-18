from rdflib import Graph
import os

cwd = os.path.abspath(os.path.dirname(__file__))
os.chdir(cwd)
os.chdir('..')
os.chdir('..')
os.chdir('knowledge_graphs')

g = Graph()

g.parse('Appliance.owl')