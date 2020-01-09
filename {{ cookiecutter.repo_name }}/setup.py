import setuptools
import apeel_{{cookiecutter.repo_name}}

# Get the version of this package
version = apeel_{{cookiecutter.repo_name}}.version

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
    install_requires=['apeel_datatools',],
    package_data={'apeel_{{cookiecutter.repo_name}}': ['models/*.joblib']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
