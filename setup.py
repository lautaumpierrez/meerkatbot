from setuptools import find_packages, setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='meerkatbot',
    packages=find_packages(include=["meerkatbot"]),
    version='0.1.0.2',
    description='MeerkatBot is an extra layout to discord py',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Lautaro Umpiérrez',
    license='MIT',
    install_requires=['discord', 'asyncio'],
    url="https://github.com/lautaumpierrez/meerkatbot.git"
)
