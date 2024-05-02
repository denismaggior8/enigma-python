from setuptools import setup, find_packages


setup(
    author="Denis Maggiorotto",
    long_description=open('enigmapython/README.txt').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/denismaggior8/enigma-python",
    name="enigmapython",
    version="v0.1.1",
    packages=find_packages(
        # All keyword arguments below are optional:
        where='.',  # '.' by default
        include=['enigmapython'],  # ['*'] by default
    ),
    description="A simple yet faithful library to emulate different Enigma machines models using Python"
)