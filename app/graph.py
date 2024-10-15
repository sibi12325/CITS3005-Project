from rdflib import Graph
from rdflib import URIRef, BNode, Literal
from rdflib.namespace import FOAF, RDF

g = Graph()

g.parse('C:/Users/sibim/OneDrive - UWA/CITS3005/CITS3005-Project/knowledge_graphs/Appliance.owl')

graph = g.serialize()

