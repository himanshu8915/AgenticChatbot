"""
setup.py - A script for packaging and distributing the Python project.

This script helps configure and distribute the project using setuptools.
It includes metadata about the project, dependencies, and package discovery.
"""

from setuptools import find_packages, setup  # Import necessary functions from setuptools
from typing import List  # Import List for type hinting

def get_requirements() -> List[str]:
    """
    Reads the `requirements.txt` file and returns a list of dependencies.

    This function:
    - Reads each line from `requirements.txt`.
    - Strips whitespace from each line.
    - Ignores empty lines and the '-e .' entry (used for local installation in editable mode).

    Returns:
        List[str]: A list of package dependencies.
    """
    requirement_lst: List[str] = []  # Initialize an empty list for storing requirements
    try:
        with open('requirements.txt', 'r') as file:  # Open the requirements file in read mode
            lines = file.readlines()  # Read all lines into a list
            for line in lines:
                requirement = line.strip()  # Remove leading and trailing whitespace
                if requirement and requirement != '-e .':  # Ignore empty lines and '-e .'
                    requirement_lst.append(requirement)  # Add valid requirements to the list
    except FileNotFoundError:
        print("requirements.txt file not found")  # Error handling if file is missing
    
    return requirement_lst  # Return the list of dependencies

# Setup function to define package metadata and configuration
setup(
    name="AgenticChatbot",  # The name of the package (change this to your package name)
    version="0.0.1",  # The initial version of the package
    author="Himanshu",  # Author's name
    author_email="himanshusharma14024@gmail.com",  # Author's email
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=get_requirements()  # Load dependencies from requirements.txt
)
