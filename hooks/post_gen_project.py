import os
import shutil

repo_type = '{{ cookiecutter.repo_type }}'
deployment_paths = ['MANIFEST.in', '.gitlab-ci.yml', 'unit_tests', 
                    'apeel_{{ cookiecutter.repo_name }}/models/deployed']

if repo_type == 'Exploratory':
    for path in deployment_paths:
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)