from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    extra_e = '-e .\n'
    requirements= []
    with open(file_path) as file_obj:
        requirements=[req.strip() for req in file_obj.readlines()]
        requirements= [req for req in requirements if req and req != extra_e]
    return requirements

setup(
name= 'ML_project',
version='0.0.1',
author='Sattwik',
author_email='Sattwikdas007@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)