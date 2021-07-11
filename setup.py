from setuptools import find_packages, setup

setup(
    name='meerkatbot',
    packages=find_packages(include=["meerkatbot"]),
    version='0.1.0',
    description='MeerkatBot is an extra layout to discord py',
    author='Lautaro Umpiérrez',
    license='MIT',
    install_requires=['discord', 'asyncio']
)
