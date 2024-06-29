# setup.py is to create a local package
# we run from app.py we write function in  src folder
# from src.helper import main:

from setuptools import find_packages, setup

setup(
    name='Generative AI project',
    version='0.0.0',
    author='sudheer',
    author_email='sudheer.read@gmail.com',
    packages=find_packages(),
    install_requires=[]
)
