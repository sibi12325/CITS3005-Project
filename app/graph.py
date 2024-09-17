from rdflib import Graph
from rdflib import URIRef, BNode, Literal
from rdflib.namespace import FOAF, RDF

g = Graph()

bob = URIRef("http://example.org/people/Bob")
linda = BNode() # a GUID is generated

name = Literal("Bob") # passing a string
age = Literal(24) # passing a python int
height = Literal(76.5) # passing a python float

g.add((bob, RDF.type, FOAF.Person))
g.add((bob, FOAF.name, name))
g.add((bob, FOAF.age, age))

g.add((bob, FOAF.knows, linda))
g.add((linda, FOAF.knows, bob))

g.add((linda, RDF.type, FOAF.Person))
g.add((linda, FOAF.name, Literal("Linda")))

graph = g.serialize()

