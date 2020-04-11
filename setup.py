# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    readme = f.read()

dependencies = [
        'numpy>=1.16.2',
        'tqdm'
]

setup(
    name='workout',
    version='0.0.0',
    description='A command line workout generator',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Tyler Hughes',
    author_email='tylerwhughes91@gmail.com',
    url='https://github.com/twhughes/workout',
    packages=find_packages(),
    install_requires=dependencies,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
