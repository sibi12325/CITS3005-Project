# CITS3005 PROJECT

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

__Sibi Moothedan__ (23615908) \
Email: 23615908@student.uwa.edu.au \

__Daniel Le__ (23625105) \
Email: 23625105@student.uwa.edu.au \
