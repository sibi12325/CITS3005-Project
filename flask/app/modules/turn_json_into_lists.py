import os

# Navigate to where the ifixit json files are stored
cwd = os.path.abspath(os.path.dirname(__file__))
os.chdir(cwd)
os.chdir('..')
os.chdir('..')
os.chdir('dataset')

# Convert each file into a list to be able to be used with the json.load in the make_ontologies file
for filename in os.listdir(os.getcwd()):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Join the lines into a single JSON string wrapped in brackets
    json_string = "[" + ",".join(lines) + "]"

    # Write the corrected JSON to a new file
    with open(filename, 'w') as corrected_file:
        corrected_file.write(json_string)