from setuptools import find_packages, setup
from typing import List

def get_requirements()-> List[str]:
    
    requriements_lst:List[str]=[]
    try:
        with open('req.txt','r') as f:
            lines=f.readlines()
            for line in lines:
                requriement=line.strip()
                if requriement and requriement!='-e .':
                    requriements_lst.append(requriement)
    except FileNotFoundError:
        print("req.txt not found")
        
    return requriements_lst

setup(
    name="Network Security",
    author="Assis Mohanty",
    version="0.0.1",
    author_email="assis.mohanty.98@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
    
)