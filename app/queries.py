from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import FOAF, RDFS
from rdflib.plugins.sparql import prepareQuery

g = Graph()
g.parse("Appliance.", format="xml")