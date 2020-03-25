# Apeel Data Science Cookiecutter

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


#### [Project homepage]


### Requirements to use the cookiecutter template:
-----------
 - Python >= 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://gilab.com/apeelsciences/datascience/projectcookiecutter.git


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
.
├── README.md                   <-- Project README
├── apeel_{{ cookiecutter.repo_name }}  <-- package, named `apeel_<repo-name>` to avoid PyPI naming conflicts
│   ├── __init__.py             <-- Specify version number of package. <major>.<minor>.<build>
│   │                               Increments correspond to <API change>.<Feature addition>.<Improvement>    
│   ├── data                    <-- All data files
│   │   ├── external            <-- Outside data goes here
│   │   ├── raw                 <-- raw, immutable data file
│   │   └── transformed         <-- transformed, merged, etc version of raw data in `transformed.csv`
│   ├── analyses                <-- All analysis work. Jupyter notebooks, including EDA and formal reports.
│   ├── models                  <-- Models for deployment. Use modelcookiecutter for uniform dir structure for each model.       
│   └── preprocessing           <-- Preprocessing functionality relevant across the whole project.
│      
├── requirements.txt            <-- `pip freeze > requirements.txt` your vrtl env so that results can be reproduced. 
├── setup.py                    <-- make package installable with `pip install -e` and define `install_requirements`
│                                   `setup.py` = abstract requirements,  requirements.txt => concrete (versioned)
└── unit_tests
    └── test_environment.py

--------
```

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
