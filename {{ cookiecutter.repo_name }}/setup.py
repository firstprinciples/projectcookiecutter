import setuptools
import os
import apeel_{{cookiecutter.repo_name}}

def populate_dependencies(filename='requirements.txt'):
    """
    this function reads external packages from
    requirements.txt, removes the versions and
    appends them to a list that will be used
    in install_requires
    :param filename: file name
    :return: populated requirements
    """

    string_to_match = "# external requirements"
    save_to_install_list = False
    requirements = []
    try:
        with open(filename) as file:
            for line in file:
                if  save_to_install_list and line.strip():
                    requirements += [line.split('=')[0].rstrip()]
                if string_to_match in line and save_to_install_list == False:
                    save_to_install_list = True
    except:
        print("reading requirements.txt failed")

    return requirements

def get_model_files():
    """
    This function looks under models/deployed
    directory to get the relative path of
    *.joblib files.
    :return: relative path of .joblib files
    """
    current_directory_path = os.path.dirname(os.path.realpath(__file__))
    current_directory = os.path.basename(current_directory_path)
    model_directory = os.path.join('apeel_' + current_directory, 'models/deployed')

    model_paths = []
    for (path, directories, filenames) in os.walk(model_directory):
        for filename in filenames:
            if ".joblib" in filename:
                model_paths.append(os.path.join(path, filename))
    return model_paths

# Get the version of this package
version = apeel_{{cookiecutter.repo_name}}.version

#Populate external requirements from requirements.txt
external_reqs = populate_dependencies('requirements.txt')

#Get model joblib files
model_files = get_model_files()

# Get the long description of this package
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='apeel_{{cookiecutter.repo_name}}',
    version=version,
    author="Apeel Data Science",
    author_email="software@apeelsciences.com",
    description="{{cookiecutter.description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/apeelsciences/datascience/projects/{{cookiecutter.repo_name}}",
    packages=setuptools.find_packages(exclude=['unit_tests']),
    install_requires=['apeel_datatools', 'apeel_nirfirmness3'] + external_reqs,
    package_data={'apeel_{{cookiecutter.repo_name}}': model_files},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
