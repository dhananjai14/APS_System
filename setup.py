from setuptools import find_packages, setup
from typing import List

requirements_file_name = 'requirements.txt'
hyphen_e_dot = '-e .'

def get_requirements()->List[str]:
    with open (requirements_file_name) as requirements:
        requirements_lst = requirements.readlines()
    requirements_lst = [requirement_name.replace('\n', '') for requirement_name in requirements_list]
    if hyphen_e_dot in requirements_lst:
        requirements_lst.remove(hyphen_e_dot)
    return requirements_lst

setup(
    name = 'sensor',
    version = '0.0.1',
    author = 'Dhananjai',
    author_email = 'dhananjai.eee@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements()
)

