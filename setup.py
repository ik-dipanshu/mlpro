from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """Read requirements from a file and return a clean list of dependencies."""
    with open(file_path, "r") as f:
        # Read lines and strip Windows/Linux whitespace (\n, \r, spaces)
        requirements = [req.strip() for req in f.readlines()]
    
    # Filter out empty lines, comments, and any editable flags (-e)
    cleaned_requirements = []
    for req in requirements:
        if req and not req.startswith("#") and not req.startswith("-e"):
            cleaned_requirements.append(req)
            
    return cleaned_requirements

setup(  
    name="my_package",  
    version="0.1.0",
    author="Dipanshu",
    author_email="dipanshupatel.880@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)