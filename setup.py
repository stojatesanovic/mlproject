from setuptools import find_packages, setup
from typing import List

CONST_E_DOT = ' -e .'
def get_requirements(file_path:str) -> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if CONST_E_DOT in requirements:
            requirements.remove(CONST_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Stoja',
    author_email='stojankatesanovic@gmail.com',
    packages=find_packages(),
    install_requiers=get_requirements('requirements.txt')
)