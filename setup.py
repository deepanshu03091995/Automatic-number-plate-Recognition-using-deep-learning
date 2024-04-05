from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:

    requirements_list: List[str] = []
    return requirements_list


setup(
    name="ANPR",
    version="0.0.1",
    description="Automatic Number Plate detection System",
    author="Deepanshu rajput",
    author_email="deepanshu.dlri@gmail.com",
    packages=find_packages(),
    install_requires=[],
)
