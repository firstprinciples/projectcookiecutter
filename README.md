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

    cookiecutter https://gilab.com/apeelsciences/datascience/datacookiecutter


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
│   ├── figures                 <-- .png etc files.
│   ├── notebooks               <-- Jupyter notebooks, including EDA and formal reports.
│   ├── predict                 <-- API code for trained models. Use base class `TrainedModel`.
│   │   ├── __init__.py 
│   │   └── predict.py          
│   ├── train                   <-- Transform raw data and use transformed data to train models          
│   │   ├── __init__.py
│   │   ├── train.py            <-- Code that uses data in `transformed.csv` to train ML models and serialize them
│   │   │                           in `trained_models`. Use base class `ModelTrainer`. 
│   │   └── preprocess.py        <-- Transform data using DataTransformer
│   │                           <-- Optional: if needed, add module `dataset.py` to make/query dataset
│   └── trained_models          <-- Serialized trained models.
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
