import setuptools
import os
import fps_{{cookiecutter.repo_name}}

# Get the version of this package
version = fps_{{cookiecutter.repo_name}}.version

# Get the long description of this package
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='fps_{{cookiecutter.repo_name}}',
    version=version,
    author="First Principles",
    author_email="rcpattison@gmail.com",
    description="{{cookiecutter.description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/firstprinciples/projects/{{cookiecutter.repo_name}}",
    packages=setuptools.find_packages(exclude=['unit_tests']),
    install_requires=[
        'numpy',
        'scipy',
        'pandas',
        'matplotlib',
        'Pillow',
        'scikit-learn',
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
