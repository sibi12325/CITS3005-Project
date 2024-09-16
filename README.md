# CITS3200 PROJECT - Conversational AI System for Error Checking Submission Forms

## About

Large Language Model (LLM) bots are becoming increasingly prevalent, aiding users in interacting with data in a human-like conversational manner. This project aims to leverage an LLM, such as ChatGPT, to create a virtual assistant capable of analysing submission forms to ensure all the information is correct. The problem we face is that submission spreadsheets often undergo subtle alterations, making it difficult to ingest the data correctly without manual checking. These minor changes can be hard to detect, requiring extensive manual intervention to fix.

To address this, I propose developing a chatbot or virtual assistant. The chatbot will initially perform the following functions: accept a chain of custody, digest and check the form for errors, and inform the user if any errors are found. By training the AI to identify and correct common errors, we can streamline the data submission process, reduce the need for manual error checking, and ensure data integrity within the LIMS. This solution will enhance efficiency, allowing us to focus on more critical aspects of laboratory management. 

## Installation

The following software should be downloaded prior to installation
 * [Git](https://git-scm.com/downloads)
 * [Python - 3.12.0](https://www.python.org/downloads/)
 * An IDE - [Visual Studio Code](https://code.visualstudio.com/download) Recommended

#### 1. Check your Python version
In a terminal run:
 * `python` / `python3` to check your python version (can run `exit()`) to close python terminal
 * `python -m pip` or `pip` to confirm pip is funtioning
 * `python -m venv` to check python's inbuilt environment manager is functioning

#### 2. Clone the Repository
The simplest way to clone the repo is using VSCode, in the IDE on the "welcome" page there is an option to "Clone Git Repository",
Click it and then paste in the link for the repo: `https://github.com/joshshipton/Prof_comp.git`, then you'll be prompted to sign into you github account.

#### 3. Create and Activate Your Virtual Environment with venv
 1. Run `python3 -m venv venv` in the terminal to create your virtual environment. 
 2. Activate your venv using `.\venv\Scripts\activate` for windows or with `source venv/bin/activate` if using a linux based command line - you will need to activate the environment whenever you plan to run code within the project.
 3. Install any packages in the virtual environment:
     * On initial setup dependancies can be installed from the `requirements.txt` file by executing `pip install -r requirements.txt` __within the virtual environment__ - `(venv)` should be visible in your command line
     * If another package needs to be installed use `pip install` as normal within the venv, then once any changes are made save them by updating the requirements.txt file using `pip freeze > requirements.txt`

#### 4. Run the Flask Application
Now that all the setup is completed you are ready to code and to run the application. This can be done with `flask run` in the terminal

## Group Members:

__Camilo Lima Castillo__ (23364195) \
Email: 23364195@student.uwa.edu.au \

__Josh Shipton__ (23192823) \
Email: 23192823@student.uwa.edu.au \

__Sibi Moothedan__ (23615908) \
Email: 23615908@student.uwa.edu.au \

__James Hudibyo__ (23452945) \
Email: 23452945@student.uwa.edu.au \

__Samuel Kent__ (22704037) \
Email: 22704037@student.uwa.edu.au \
