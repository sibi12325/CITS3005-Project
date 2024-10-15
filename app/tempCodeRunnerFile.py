import os

cwd = os.path.abspath(os.path.dirname(__file__))
os.chdir(cwd)
os.chdir('..')
os.chdir('dataset')

for filename in os.listdir(os.getcwd()):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Join the lines into a single JSON string wrapped in brackets
    json_string = "[" + ",".join(lines) + "]"

    # Write the corrected JSON to a new file
    with open(filename, 'w') as corrected_file:
        corrected_file.write(json_string)