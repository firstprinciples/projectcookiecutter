{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Apeel Data Science Project Organization
------------
```
.
├── README.md                           <-- This README
├── apeel_{{ cookiecutter.repo_name }}  <-- package, named `apeel_<repo-name>` to avoid PyPI naming conflicts
│   ├── __init__.py                     <-- Specify version number of package. <major>.<minor>.<build>
│   │                                       Increments correspond to <API change>.<Feature addition>.<Improvement>   
│   ├── analyses                        <-- analysis work, jupyter notebooks, etc
│   ├── data                            <-- All data files
│   │   ├── external
│   │   ├── raw
│   │   └── transformed
│   ├── models                          <-- models and their subfolder in here
│   └── preprocessing                   <-- any refactor preprocessing files in here
├── requirements.txt                    <-- keep this up to date so that a new user can
│                                           pip install -r requirements.txt
├── setup.py                            <-- make package installable with `pip install -e` and define `install_requirements`
│                                           `setup.py` = abstract requirements,  requirements.txt => concrete (versioned)
└── unit_tests
    └── test_environment.py
```
--------
