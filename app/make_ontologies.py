import json
import os
from owlready2 import *

cwd = os.path.abspath(os.path.dirname(__file__))
os.chdir(cwd)
os.chdir('..')
os.chdir('dataset')

for filename in os.listdir(os.getcwd()):
    cwd = os.path.abspath(os.path.dirname(__file__))
    os.chdir(cwd)
    os.chdir('..')
    os.chdir('dataset')

    # Load the JSON file
    with open(filename, 'r') as file:
        data = json.load(file)

    # Create a new ontology
    onto = get_ontology("http://example.org/ontologies.owl")

    # Define classes and properties
    with onto:
        class Guide(Thing): pass
        class Step(Thing): pass
        class Tool(Thing): pass
        
        class has_title(DataProperty, FunctionalProperty): pass
        class has_category(DataProperty, FunctionalProperty): pass
        class has_guidid(DataProperty, FunctionalProperty): pass
        class has_url(DataProperty, FunctionalProperty): pass
        class has_step(ObjectProperty): pass
        class uses_tool(ObjectProperty): pass
        class step_order(DataProperty, FunctionalProperty): pass
        class step_text(DataProperty, FunctionalProperty): pass

    # Populate the ontology with data from JSON
    for guide_data in data:
        # Create a new Guide instance
        guide = Guide(f"Guide_{guide_data['Guidid']}")
        guide.has_title = guide_data['Title']
        guide.has_category = guide_data['Category']
        guide.has_guidid = guide_data['Guidid']
        guide.has_url = guide_data['Url']
        
        # Add tools to the ontology and link them to the guide
        for tool_data in guide_data.get('Toolbox', []):
            tool_name_cleaned = tool_data['Name'].replace(' ', '_').replace('-', '_').lower()
            tool = Tool(f"Tool_{tool_name_cleaned}")
            tool.label = tool_data['Name']
            tool.has_url = tool_data['Url']
            # Link the tool to the guide
            guide.uses_tool.append(tool)
        
        # Add steps to the ontology
        for step_data in guide_data.get('Steps', []):
            step = Step(f"Step_{step_data['StepId']}")
            step.step_order = step_data['Order']
            step.step_text = step_data['Text_raw']
            
            # Link the step to the guide
            guide.has_step.append(step)
            
            # Link extracted tools to the step
            for tool_name in step_data['Tools_extracted']:
                if tool_name != "NA":
                    tool_name_cleaned = tool_name.replace(' ', '_').replace('-', '_').lower()
                    tool_instance = onto.search_one(label=tool_name) or onto.search_one(iri=f"*{tool_name_cleaned}")
                    if tool_instance:
                        step.uses_tool.append(tool_instance)

    os.chdir('..')
    os.chdir('knowledge_graphs')

    # Save the ontology to an OWL file
    onto.save(file=f"{filename.split('.')[0]}.owl", format="rdfxml")
