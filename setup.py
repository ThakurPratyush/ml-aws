# helps to deploy app as package
## can do install and use
from setuptools import find_packages,setup
## find the packages that are there in the entire ml application

# setup.py to automatically discover all the packages that should be 
# included in your distribution package. 

#It finds all the packages (directories containing an __init__.py file)
#in your project directory that should be included in the distribution.

#It ensures that only directories with __init__.py 
#files are considered packages and avoids including non-package directories.

from typing import List
## function returns a list
# we want that while getting req we do not read -e

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    function returns list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        ## issue with readline is that we have \n 
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements : 
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
name = 'mlproject',
version = '0.0.0.1',
## version given to the application 
author = 'ptysh',
author_email = 'thakurpratyush225@gmail.com',
packages = find_packages(),
## we dont want to manually add all the names here 
#install_requires = ['pandas','numpy','seaborn']
install_requires = get_requirements('requirements.txt')
## mention requirements/liberaries 
)


## we want that when we are doing pip install on requirements file this setup is trigerred
## write -e . for that purpose 
