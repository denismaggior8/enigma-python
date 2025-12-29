from setuptools import setup, find_packages
from pathlib import Path


this_directory = Path(__file__).parent
long_description = (this_directory/".."/".."/"README.md").read_text()


setup(
    author="Denis Maggiorotto",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/denismaggior8/enigma-python",
    name="enigmapython",
    version="3.0.0",
    packages=find_packages(
        # All keyword arguments below are optional:
        where='.',  # '.' by default
        include=['enigmapython'],  # ['*'] by default
    ),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    license="MIT",
    description="A simple yet faithful library to emulate different Enigma machines models using Python"
)