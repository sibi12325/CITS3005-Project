# Import used libraries
from rdflib import Graph
import os

# Change to the directory of the knowledge graphs
cwd = os.path.abspath(os.path.dirname(__file__))
os.chdir(cwd)
os.chdir('flask')
os.chdir('knowledge_graphs')

# Initialise graph
g = Graph()
g.parse('Appliance.owl')

# Query to find all guides that have more than 6 steps
query1 = """
    SELECT ?title
    WHERE { 
        ?guide a :Guide ;
            :has_title ?title ;
            :has_step ?step .
    }
    GROUP BY ?guide ?title
    HAVING (COUNT(?step) > 6)
"""
print('Procedures that include more than 6 steps: ')
for row in g.query(query1):
    print(row[0])
print('\n')

# Query to find all tools that appear in more than 10 Guides
query2 = """
    SELECT ?tool
    WHERE { 
        ?guide a :Guide ;
            :uses_tool ?tool .
    }
    GROUP BY ?tool
    HAVING (COUNT(?tool) > 10)
"""
print('All items that have more than 10 procedures written for them:')
for row in g.query(query2):
    print(row[0].split('#')[1])
print('\n')


# Query to find all tools in guides that are no mentioned in any of the guide's steps
query3 = """
    SELECT ?title
    WHERE {
    ?guide rdf:type :Guide;
        :has_title ?title.
    ?guide :uses_tool ?tool .
    
    FILTER NOT EXISTS {
        ?guide :has_step ?step .
        ?step :uses_tool ?tool .
    }
    }
"""
print('All procedures that include a tool that is never mentioned in the procedure steps:')
for row in g.query(query3):
    print(row[0])
print('\n')

# Query to flag all guides which have words "careful"/"dangerous" as potential hazards
query4 = """
    SELECT ?guide ?step
    WHERE {

    ?guide rdf:type :Guide;
        :has_step ?step .

    ?step rdf:type :Step;
        :step_text ?text.
    
    FILTER (CONTAINS(?text,"careful") || CONTAINS(?text,"dangerous"))
    }
"""
print("All guides that have potentialy hazardous steps")
for row in g.query(query4):
    print(f"Potential hazard at Guide {row[0].split('#')[1]} on step : {row[1].split('#')[1]}")
print('\n')
